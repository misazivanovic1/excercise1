import easygui as g


class Animal():
    def __init__(self,sound):
        self.sound = sound
    
    def make_sound(self):
        g.msgbox(self.sound)
    
    def move(self, steps):
        g.msgbox(f"I have moved {steps} steps.")

class Bear(Animal):
    def __init__(self, sound):
        super().__init__(sound)
    def name(self):
        g.msgbox("I am bear")
        
anml = Animal("Grrrr")
anml.make_sound()
anml.move(100)

lovellybear = Bear("Roooarrrr")
lovellybear.make_sound()
lovellybear.move(55)
lovellybear.name()