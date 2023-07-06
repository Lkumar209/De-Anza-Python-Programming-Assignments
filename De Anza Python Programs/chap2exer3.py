'''
Laxya Kumar
This code prompts the user for input to create a graphics window, draws a circle with specified attributes, and calculates and displays its circumference and area using the ezgraphics package.
'''



from ezgraphics import GraphicsWindow, GraphicsCanvas

# Prompt the user for input
width = float(input("Enter the width of the graphics window: "))
height = float(input("Enter the height of the graphics window: "))
radius = float(input("Enter the radius of the circle: "))
outline_color = input("Enter the outline color of the circle: ")
fill_color = input("Enter the fill color of the circle: ")

# Create the graphics window
win = GraphicsWindow(width, height)
canvas = win.canvas()

canvas.setBackground(255, 255, 224)

canvas.setTextAnchor("nw")

canvas.setLineWidth(5)

win.setTitle("Circle Drawing")

circumference = 2 * 3.14159 * radius
area = 3.14159 * radius ** 2

center_x = width / 2
center_y = height / 2
canvas.setOutline(outline_color)
canvas.setFill(fill_color)
canvas.drawOval(center_x - radius, center_y - radius, 2 * radius, 2 * radius)

text_x = 0.01 * width
text_y = 0.01 * height
message = f"Circumference: {circumference}\nArea: {area}"
canvas.drawText(text_x, text_y, message)

win.wait()



'''
Output 1:

Enter the width of the graphics window: 600
Enter the height of the graphics window: 400
Enter the radius of the circle: 150
Enter the outline color of the circle: red
Enter the fill color of the circle: yellow
Circumference: 942.478
Area: 70685.8


Enter the width of the graphics window: 800
Enter the height of the graphics window: 800
Enter the radius of the circle: 200
Enter the outline color of the circle: blue
Enter the fill color of the circle: green
Circumference: 1256.64
Area: 125663.2



'''
