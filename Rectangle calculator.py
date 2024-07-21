
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** .5
    def get_picture(self):
       for i in range(self.width, self.height):
           if i > 50:
               print('Too big for picture')
           else:
               return ("*" * {self.height} * {self.width})
    
           

class Square(Rectangle):
    def __init__(self):
        pass
    def set_side(self, side):
        self.side = side
    def area(self):
        return self.side**2
    def perimeter(self):
        return self.side*4
    def get_amount_inside(self):
        if self.side:
            return Square()
        else:
            return Rectangle()  


try:
    width = input('enter your value: ')
    height = input('enter your value: ')
except: TypeError
print('invalid command')

           
y = Rectangle('width', 'height')
y.get_area()