from threading import *
from tkinter import *
import tkinter as tk
import datetime
import threading
import time
from PIL import ImageTk, Image
c = 0
dates = ["2022-10-11","2022-10-18","2022-10-25","2022-11-1","2022-11-8","2022-11-15","2022-11-22","2022-11-29","2022-12-6","2022-12-13","2022-12-20","2022-12-27"]

hide2 = False

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs): # Creating a rounded rectangle
        
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
            
        return canvas.create_polygon(points, **kwargs, smooth=True, fill="#1fa5fe")



def move_window(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')

image = Image.open('csm poster.jpg')
new_image = image.resize((282, 422))
new_image.save('csm poster.jpg')
yy = True
images = []

def create_rectangle(x1, y1, x2, y2, **kwargs):
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = Image.new('RGBA', (x2-x1, y2-y1), fill)
        images.append(ImageTk.PhotoImage(image))
        canvas.create_image(x1, y1, image=images[-1], anchor='nw')
    canvas.create_rectangle(x1, y1, x2, y2, **kwargs)




def CSM_timer():
    while yy:
        global bb
        if bb == False:
            time.sleep(1)  
        bb = False
        times2233 = []
        times3322 = []
        for date in dates:
            datey = date.split('-')

            year2 = int(datey[0])
            month2 = int(datey[1])
            day2 = int(datey[2])


            today   = datetime.date.today()
            today2 = str(today)
            today2 = today2.split('-')
            year1 = today2[0]
            month1 = today2[1]
            day1= today2[2]

            now = datetime.datetime.now()
            x = len(str(today))

            now = str(now)
            now = now[int(x+1):]
            now2 = now.split('.')
            now = now2[0]
            now = now.split(':')
            hours1 = now[0]
            minutes1 = now[1]
            seconds1 = now[2]
            a = datetime.datetime(int(year1),int(month1),int(day1),int(hours1),int(minutes1),int(seconds1))
            b = datetime.datetime(year2,month2,day2,17,0,0)

            c = (b-a).total_seconds()
            if int(c) < 0:

                times3322.append(c)
            else:

                times2233.append(float(c))   
                times3322.append(c)  

        date2 = times2233.index(min(times2233))

        times2233 = min(times2233)
        date4 = times3322.index(min([n for n in times3322  if n>0]))
        c = times2233

        date3 = dates[date2]

        result = datetime.timedelta(seconds = c)
        result = str(result)
        days33 = []
        try:
            result = result.split(',')



            canvas.itemconfigure(timetxt,text=f"{result[0]} {result[1]}")
        except:
            canvas.itemconfigure(timetxt,text=f"{result[0]}")
        canvas.itemconfigure(timetxt2,text=f"Episode {date4 + 1}")


        root.update()
global Enter








image = Image.open('csm 103.png')
new_image = image.resize((250, 50))
new_image.save('csm 104.png')



def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

xx = True
xxx33 = 0
xx2233 = 0




bb = True
root = Tk()
root.overrideredirect(1)
root.bind("<B1-Motion>", move_window)
root.eval('tk::PlaceWindow . center')
root.title("Chainsaw Man Timer")
root.geometry('282x422')
root.config(background='grey')
root.attributes("-transparentcolor", "grey")

frame = Frame(root, width=50, height=30)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
canvas = Canvas(root, bg="grey", highlightthickness=0)
canvas.pack(fill=BOTH, expand=1)
img = ImageTk.PhotoImage(Image.open("csm poster.jpg"))
img2 = ImageTk.PhotoImage(Image.open("csm 104.png"))
image_container = canvas.create_image(0,0,anchor="nw",image=img)

image_container2 = canvas.create_image(138,40,anchor="center",image=img2)
m = Menu(root, tearoff=0)
m.add_command(label="Close",command=root.destroy)
timetxt = canvas.create_text(141,400,text="Test",font=("Edge Of Madness", 15),anchor="center",fill='white')
timetxt2 = canvas.create_text(141,375,text="Test",font=("Nerve Agent", 15),anchor="center",fill='white')
root.bind("<Button-3>", do_popup)
tt = threading.Thread(target=CSM_timer)
tt.setDaemon(True)



tt.start()









    
    
    
root.mainloop()
