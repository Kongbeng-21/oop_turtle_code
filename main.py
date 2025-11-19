import turtle
import random
import math

class PolygonArt:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor("black")
        turtle.tracer(0)
        turtle.colormode(255)

    def get_new_color(self):
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

    def draw_polygon(self, num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360 / num_sides)
            turtle.penup()
    def draw_art1(self):
        num_sides = random.randint(3, 5) 
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = self.get_new_color()
        border_size = random.randint(1, 10)
        self.draw_polygon(num_sides, size, orientation, location, color, border_size)
        reduction_ratio = 0.618

        turtle.penup()
        turtle.forward(size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]

        size *= reduction_ratio

        self.draw_polygon(num_sides, size, orientation, location, color, border_size)

    def draw_art2(self):
        num_sides = random.randint(3, 6)
        size = 120
        location = [0, 0]
        border_size = 2

        for angle in range(0, 360, 15):
            color = self.get_new_color()
            self.draw_polygon(num_sides, size, angle, location, color, border_size)

    def draw_art3(self):
        for _ in range(40):
            num_sides = random.randint(3, 6)
            size = random.randint(20, 60)
            orientation = random.randint(0, 360)
            location = [
                random.randint(-320, 320),
                random.randint(-220, 220),
            ]
            color = self.get_new_color()
            border_size = random.randint(1, 4)
            self.draw_polygon(num_sides, size, orientation, location, color, border_size)

    def draw_art4(self):
        num_sides = random.randint(3, 6)
        size = 220
        location = [0, 0]
        orientation = random.randint(0, 360)
        border_size = 3

        for i in range(6):
            color = self.get_new_color()
            self.draw_polygon(num_sides, size, orientation, location, color, border_size)
            size *= 0.7          
            orientation += 10     

    def draw_art5(self):
        num_sides = 4           
        base_size = 30
        border_size = 2

        for i in range(30):
            angle = i * 12               
            radius = 10 + i * 8          
            rad = math.radians(angle)
            x = radius * math.cos(rad)
            y = radius * math.sin(rad)

            size = base_size * (0.7 ** (i / 10))  
            color = self.get_new_color()
            self.draw_polygon(num_sides, size, angle, [x, y], color, border_size)

    def draw_art6(self):
        border_size = 2

        for x in range(-320, 321, 40):
            y = 100 * math.sin(math.radians(x * 2))
            num_sides = random.randint(3, 5)
            size = 30
            orientation = random.randint(0, 360)
            color = self.get_new_color()
            self.draw_polygon(num_sides, size, orientation, [x, y], color, border_size)


    def draw_art7(self):
        radius = 180
        num_sides = random.randint(3, 6)
        size = 40
        border_size = 2

        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            x = radius * math.cos(rad)
            y = radius * math.sin(rad)
            color = self.get_new_color()
            self.draw_polygon(num_sides, size, angle, [x, y], color, border_size)

    def draw_art8(self):
        start_x = -250
        start_y = 200
        step = 100
        border_size = 2

        for row in range(4):        
            for col in range(5):    
                x = start_x + col * step
                y = start_y - row * step
                num_sides = random.randint(3, 6)
                size = 40
                orientation = random.randint(0, 360)
                color = self.get_new_color()
                self.draw_polygon(num_sides, size, orientation, [x, y], color, border_size)

    def draw_art9(self):
        locations = [
            [-250, 200],   
            [250, 200],    
            [-250, -200],  
            [250, -200],  
        ]

        num_sides = random.randint(3, 5)
        base_size = 120
        border_size = 3

        for loc in locations:
            size = base_size
            orientation = random.randint(0, 360)

            for _ in range(3):   
                color = self.get_new_color()
                self.draw_polygon(num_sides, size, orientation, loc, color, border_size)
                size *= 0.6
                orientation += 10


    def generate(self, choice: int):
        if choice == 1:
            self.draw_art1()
        elif choice == 2:
            self.draw_art2()
        elif choice == 3:
            self.draw_art3()
        elif choice == 4:
            self.draw_art4()
        elif choice == 5:
            self.draw_art5()
        elif choice == 6:
            self.draw_art6()
        elif choice == 7:
            self.draw_art7()
        elif choice == 8:
            self.draw_art8()
        elif choice == 9:
            self.draw_art9()
        else:
            print("Invalid choice")

        turtle.update()


def main():
    choice_str = input(
        "Which art do you want to generate? Enter a number between 1 to 9 inclusive: "
    )

    try:
        choice = int(choice_str)
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 9.")
        return

    art = PolygonArt()
    art.generate(choice)

    turtle.done()


if __name__ == "__main__":
    main()
