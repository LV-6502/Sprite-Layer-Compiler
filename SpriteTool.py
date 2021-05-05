import tkinter as tk
from tkinter import filedialog, Entry, messagebox
from PIL import ImageTk, Image

filenames = []
all_labels = []
base_labels = []
Layer_0 = Image.new(mode = "RGB", size = (1, 1))
left_img_out = Image.new(mode = "RGB", size = (1, 1))
right_img_out = Image.new(mode = "RGB", size = (1, 1))

def openfile0(xnum,ynum):
    global filename0
    filename0 = filedialog.askopenfilename(parent=window,title="Layer 0")
    if filename0:
        b0_l = tk.Label(window, text = "File path: " + filename0)
        b0_l.place(x=xnum,y=ynum)
        filenames.append(filename0)
        base_labels.append(b0_l)
    else:
        b0_l = tk.Label(window, text = "File path: " + "Nothing Chosen")
        b0_l.place(x=xnum,y=ynum)
        base_labels.append(b0_l)
    
def openfile1(xnum,ynum):
    filename = filedialog.askopenfilename(parent=window, title="Layer 1")
    if filename:
        b1_l = tk.Label(window, text = "File path: " + filename)
        b1_l.place(x=xnum,y=ynum) 
        filenames.append(filename)
        all_labels.append(b1_l)
        all_labels.append(b1_l)
    else:
        b1_l = tk.Label(window, text = "File path: " + "Nothing chosen")
        b1_l.place(x=xnum,y=ynum)
        all_labels.append(b1_l)

def Preview():
    global Layer_0
    global right_img_out
    try:
        Layer_0 = Image.open(filename0)
        for name in filenames:
            try:
                sub_image = Image.open(name)
                Layer_0.paste(sub_image, (0, 0), sub_image)
            except:
                pass
        img_x = ImageTk.PhotoImage(Layer_0)
        right_img_out = ImageTk.getimage(img_x)
        panel = tk.Label(window, image=img_x)
        panel.image = img_x
        panel.place(x=10,y=380)
        all_labels.append(panel)
    except:
        pass
    
def ClearAll():
    global filenames
    global filename0
    global Layer_0
    filenames = []
    Preview()
    for label in all_labels: label.destroy()
    for label in base_labels: label.destroy()
    filename0 = ""
    Layer_0 = Image.new(mode = "RGB", size = (1, 1))
    
def Clear():
    global filenames
    filenames = []
    Preview()
    for label in all_labels: label.destroy()

def FlipLeft():
    global flip_img
    global left_img_out
    try:
        flip_img = Layer_0
        x_value = getXval()
        y_value = getYval()
        width, height = flip_img.size
        limit = int(width/x_value)
        for x in range(limit):
            y = x+1
            sub_image = flip_img.crop(box=((x_value*x),0,(x_value*y),y_value)).transpose(Image.FLIP_LEFT_RIGHT)
            flip_img.paste(sub_image, box=((x_value*x),0))
            img_sub = ImageTk.PhotoImage(flip_img)
            img_PIL = ImageTk.getimage(img_sub)
            flip_img = img_PIL
        img = ImageTk.PhotoImage(flip_img)
        left_img_out = ImageTk.getimage(img)
        panel2 = tk.Label(window, image=img)
        panel2.image = img
        all_labels.append(panel2)
        panel2.place(x=10,y=450)
    except ValueError:
        tk.messagebox.showerror('Hold up','Sprite dimensions required')
    
def getXval():
    global xval
    string = xval.get()
    strtoint = int(string)
    return strtoint

def getYval():
    global yval
    string = yval.get()
    strtoint = int(string)
    return strtoint
    
def SaveFileRight():
    location = filedialog.asksaveasfile(mode='wb', defaultextension=".png")
    if not location:
        return
    right_img_out.save(location, "png")
    
def SaveFileLeft():
    location = filedialog.asksaveasfile(mode='wb', defaultextension=".png")
    if not location:
        return
    left_img_out.save(location, "png")


window = tk.Tk()
window.geometry("1000x600")
window.title("V1.0")
heading = tk.Label(text = "Sprite Layer Compiler", bg="grey", fg="white", width="500",height="3")
heading2 = tk.Label(text = "", bg="grey", fg="white", width="500",height="1")
heading.pack()
heading2.place(x=0,y=350)

Description_Label  = tk.Label(window, text = "Sprite Frame Dimensions").place(x=320,y=260)
X_label = tk.Label(window, text = "Pixel X:").place(x=320,y=280)
xval = Entry(window, width="8")
xval.place(x=370,y=280)
xval.focus_set()
Y_label = tk.Label(window, text = "Pixel Y:").place(x=320,y=300)
yval = Entry(window, width="8")
yval.place(x=370,y=300)
yval.focus_set()

tk.Button(window, text='Layer 0', command= lambda: openfile0(60,60),).place(x=10,y=60)

tk.Button(window, text='Layer 1', command= lambda: openfile1(60,90)).place(x=10,y=90)
tk.Button(window, text='Layer 2', command= lambda: openfile1(60,120)).place(x=10,y=120)
tk.Button(window, text='Layer 3', command= lambda: openfile1(60,150)).place(x=10,y=150)
tk.Button(window, text='Layer 4', command= lambda: openfile1(60,180)).place(x=10,y=180)
tk.Button(window, text='Layer 5', command= lambda: openfile1(60,210)).place(x=10,y=210)
tk.Button(window, text='Layer 6', command= lambda: openfile1(60,240)).place(x=10,y=240)

tk.Button(window, text='Preview', command=Preview, bg="grey", fg="white", width="8",height="1").place(x=10,y=280)
tk.Button(window, text='Flip Left', command=FlipLeft, bg="grey", fg="white", width="8",height="1").place(x=80,y=280)
tk.Button(window, text='Clear', command=Clear, bg="#e12120", fg="white", width="8",height="1").place(x=170,y=280)
tk.Button(window, text='Clear All', command=ClearAll, bg="#971414", fg="white", width="8",height="1").place(x=240,y=280)


tk.Button(window, text='Save Right', command=SaveFileRight, bg="green", fg="white", width="8",height="1").place(x=10,y=310)
tk.Button(window, text='Save Left', command=SaveFileLeft, bg="green", fg="white", width="8",height="1").place(x=80,y=310)


window.mainloop()
