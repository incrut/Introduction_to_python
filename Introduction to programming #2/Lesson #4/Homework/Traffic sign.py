from tkinter import *

window = Tk()
window.title('Traffic sign')
area = Canvas (window, width = 880, height = 560)

area.create_rectangle (0,0, 880, 560, fill = 'white', outline = 'white')
area.create_oval(240, 80, 620, 480, fill = 'red')
area.create_rectangle (250, 240, 610, 320, fill = 'white')


area.pack()
window.mainloop()