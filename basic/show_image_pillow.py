import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title('画像表示(JPEG)')
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()
img = Image.open('./images/trees.jpg')
img_jpeg = ImageTk.PhotoImage(img)
cvs.create_image(250,250,image=img_jpeg)

root.mainloop()