class Student:

    def __init__(self,name,hometown,age,height,favorite_ice_cream):
        
        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.favorite_ice_cream=favorite_ice_cream

    def print_summary(self):

        print("The student's name is "+str(self.name)+"."+" They are from "+str(self.hometown)+"."+" They are "+str(self.age)+" years old. "+"They are "+str(self.height)+" cm tall. "+"Their favorite ice cream flavor is "+str(self.favorite_ice_cream)+".")

    def get_giraffe_gap(self):

        return (str(500-int(self.height)))

        
