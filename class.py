class student:
    def __init__ (self,name,rollnum,python,maths,science):
        
        self.name=name
        self.rollnum=rollnum
        self.python=python
        self.maths=maths
        self.science=science
    def member(self):
        
        print(self.name)
        print(self.rollnum)
        print(self.python)
        print(self.maths)
        print(self.science)
    
obj=student("kumar",45,87,67,91)
obj.member()
obj1=student("raj",46,87,93,63)
obj1.member()

obj2=student("ram",47,76,79,89)
obj2.member()
