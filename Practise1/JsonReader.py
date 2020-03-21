_author_ = "aman"
import json as js
class JsonReader:

    def __init__(self, sch):
        self.sch = sch

    def parse_json(self):
        with open("C:\\Users\\aman.raj\\Desktop\\python_output\\jobs.json") as jfile:
            y = js.load(jfile)
        return y[self.sch]
