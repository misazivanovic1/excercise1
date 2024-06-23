import easygui as g

lst_clr = ["Red","Blue","Pink","Yellow","Black","Purple","One","Two","Three"]

clr = g.buttonbox(msg="Please choose one color", title="color choices",choices=(lst_clr))


if clr=="Red":
    g.msgbox(f"red is my favourite color go {clr}",title="results")
elif clr =="Blue":
    g.msgbox(f"Blue is an awesome color go {clr}",title="results")
elif clr =="Pink":
    g.msgbox(f"Die hard Pink fan here!! Go {clr}",title="results")
else:
    g.msgbox("Please make a choice.")
