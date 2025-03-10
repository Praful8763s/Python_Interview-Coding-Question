# Perimeter of Rectangle and Area of Rectangle
# # # def area_of_rectangle(length,breadth):
# # #     return length * breadth
# # # length = int(input("enter the length of rectangle"))
# # # breadth = int(input("enter the breadth of rectangle"))
# # # print("Area of Rectangle are :   ", area_of_rectangle(length,breadth))
# # def perimeter_of_rectangle(length,breadth):
# #     return 2*(length + breadth)
# # length = int(input("enter the length of rectangle"))
# # breadth = int(input("enter the breadth of rectangle"))
# # print("Perimeter of Rectangle are ", perimeter_of_rectangle(length,breadth))


#Area and Perimeter of Square
# def area_square(side):
    
#     return side * side
# def perimeter_square(side):
#     return 4 * side
# side = int(input("Enter the sides of square"))
# print(area_square(side))
# print(perimeter_square(side))

#Perimeter and area of triangle
def area_triangle(base,height):
    return base * height
def perimeter_triangle(base,height):
    return 0.5 * base * height
base = int(input("enter the base of triangle are :"))
height = int(input("enter the height of triangle are : "))
print("Perimeter of Triangle are : ", perimeter_triangle(base,height))
print("Area of Triangle are : ", area_triangle(base,height))