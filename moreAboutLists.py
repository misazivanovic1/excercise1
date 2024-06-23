import easygui as g

shopping_list = [
    "bread",#0
    "milk",#1
    "eggs",#2
    "oranges",#3
    "juice",#4
    "rice",#5
    "beef",#6
    "tomatoes"#7
]#lists have square brackets around them
shopping_touple = (
    "bread",#0
    "milk",#1
    "eggs",#2
    "oranges",#3
    "juice",#4
    "rice",#5
    "beef",#6
    "tomatoes"#7
)#touples have parentheses around them

# g.msgbox(f"I am going to buy me some {shopping_list[2]} and some {shopping_list[1]} and some {shopping_touple[7]}")
# shopping_list.append("apples")#adds to the list to the last possition

# g.msgbox(shopping_list)
# shopping_list.append("cake")
# g.msgbox(shopping_list)

# shopping_list.pop()#removes the last item of the list
# g.msgbox(shopping_list)
results = g.buttonbox("Please pick one", title="Shopping list",choices=(shopping_touple))
g.msgbox(f"You have bought {results}.")