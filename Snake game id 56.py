from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Window size
WIDTH = 600
HEIGHT = 600

# Box size
SIZE = 20

# Snake body
snake = [(5, 5), (4, 5), (3, 5)]

# First direction
direction = "RIGHT"

# Food position
food = (10, 10)

# Game over check
game_over = False

# Score
score = 0


# Draw box
def draw_box(x, y, r, g, b):

    glColor3f(r, g, b)

    glBegin(GL_QUADS)

    glVertex2f(x * SIZE, y * SIZE)
    glVertex2f((x + 1) * SIZE, y * SIZE)
    glVertex2f((x + 1) * SIZE, (y + 1) * SIZE)
    glVertex2f(x * SIZE, (y + 1) * SIZE)

    glEnd()


# Display everything
def display():

    glClear(GL_COLOR_BUFFER_BIT)

    # Draw snake
    for part in snake:
        draw_box(part[0], part[1], 0, 1, 0)

    # Draw food
    draw_box(food[0], food[1], 1, 0, 0)

    # Show score
    glColor3f(1, 1, 0)

    glRasterPos2f(10, 570)

    text = "Score : " + str(score)

    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

    # Game over text
    if game_over:

        glColor3f(1, 1, 1)

        glRasterPos2f(180, 300)

        text = "GAME OVER - Press SPACE"

        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

    glutSwapBuffers()


# Update game
def update(value):

    global snake, food, game_over, score

    if game_over:
        return

    # Snake head
    x = snake[0][0]
    y = snake[0][1]

    # Movement
    if direction == "UP":
        y += 1

    elif direction == "DOWN":
        y -= 1

    elif direction == "LEFT":
        x -= 1

    elif direction == "RIGHT":
        x += 1

    new_head = (x, y)

    # Wall collision
    if x < 0 or x >= 30 or y < 0 or y >= 30:
        game_over = True

    # Body collision
    elif new_head in snake:
        game_over = True

    else:

        # Add new head
        snake.insert(0, new_head)

        # Food eat
        if new_head == food:

            score += 10

            food = (
                random.randint(0, 29),
                random.randint(0, 29)
            )

        else:
            snake.pop()

    glutPostRedisplay()

    glutTimerFunc(100, update, 0)


# Arrow key control
def special_keys(key, x, y):

    global direction

    if key == GLUT_KEY_UP and direction != "DOWN":
        direction = "UP"

    elif key == GLUT_KEY_DOWN and direction != "UP":
        direction = "DOWN"

    elif key == GLUT_KEY_LEFT and direction != "RIGHT":
        direction = "LEFT"

    elif key == GLUT_KEY_RIGHT and direction != "LEFT":
        direction = "RIGHT"


# Keyboard control
def keyboard(key, x, y):

    global snake, direction, food, game_over, score

    # Restart game
    if key == b' ' and game_over:

        snake = [(5, 5), (4, 5), (3, 5)]

        direction = "RIGHT"

        food = (10, 10)

        score = 0

        game_over = False

        glutTimerFunc(100, update, 0)


# OpenGL setup
def init():

    glClearColor(0, 0, 0, 1)

    glMatrixMode(GL_PROJECTION)

    gluOrtho2D(0, WIDTH, 0, HEIGHT)


# Main function
glutInit()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

glutInitWindowSize(WIDTH, HEIGHT)

glutCreateWindow(b"Snake Game With Score")

init()

glutDisplayFunc(display)

glutSpecialFunc(special_keys)

glutKeyboardFunc(keyboard)

glutTimerFunc(100, update, 0)

glutMainLoop()