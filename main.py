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
            
    def draw_nested_polygons(self, num_sides, center, base_size, layers):
        orientation = random.randint(0, 360)
        color = self.get_new_color()
        border_size = 2

        size = base_size
        for _ in range(layers):
            self.draw_polygon(num_sides, size, orientation, center, color, border_size)
            size *= 0.7
            
    def draw_art1(self):
        for _ in range(30):  
            center_x = random.randint(-320, 320)
            center_y = random.randint(-240, 240)
            base_size = random.randint(40, 140)
            layers = random.randint(1, 2)   # 1 = เดี่ยว, 2 = ซ้อนสองชั้น
            self.draw_nested_polygons(
                num_sides=3,
                center=[center_x, center_y],
                base_size=base_size,
                layers=layers
            )
    def draw_art2(self):
        for _ in range(35):  
            num_sides = 4                       
            size = random.randint(30, 150)     
            orientation = random.randint(0, 360)
            x = random.randint(-320, 320)       
            y = random.randint(-240, 240)
            color = self.get_new_color()
            border_size = 2

            self.draw_polygon(num_sides, size, orientation, [x, y], color, border_size)

    def draw_art3(self):
        for _ in range(35):
            num_sides = 5                       
            size = random.randint(30, 150)
            orientation = random.randint(0, 360)
            location = [
                random.randint(-320, 320),
                random.randint(-240, 240),
            ]
            color = self.get_new_color()
            border_size = 2
            self.draw_polygon(num_sides, size, orientation, location, color, border_size)

    def draw_art4(self):
        for _ in range(40):
            num_sides = random.randint(3, 5)        
            size = random.randint(30, 150)
            orientation = random.randint(0, 360)
            x = random.randint(-320, 320)
            y = random.randint(-240, 240)
            color = self.get_new_color()
            border_size = 2
            self.draw_polygon(num_sides, size, orientation, [x, y], color, border_size) 

    def draw_art5(self):
        for _ in range(32):  
            center_x = random.randint(-200, 200)
            center_y = random.randint(-150, 150)
            base_size = random.randint(70, 140)
            layers = random.randint(3, 4)
            self.draw_nested_polygons(
                num_sides=3,
                center=[center_x, center_y],
                base_size=base_size,
                layers=layers
            )

    def draw_art6(self):
        for _ in range(18):
            center_x = random.randint(-320, 320)
            center_y = random.randint(-240, 240)
            base_size = random.randint(40, 140)
            layers = random.randint(2, 4)
            self.draw_nested_polygons(
                num_sides=4,
                center=[center_x, center_y],
                base_size=base_size,
                layers=layers
            )


    def draw_art7(self):
        for _ in range(18):
            center_x = random.randint(-320, 320)
            center_y = random.randint(-240, 240)
            base_size = random.randint(40, 140)
            layers = random.randint(2, 4)
            self.draw_nested_polygons(
                num_sides=5,
                center=[center_x, center_y],
                base_size=base_size,
                layers=layers
            )


    def draw_art8(self):
        for _ in range(20):
            num_sides = random.randint(3, 5)
            center_x = random.randint(-320, 320)
            center_y = random.randint(-240, 240)
            base_size = random.randint(40, 140)
            layers = random.randint(2, 4)
            self.draw_nested_polygons(
                num_sides=num_sides,
                center=[center_x, center_y],
                base_size=base_size,
                layers=layers
            )

    def draw_art9(self):
        for _ in range(18):
            num_sides = random.randint(3, 5)
            size = random.randint(30, 120)
            orientation = random.randint(0, 360)
            x = random.randint(-320, 320)
            y = random.randint(-240, 240)
            color = self.get_new_color()
            border_size = 2
            self.draw_polygon(num_sides, size, orientation, [x, y], color, border_size)

        for _ in range(12):
            num_sides = random.randint(3, 5)
            center_x = random.randint(-320, 320)
            center_y = random.randint(-240, 240)
            base_size = random.randint(40, 140)
            layers = random.randint(2, 4)
            self.draw_nested_polygons(
                num_sides=num_sides,
                center=[center_x, center_y],
                base_size=base_size,
                layers=layers
            )


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
