import tkinter, random

class Circle:
    pass

circles = []

def pressed(e):
    en = Circle()
    en.x = e.x-25
    en.y = e.y-25
    en.speedx = random.randint(2,3)
    en.speedy = random.randint(1,3)
    en.color = 'black'
    en.id = cvs.create_oval(en.x,en.y,en.x+50,en.y+50,fill=en.color,width=0)
    circles.append(en)

def main():
    for en in circles:
        en.x += en.speedx
        en.y += en.speedy
        if en.x < 0 or en.x > 450:
            en.speedx *= -1
            en.color = f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'
        elif en.y < 0 or en.y > 450:
            en.speedy *= -1
            en.color = f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'
        cvs.itemconfig(en.id,fill=en.color)
        cvs.coords(en.id,en.x,en.y,en.x+50,en.y+50)

    root.after(10,main)

root = tkinter.Tk()
root.title('クリックしたところに円を表示し移動する')
root.bind('<Button>',pressed)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()

main()
root.mainloop()