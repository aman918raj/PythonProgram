import sched, time, datetime
import tkinter
from PIL import Image, ImageTk
from Practise1.JsonReader import JsonReader

def drink_water():
    window = tkinter.Tk()
    window.title("GUI")
    load = Image.open("C:\\Users\\aman.raj\\MyProject\\"
                      "PythonProgram\\images\\water.jpg")
    icon = ImageTk.PhotoImage(load)
    label = tkinter.Label(window, image=icon)
    tkinter.Label(window, text="Drink Water").pack()
    label.pack()

    window.mainloop()

s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    d = datetime.datetime.now()
    t = d.time()
    print(t.hour, t.minute)
    print("Doing stuff...")
    r = JsonReader("repeat")
    sch = JsonReader("schedule")
    print(r.parse_json())
    print(s.parse_json())
    # do your stuff
    s.enter(60, 1, do_something, (sch))


s.enter(60, 1, do_something, (s,))
s.run()