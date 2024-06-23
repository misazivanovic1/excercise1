import easygui as g

class Animal():
    def __init__(self,type_of_animal,name, age, size):
        self.type = type_of_animal
        self.name = name
        self.age = age
        self.size = size
        self.attitude = ["Loves children","Loves to eat","Loves long walks"]

dog = Animal("dog","Fido",3,"medium")
cat = Animal("cat","Garfield",2,"small")

lst_of_animals=[dog,cat]
for x in lst_of_animals:
    msg1 = f"""
Hello I am a {x.type}, my name is {x.name}
i am {x.age} years old, and i am {x.size} size
and I love {x.attitude[0]}
"""
    g.msgbox(msg1)