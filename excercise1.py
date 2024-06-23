#make a questionaire with 5 questions
#display users answers in a messagebox

import easygui as g

name = g.enterbox("What is your name?")
last_name = g.enterbox("What is your last name?")
age = g.enterbox("How old are you?")
country = g.enterbox("Where do you live?")
movie = g.enterbox("What is your favourite movie?")

answer = f"""
Your name is {name}
your last name is {last_name}
you are {age} years old
and your favourite movie is {movie}.
Thank you for doing this excercise.
"""

g.msgbox(answer)