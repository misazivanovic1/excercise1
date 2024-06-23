import easygui as g

#as long as it is true = while loop

# lst_num = []
# for x in range(2,1001,2):#if not stated it starts from 0 and goes up to the number, not including
#     lst_num.append(x)

# g.msgbox(lst_num)

lst_colors = [
    "red",
    "blue",
    "orange",
    "black",
    "gray",
    "green",
    "pink"
]
for x in lst_colors:
    g.msgbox(x)

#for color in lst_colors