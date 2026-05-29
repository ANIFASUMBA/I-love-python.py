import turtle

# 1. Set up the canvas
screen = turtle.Screen()
screen.bgcolor("black")  # Black background makes the red and pink pop!
screen.title("Anifa's Tech Flower")
screen.setup(width=800, height=800)

# 2. Set up the drawing pen
pen = turtle.Turtle()
pen.speed(0)      # Speed 0 is the fastest, making the drawing look like a smooth animation
pen.pensize(2)

# A list of attractive red/pink shades to give it depth
colors = ["#ff0000", "#ff1a1a", "#ff4d4d", "#e60000", "#cc0000", "#ff0066"]

# 3. Draw the Heart-Shaped Flower
# This loop draws 36 hearts in a circle. Watching it draw creates the "moving" effect.
for i in range(36):
    pen.color(colors[i % len(colors)]) # Cycle through our amazing colors
    
    # Point the pen in a new direction for the next petal
    pen.setheading(i * 10)
    
    # Mathematical steps to draw a perfect heart
    pen.left(140)
    pen.forward(150)
    pen.circle(-75, 200)
    pen.left(120)
    pen.circle(-75, 200)
    pen.forward(150)

# 4. Add your unique text
pen.penup()

# Write your name
pen.goto(0, -20) 
pen.color("white") # Crisp white text against the black background
pen.write("ANIFA SUMBA", align="center", font=("Arial", 30, "bold"))

# Write your tech title
pen.goto(0, -60)
pen.color("hotpink") # Fun tech color
pen.write("Am a girl in TECH 💻", align="center", font=("Courier", 18, "bold"))

pen.hideturtle() # Hide the little drawing arrow when finished

# Keep the beautiful window open until you click on it
screen.exitonclick()