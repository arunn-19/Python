'''class ABC:
    var=10
object_name=ABC()
print(object_name.var)'''

class abc():
    def __init__(self,name):
        self.name=name
        print('name:',name)
object=abc('XYZ')