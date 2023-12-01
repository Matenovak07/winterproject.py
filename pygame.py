import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame

def show_surprise():
    
    surprise_window = tk.Toplevel(root)
    surprise_window.title("Final Surprise!")
    surprise_window.geometry("1920x1080")  

    
    image = Image.open("your_image_path_here.jpg")  #replace with created imgage
    image = image.resize((1920, 1080), Image.ANTIALIAS)  
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(surprise_window, image=photo)
    label.image = photo
    label.pack()

    
    pygame.mixer.init()
    pygame.mixer.music.load("your_music_file_path_here.mp3")  #replace with music pack
    pygame.mixer.music.play(loops=0)

def thank_you_message():
    messagebox.showinfo("Thank You!", "Thank you for playing the game! We hope you liked it!!!")

 
root = tk.Tk()
root.title("Game Finished")
root.geometry("1920x1080")  


thank_you_message()


surprise_button = tk.Button(root, text="Click me for the final surprise", command=show_surprise, font=("Arial", 16))
surprise_button.pack(pady=20)


root.mainloop()
