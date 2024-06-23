import easygui as g

# if this is true:# it will be done/checked once
#     do this

# while this is true:#it will be done as long as the condition is true
#     do this

run = True

while run:#do this forever, there is no way to change True to False
    result = g.buttonbox("I love python!",title="BTN",choices=("Continue","Not"))
    if result == "Not":
        run=False