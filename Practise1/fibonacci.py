_author_ = "aman"

def fibonaci(n, a = 0, b = 1):
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return fibonaci(n-1, b, a + b)

fib = fibonaci(9)
print(fib)

st1 = "{0} abc {1} def {2}".format("a","b","c")
st2 = """a"""+" abc "+"b"+" def "+"c"
print(st1)
print(st2)

st3 = """abc 
def"""+st1+"""
xyz
"""
print(st3)
def on_launch(event):
    onlunch_MSG = "Hi, welcome to the My Favourite Chess Player Alexa Skill."\
    "If you would like to hear about any disease related precaution or cure, " \
                  "you could say for example: i have got cold or i have got fever?"
    reprompt_MSG = "Do you want to hear more about any other issue?"
    card_TEXT = "Pick a chess payer."
    card_TITLE = "Choose a chess player."
    return output_json_builder_with_reprompt_and_card(onlunch_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)


