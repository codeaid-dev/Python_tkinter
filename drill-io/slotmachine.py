import tkinter

class Drum:
    def __init__(self):
        self.status = False
        self.index = 0
        self.moveId = None
    def stop(self):
        if self.moveId:
            root.after_cancel(self.moveId)
            self.moveId = None
        judge()
    def move(self):
        self.label['image'] = images[self.index]
        self.label.update()
        self.index = (self.index+1) % 7
        self.moveId = root.after(300,self.move)

status = False
result = ''
def start():
    global status, result
    status = True
    result = ''
    resl['text'] = result
    resl.update()
    for d in drums:
        d.index = 0
        d.move()

def judge():
    global status, result
    if status:
        nums = []
        for d in drums:
            if d.moveId == None:
                nums.append(d.index)
        if len(nums) == 3:
            status = False
            if nums[0] == nums[1] == nums[2]:
                result = '3つ揃った！'
            elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
                result = 'おしい'
            else:
                result = 'ざんねん・・'
            resl['text'] = result
            resl.update()

root = tkinter.Tk()
root.title('スロットマシーン')
#root.geometry('500x300')

resl = tkinter.Label(root, text=result,
            font=('Helvetica', 16),
            fg='red')
resl.pack(pady=10)

f = tkinter.Frame(root)
f.pack(pady=10)

images = []
for i in range(7):
    img = tkinter.PhotoImage(file=f'images/slot{i}.png')
    images.append(img)

drums = []
for i in range(3):
    d = Drum()
    df = tkinter.Frame(f)
    df.grid(row=0,column=i, padx=10, pady=10)
    d.label = tkinter.Label(df, image=images[0])
    d.label.pack()
    d.button = tkinter.Button(df, text='ストップ',
        font=('Helvetica', 16),
        command=d.stop)
    d.button.pack()
    drums.append(d)

s = tkinter.Button(root, text='スタート',
                       font=('Helvetica', 30),
                       command=start)
s.pack(pady=10)

root.mainloop()