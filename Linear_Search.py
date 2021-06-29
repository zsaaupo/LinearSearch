"""Linear Search"""
print(__doc__)


class LinearSearch :


    def __init__(self, array_01, f_value):

        self.array = array_01
        self.f_value = f_value


    def liner_search (self):

        for i in range(len(self.array)):

            if self.f_value == self.array[i]:
                
                self.a = i, "is the index number of value"
                return self.a
                
            elif i == len(self.array) - 1 and self.f_value != self.array[i]:
                
                self.b = "value not found"
                return self.b
                



ls_obj_1 = LinearSearch([2, 5, 6, 4, 8,], 8)
print(ls_obj_1.liner_search())


ls_obj_2 = LinearSearch(input("input an array = ").split(), (input("input finding value = ")))
print(ls_obj_2.liner_search())