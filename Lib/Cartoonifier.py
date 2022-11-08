import tkinter as tk
from tkinter import filedialog
from tkinter import *
from cartoonizer import make_cartoon
from PIL import ImageTk, Image
import cv2

top=tk.Tk()
top.geometry('1000x600')
top.title('Cartoonifier')
top.iconbitmap('.\\Pictures\\df_icon.ico')
top.configure(background='white')


    
    
def save_cartoon(file_path_c,cartoon_img):
    where=filedialog.asksaveasfilename(filetypes=(('JPEG Files','*.jpg'),('PNG Files','*.png'),('All Files','*.*')),defaultextension=file_path_c[-4:])
    cartoon_img.save(where)

    

def show_save_button(file_path_c,cartoon_img,new):
    save_b=Button(new,text='Save to computer', command=lambda: save_cartoon(file_path_c,cartoon_img),padx=10,pady=5)
    save_b.place(relx=0.69,rely=0.86)
    
def convert(file_path_c,new):
    cartoon=make_cartoon(file_path_c)
    cartoon=cv2.cvtColor(cartoon,cv2.COLOR_BGR2RGB)
    cartoon_img=Image.fromarray(cartoon)
    cartoon_img.thumbnail(((new.winfo_width()/1.8),(new.winfo_height()/1.8)))
    im=ImageTk.PhotoImage(cartoon_img)
    label=Label(new,image=im)
    label.image=im
    label.pack(side="right",expand='yes')
    show_save_button(file_path_c,cartoon_img,new)

def show_convert_button(file_path_c,new):
    convert_b=Button(new,text="Cartoonify me",command=lambda: convert(file_path_c,new),padx=10,pady=5)
    convert_b.place(relx=0.79,rely=0.46)



def upload_image():
    new=Toplevel()
    new.geometry('1000x600')
    new.title('New Project')
    new.configure(background='white')
    
    file_path_c=filedialog.askopenfilename()
    uploaded=Image.open(file_path_c)
    uploaded.thumbnail(((new.winfo_width()/2.25),(new.winfo_height()/2.25)))
    im=ImageTk.PhotoImage(uploaded)

    label=Label(new,image=im)
    label.image=im
    label.pack(side="left", expand='yes')
    show_convert_button(file_path_c, new)
    
    



upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#adadee', foreground='white',font=('arial',10,'bold'))
upload.place(relx=0.44,rely=0.86)

top.mainloop()
