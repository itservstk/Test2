class MyObject():

    def __init__(self):
            self.attribute=2
            self._inner_attribute=3
            self.__private_attribute=4
 
obj=MyObject()
print(obj._MyObject__private_attribute)