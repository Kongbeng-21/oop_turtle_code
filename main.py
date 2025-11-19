import turtle
import random

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
        pass

    def draw_art6(self):
        pass

    def draw_art7(self):
        pass

    def draw_art8(self):
        pass

    def draw_art9(self):
        pass

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
