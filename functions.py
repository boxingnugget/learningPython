###defining functions exercise
###area of shapes

def areaSquareRectangle(width, height):
    print(width*height)

def areaCircle(radius):
    print((3.14*radius)**2)

def area():
    shape = None
    while shape != "q":
        shape = str(input("'q' to quit. square, rectangle, circle?: "))
        if shape == "square":
            width = float(input("width: "))
            height = float(input("height: "))
            areaSquareRectangle(width, height)
        elif shape == "rectangle":
            width = float(input("width: "))
            height = float(input("height: "))
            areaSquareRectangle(width, height)
        elif shape == "circle":
            radius = float(input("radius: "))
            areaCircle(radius)
        elif shape == "q":
            print("program ended")
        else:
            print("try again")

area()