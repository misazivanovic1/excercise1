import easygui as g

message = "It is wonderful and amazing day today. I am"
message2 = "I love python."
name = g.enterbox("Please type in your name")

g.msgbox(message+" "+name+" and "+message2)

