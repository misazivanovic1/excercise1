import easygui as g

user = g.enterbox("What is your username?")
password = g.enterbox("What is your password?")
correct_user = "user1"
correct_password = "password1"


# if user == correct_user:
#     if password==correct_password:
#         g.msgbox(f"Welcome sir {user}, your password is correct.")
#     else:
#         g.msgbox("Wrong password.")
if user == correct_user or password==correct_password:
    g.msgbox(f"Welcome sir {user}, your password is correct.")
else:
    g.msgbox("Wrong username or password.")
# g.msgbox(f"Your username is {user} and your password is {password}")
