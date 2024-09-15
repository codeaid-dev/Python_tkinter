import tkinter
from PIL import Image, ImageTk

WIDTH,HEIGHT = 600,600
root = tkinter.Tk()
root.title("ルーレット")
cvs = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
cvs.pack()

img = Image.open('./images/roulette.png')
photo_img = ImageTk.PhotoImage(img)
cvs.create_image(WIDTH/2, HEIGHT/2, image=photo_img)
cvs.create_line(WIDTH/2,0,WIDTH/2,100,fill='red',width=5)
angle = 0

def rotate_image():
    global photo_img, angle
    if img and is_rotating:
        angle += 10
        rotated_img = img.rotate(angle, expand=True)
        photo_img = ImageTk.PhotoImage(rotated_img)
        cvs.create_image(WIDTH/2, HEIGHT/2, image=photo_img)
        cvs.create_line(WIDTH/2,0,WIDTH/2,100,fill='red',width=5)
    root.after(50,rotate_image)

is_rotating = False
def start_rotation():
    global is_rotating
    if img and not is_rotating:
        is_rotating = True
        rotate_image()

rotate_button = tkinter.Button(root, text="回転",
                               font=('Helvetica',50),
                               command=start_rotation)
rotate_button.pack(pady=10)

root.mainloop()
