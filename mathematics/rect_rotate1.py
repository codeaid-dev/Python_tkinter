import tkinter,math

root = tkinter.Tk()
root.title('図形を回転')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='white')
cvs.pack()


# 四角形の中心
cx, cy = 250, 250

# 四角形のサイズ
w, h = 200, 200

# 回転角度（ラジアン）
angle = math.radians(45)

# 元の頂点（中心基準）
points = [
    (-w/2, -h/2),
    ( w/2, -h/2),
    ( w/2,  h/2),
    (-w/2,  h/2)
]

rotated_points = []
for x, y in points:
    # 回転
    rx = x * math.cos(angle) - y * math.sin(angle)
    ry = x * math.sin(angle) + y * math.cos(angle)
    
    # 元の位置に戻す（平行移動）
    rotated_points.append(cx + rx)
    rotated_points.append(cy + ry)

# 描画
cvs.create_polygon(rotated_points, fill="black", width=0)
root.mainloop()