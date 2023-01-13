import tkinter as tk
from tkinter import font
import random
import time
from PIL import Image, ImageTk



root = tk.Tk()
root.title("Snakes Games By Owner#2624 []")

def start_game():
    global snake_color
    snake_color = color_var.get()
    print("La couleur du serpent est:", snake_color)
    # masque l'interface d'accueil et affiche l'interface de jeu
    welcome_frame.pack_forget()
    game_frame.pack()
    play_game()

def play_game():
    global snake_pos, snake_body, snake_dir, food_pos, score, game_over



    # Initialisation de la fenêtre de jeu
    size = (400, 400)

    canvas = tk.Canvas(game_frame, width=size[0], height=size[1], bg="black")
    canvas.pack()

    snake_pos = [size[0]//2, size[1]//2]
    snake_body = [[size[0]//2, size[1]//2], [size[0]//2-10, size[1]//2], [size[0]//2-20, size[1]//2]]
    snake_dir = "right"

    food_pos = [random.randint(0, size[0]-10), random.randint(0, size[1]-10)]
    score = 0
    game_over = False

        # Chargement de l'image
    image = Image.open("image.png")
    photo = ImageTk.PhotoImage(image)

    time.sleep(1.5)

    def draw_snake():
        for pos in snake_body:
            canvas.create_rectangle(pos[0], pos[1], pos[0]+10, pos[1]+10, fill=snake_color)

    def move_snake():
        global game_over, score
        new_head = [snake_body[0][0], snake_body[0][1]]
        if snake_dir == "right":
            new_head[0] += 10
        elif snake_dir == "left":
            new_head[0] -= 10
        elif snake_dir == "up":
            new_head[1] -= 10
        elif snake_dir == "down":
            new_head[1] += 10
        snake_body.insert(0, new_head)
        if new_head[0] < 0 or new_head[0] >= size[0] or new_head[1] < 0 or new_head[1] >= size[1]:
            game_over = True
        if snake_body[0] in snake_body[1:]:
            game_over = True
        if new_head[0] >= food_pos[0] and new_head[0] <= food_pos[0] + 10 and new_head[1] >= food_pos[1] and new_head[1] <= food_pos[1] + 10:
            food_pos[0] = random.randint(0, size[0]-10)
            food_pos[1] = random.randint(0, size[1]-10)
            canvas.delete(food)
            score += 1
        else:
            snake_body.pop()

    def game_loop():
        global game_over
        if not game_over:
            canvas.delete("all")
            move_snake()
            food = canvas.create_rectangle(food_pos[0], food_pos[1], food_pos[0]+10, food_pos[1]+10, fill="red")
            draw_snake()
            canvas.create_text(20, 20, text="Score: " + str(score), font=("Arial", 14), fill="white")
            if score >= 150:
                canvas.create_image(size[0]//2, size[1]//2, image=photo)
                canvas.create_text(size[0]//2, size[1]//2 + 50, text="Félicitations!", font=("Arial", 24), fill="white")
            canvas.update()
            root.after(100, game_loop)
        else:
            canvas.create_text(size[0]//2, size[1]//2, text="Game Over!", font=("Arial", 24), fill="white")
            canvas.update()

    root.bind("<Right>", lambda event: change_dir("right"))
    root.bind("<Left>", lambda event: change_dir("left"))
    root.bind("<Up>", lambda event: change_dir("up"))
    root.bind("<Down>", lambda event: change_dir("down"))
    

# Frame d'accueil
welcome_frame = tk.Frame(root)
welcome_frame.pack()

title_font = font.Font(size=24, weight='bold')
title_label = tk.Label(welcome_frame, text="Snakes Game", font=title_font)
title_label.pack()

play_button = tk.Button(welcome_frame, text="Jouer", command=start_game)
play_button.pack()

color_var = tk.StringVar(value="orange")
color_label = tk.Label(welcome_frame, text="Couleur du serpent :")
color_label.pack()
color_entry = tk.Entry(welcome_frame, textvariable=color_var)
color_entry.pack()

# Frame de jeu
game_frame = tk.Frame(root)
game_loop()
root.mainloop()
