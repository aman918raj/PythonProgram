_author_ = "aman"
import tkinter

window = tkinter.Tk()
window.title("Hello")
window.geometry('640x480')

label = tkinter.Label(window, text="Hello Everyone")
label.pack(side='top')

left_frame = tkinter.Frame(window)
left_frame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=1)
# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)
canvas.pack(side='top')

right_frame = tkinter.Frame(window)
right_frame.pack(side='right', anchor='n', expand=True)
button1 = tkinter.Button(right_frame, text="button1")
button2 = tkinter.Button(right_frame, text="button2")
button3 = tkinter.Button(right_frame, text="button3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

window.mainloop()
