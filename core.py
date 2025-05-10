from ctypes import Structure, c_long, windll, byref

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

point = POINT()

while True:
    windll.user32.GetCursorPos(byref(point))

    print(f"Mouse X={point.x}, Y={point.y}")