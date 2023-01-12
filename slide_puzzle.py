import tkinter
import random

side=150
nums = []
while len(nums) < 9:
    n = random.randint(0,8)
    if n not in nums:
        nums.append(n)

def slide(i):
    if i <= 5 and nums[i+3]==0:
        nums[i], nums[i+3] = nums[i+3], nums[i]
    if i >= 3 and nums[i-3]==0:
        nums[i], nums[i-3] = nums[i-3], nums[i]
    if i%3 != 2 and nums[i+1]==0:
        nums[i], nums[i+1] = nums[i+1], nums[i]
    if i%3 != 0 and nums[i-1]==0:
        nums[i], nums[i-1] = nums[i-1], nums[i]
    cvs.delete('number')
    for i in range(9):
        if nums[i] != 0:
            cvs.create_text(i%3*side+(side/2),i//3*side+(side/2),text=nums[i],font=('メイリオ',40),tags='number')

def click(e):
    for i in range(9):
        if i%3*side<e.x<i%3*side+side and i//3*side<e.y<i//3*side+side:
            slide(i)

root = tkinter.Tk()
root.title('スライドパズル')
root.geometry('450x450')
root.bind('<Button>',click)
cvs = tkinter.Canvas(root,width=450,height=450,bg='white')
cvs.pack()
for i in range(9):
    cvs.create_rectangle(i%3*side,i//3*side,i%3*side+side,i//3*side+side,fill='gray')
    if nums[i] != 0:
        cvs.create_text(i%3*side+(side/2),i//3*side+(side/2),text=nums[i],font=('メイリオ',40),tags='number')

root.mainloop()
