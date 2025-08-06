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
rotation_speed = 10  # 初期の回転速度

def rotate_image():
    global photo_img, angle, is_rotating, rotation_speed
    if img and is_rotating:
        angle = (angle + rotation_speed) % 360
        rotated_img = img.rotate(angle, expand=True)
        photo_img = ImageTk.PhotoImage(rotated_img)
        cvs.create_image(WIDTH/2, HEIGHT/2, image=photo_img)
        cvs.create_line(WIDTH/2,0,WIDTH/2,100,fill='red',width=5)

        # 回転速度を減少させる
        if rotation_speed > 0 and stop_rotating:
            rotation_speed -= 0.1

        # 速度がゼロになるまで回転し続ける
        if rotation_speed > 0:
            root.after(50, rotate_image)
        else:
            is_rotating = False

is_rotating = False
def start_rotation():
    global is_rotating, rotation_speed, stop_rotating
    if img and not is_rotating:
        rotation_speed = 10
        is_rotating = True
        stop_rotating = False
        rotate_image()

stop_rotating = False
def stop_rotation():
    global stop_rotating
    stop_rotating = True

rotate_button = tkinter.Button(root, text="回転",
                               font=('Helvetica',50),
                               command=start_rotation)
rotate_button.pack(pady=10)
stop_button = tkinter.Button(root, text="停止",
                             font=('Helvetica',50),
                             command=stop_rotation)
stop_button.pack(pady=10)

root.mainloop()
