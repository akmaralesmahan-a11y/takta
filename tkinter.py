"""Браузерде (PyScript/Pyodide) жұмыс істейтін минималды tkinter алмастырғышы. Тек Tk, Canvas, Button үшін қажетті командаларды қолдайды.""" import math from js import document from pyodide.ffi import create_proxy
class _Event: def init(self, x, y): self.x = int(x) self.y = int(y)
class Tk: def init(self): self._el = document.createElement("div") self._el.style.cssText = "font-family: sans-serif; margin: 20px;" document.body.appendChild(self._el) self._row = None
def title(self, text):
    document.title = text

def mainloop(self):
    pass  # браузердің өзі оқиғаларды өңдейді

def _add(self, el, side):
    if side == "left":
        if self._row is None:
            self._row = document.createElement("div")
            self._row.style.cssText = "display:flex; gap:4px; margin-top:8px;"
            self._el.appendChild(self._row)
        self._row.appendChild(el)
    else:
        self._row = None
        self._el.appendChild(el)
class Canvas: def init(self, master, width=800, height=500, bg="white", **kw): self._master = master self._el = document.createElement("canvas") self._el.width = width self._el.height = height self._el.style.cssText = ( "background:%s; border:1px solid #888; display:block; " "max-width:100%%; touch-action:none;" % bg ) self._ctx = self._el.getContext("2d") self._next_id = 1
def pack(self, side=None, **kw):
    self._master._add(self._el, side)

def _event(self, e):
    r = self._el.getBoundingClientRect()
    x = (e.clientX - r.left) * self._el.width / r.width
    y = (e.clientY - r.top) * self._el.height / r.height
    return _Event(x, y)

def bind(self, sequence, func):
    if sequence == "<B1-Motion>":
        def handler(e):
            if e.buttons & 1:
                func(self._event(e))
        self._el.addEventListener("pointermove", create_proxy(handler))
    elif sequence == "<Button-1>":
        self._el.addEventListener(
            "pointerdown", create_proxy(lambda e: func(self._event(e))))
    elif sequence == "<ButtonRelease-1>":
        self._el.addEventListener(
            "pointerup", create_proxy(lambda e: func(self._event(e))))

def create_oval(self, x1, y1, x2, y2, fill="", outline="black", width=1, **kw):
    c = self._ctx
    c.beginPath()
    c.ellipse((x1 + x2) / 2, (y1 + y2) / 2,
              abs(x2 - x1) / 2, abs(y2 - y1) / 2, 0, 0, 2 * math.pi)
    if fill:
        c.fillStyle = fill
        c.fill()
    if outline:
        c.strokeStyle = outline
        c.lineWidth = width
        c.stroke()
    self._next_id += 1
    return self._next_id - 1

def delete(self, *args):
    self._ctx.clearRect(0, 0, self._el.width, self._el.height)
class Button: def init(self, master, text="", command=None, **kw): self._master = master self._el = document.createElement("button") self._el.textContent = text self._el.style.cssText = "padding:6px 12px; cursor:pointer;" if command: self._el.addEventListener("click", create_proxy(lambda e: command()))
def pack(self, side=None, **kw):
    self._master._add(self._el, side)
