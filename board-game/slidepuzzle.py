import tkinter
import random

tiles = ['','1','2','3','4','5','6','7','8']
random.shuffle(tiles)

labels = []
root = tkinter.Tk()
root.title('Slide Puzzle')

def slide(label):
    i = tiles.index(label.widget['text'])

    if i <= 5 and tiles[i+3] == '':
        # Replace with below
        tiles[i], tiles[i+3] = tiles[i+3], tiles[i]
        labels[i]['text'] = tiles[i]
        labels[i+3]['text'] = tiles[i+3]
    if i >= 3 and tiles[i-3] == '':
        # Replace with above
        tiles[i], tiles[i-3] = tiles[i-3], tiles[i]
        labels[i]['text'] = tiles[i]
        labels[i-3]['text'] = tiles[i-3]
    if i%3 != 2 and tiles[i+1] == '':
        # Replace with right
        tiles[i], tiles[i+1] = tiles[i+1], tiles[i]
        labels[i]['text'] = tiles[i]
        labels[i+1]['text'] = tiles[i+1]
    if i%3 != 0 and tiles[i-1] == '':
        # Replace with left
        tiles[i], tiles[i-1] = tiles[i-1], tiles[i]
        labels[i]['text'] = tiles[i]
        labels[i-1]['text'] = tiles[i-1]

for i in range(9):
    label = tkinter.Label(root, text=tiles[i], font=('Helvetica', 20), height=3, width=6, borderwidth=2, relief='ridge')
    label.grid(row=i//3, column=i%3)
    label.bind('<ButtonPress>', slide)
    labels.append(label)


root.mainloop()
