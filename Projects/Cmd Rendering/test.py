import cmd
w, h = 900, 500
canvas = cmd.canvas(w,h)
canvas.clear()
canvas.drawBorder()
canvas.render("C:/Users/leopold/Documents/cmd rendering/monkey.obj",200, 450,250, rotate=False,shading=True, color="white")
canvas.cursorResetBottom()
