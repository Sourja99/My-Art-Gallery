import tkinter as tk
from tkinter import filedialog
from tkinter import *
from backened_algorithm import add_color
from cartoonizer import make_cartoon
from style_transfer import transfer_style
from PIL import ImageTk, Image
import cv2
import os



top=tk.Tk()
top.geometry('1000x700')
top.title('Cp2 ART GALLERY')
top.iconbitmap('.\\images\\icons\\gallery_hdpi.ico')
top.configure(background='blue')


#####################################################colorizer###########################################

def save_colorized(file_path,colorized_img):
    try:
        where=filedialog.asksaveasfilename(filetypes=(('JPEG Files','*.jpg'),('PNG Files','*.png'),('All Files','*.*')),defaultextension=file_path[-4:])
        colorized_img.save(where)
    except:
        pass

def show_save_button(file_path,colorized_img, new):
    save_b=Button(new,text='Save to computer', command=lambda: save_colorized(file_path,colorized_img),padx=10,pady=5)
    save_b.place(relx=0.69,rely=0.86)

########################################################filter###########################

def save_colorized_style(file_path_s,styled_img):
    try:
        where=filedialog.asksaveasfilename(filetypes=(('JPEG Files','*.jpg'),('PNG Files','*.png'),('All Files','*.*')),defaultextension=file_path[-4:])
        styled_img.save(where)
    except:
        pass

def show_save_button_style(file_path_s,styled_img, new_1):
    save_b=Button(new_1,text='Save to computer', command=lambda: save_colorized_style(file_path_s,styled_img),padx=10,pady=5)
    save_b.place(relx=0.80,rely=0.51)


#######################################################Cartoonify ##############################################
def save_cartoon(file_path_c,cartoon_img):
    where=filedialog.asksaveasfilename(filetypes=(('JPEG Files','*.jpg'),('PNG Files','*.png'),('All Files','*.*')),defaultextension=file_path_c[-4:])
    cartoon_img.save(where)

    

def show_save_button_cartoon(file_path_c,cartoon_img,new):
    save_b=Button(new,text='Save to computer', command=lambda: save_cartoon(file_path_c,cartoon_img),padx=10,pady=5)
    save_b.place(relx=0.69,rely=0.86)
    
#################################################filter pic obtain######################################################

def convert_filter(file_path_s,fil,new_1):
    styled_img=transfer_style(file_path_s,fil)
    cv2.imshow('filtered image',styled_img)
    
    show_save_button_style(file_path_s,styled_img, new_1)
    



def pick_filter(file_path_s,new_1):
    filter_text=Label(new_1,text='Pick a filter to apply')
    filter_text.configure(background='yellow', foreground='#05232c', font='arial 22 bold underline')
    filter_text.place(x=30,y=30)
    filters=os.listdir('.\\images\\filters')
    i=10
    for fil in range(len(filters)):
        im=Image.open(f'.\\images\\filters\\{filters[fil]}')
        im.thumbnail(((new_1.winfo_width()/8),(new_1.winfo_height()/8)))
        im=ImageTk.PhotoImage(im)
        label=Label(new_1,image=im,cursor="hand2")
        label.image=im
        label.place(x=i,y=530); i+=new_1.winfo_width()/6.6
        label.bind("<1>",lambda e,f=fil:convert_filter(file_path_s,f'.\\images\\filters\\{filters[f]}',new_1))
    

    
####################################################  Convert color ##########################################################################
   
   
def convert_color(file_path, new):
    colorized_img=add_color(file_path)
    colorized_img=cv2.cvtColor(colorized_img,cv2.COLOR_BGR2RGB)
    colorized_img=Image.fromarray(colorized_img)
    colorized_img.thumbnail(((new.winfo_width()/1.8),(new.winfo_height()/1.8)))
    im=ImageTk.PhotoImage(colorized_img)
    label=Label(new,image=im)
    label.image=im
    label.pack(side="right",expand='yes')
    show_save_button(file_path, colorized_img, new)
 
def show_convert_button(file_path, new):
    convert_b=Button(new,text="Colorize",command=lambda: convert_color(file_path, new),padx=10,pady=5)
    convert_b.place(relx=0.79,rely=0.46)


###############################################################
def convert(file_path_c,new):
    cartoon=make_cartoon(file_path_c)
    cartoon=cv2.cvtColor(cartoon,cv2.COLOR_BGR2RGB)
    cartoon_img=Image.fromarray(cartoon)
    cartoon_img.thumbnail(((new.winfo_width()/1.8),(new.winfo_height()/1.8)))
    im=ImageTk.PhotoImage(cartoon_img)
    label=Label(new,image=im)
    label.image=im
    label.pack(side="right",expand='yes')
    show_save_button_cartoon(file_path_c,cartoon_img,new)

def show_convert_button_cartoon(file_path_c,new):
    convert_b=Button(new,text="Cartoonify me",command=lambda: convert(file_path_c,new),padx=10,pady=5)
    convert_b.place(relx=0.79,rely=0.46)


#####################################################cartoon image #####################3################################

def upload_image_cartoon():
    new=Toplevel()
    new.geometry('1000x600')
    new.title('Cartoon Project')
    new.configure(background='blue')
    
    file_path_c=filedialog.askopenfilename()
    uploaded=Image.open(file_path_c)
    uploaded.thumbnail(((new.winfo_width()/2),(new.winfo_height()/2)))
    im=ImageTk.PhotoImage(uploaded)

    _text=Label(new,text='Workspace : ')
    _text.configure(background='yellow', foreground='#05232c', font='arial 40 underline')
    _text.place(x=30,y=30)

    label=Label(new,image=im)
    label.image=im
    label.pack(side="left", expand='yes')
    show_convert_button_cartoon(file_path_c, new)




    
################################################################ colourize image #################3#############


def new_image(im,file_path):
    new=Toplevel()
    new.geometry('1000x600')
    new.title('Colorize Project')
     
    image_text=Label(new,text='Workspace : ')
    image_text.configure(background='yellow', foreground='#05232c', font='arial 40 underline')
    image_text.place(x=30,y=30)
    
    new.iconbitmap('.\\images\\icons\\gallery_hdpi.ico')
    new.configure(background='blue')
    label=Label(new,image=im)
    label.image=im
    label.pack(side="left", expand='yes')
    show_convert_button(file_path, new)
    
   ######### ############################################     filter image ####################################
def new_image_style(im,file_path_s):
    new_1=Toplevel()
    new_1.geometry('1000x600')
    new_1.title('Filter Project')
    new_1.iconbitmap('.\\images\\icons\\mag_icon.ico')
    new_1.configure(background='yellow')
    label=Label(new_1,image=im)
    label.image=im
    label.pack(side="left", expand='yes')
    pick_filter(file_path_s, new_1)
    

   
   
   ####################################################### colorize upload button ##################
    
def colorize_1():
    new = Toplevel()
    new.geometry('1000x600')
    new.title('New Project')
    new.iconbitmap('.\\images\\icons\\gallery_hdpi.ico')
    #new.configure(background='Yellow')
    
    
    c_img=Image.open('.\\images\\others\\color.jpeg')
    c_img=ImageTk.PhotoImage(c_img)
    c_label=Label(new,image=c_img)
    c_label.image=c_img
    c_label.pack(side='top',expand='yes')
    

    
    
    
    upload=Button(new,text="Upload an image",command=upload_image,padx=10,pady=5)
    upload.configure(background='#e6d309',foreground='black',font=('arial',12,'bold'))
    upload.place(relx=0.22,rely=0.89)
    
    
    sample=Button(new,text="Try a sample image",command=upload_sample,padx=10,pady=5)
    sample.configure(background='#eb1321',foreground='white',font=('arial',10,'bold'))
    sample.place(relx=0.63,rely=0.89)
   ###########################################################
   
def filter_1():
    new = Toplevel()
    new.geometry('1000x600')
    new.title('Filter Project')
    new.iconbitmap('.\\images\\icons\\gallery_hdpi.ico')
    new.configure(background='Yellow')
    
    
    s_img=Image.open('.\\images\\others\\Style.jfif')
    s_img=ImageTk.PhotoImage(s_img)
    s_label=Label(new,image=s_img)
    s_label.image=s_img
    s_label.pack(side='top',expand='yes')
    
    
    upload=Button(new,text="Upload an image",command=upload_image_style,padx=10,pady=5)
    upload.configure(background='#e6d309',foreground='black',font=('arial',12,'bold'))
    upload.place(relx=0.41,rely=0.89)
    
    
    
    
####################################    
def cartoon_1():
    new=Toplevel()
    new.geometry('815x430')
    new.title('Cartoon Project')
    new.configure(background='blue')
    
    ca_img=Image.open('.\\images\\others\\cartoon.jpg')
    ca_img=ImageTk.PhotoImage(ca_img)
    ca_label=Label(new,image=ca_img)
    ca_label.image=ca_img
    ca_label.pack(side='top',expand='yes')
    
    upload=Button(new,text="Upload an image",command=upload_image_cartoon,padx=10,pady=5)
    upload.configure(background='#adadee', foreground='black',font=('arial',12,'bold'))
    upload.place(relx=0.42,rely=0.73)





##############################################

def upload_image(file_path=None,sample_gallery=None):
    if file_path==None: file_path=filedialog.askopenfilename()
    if sample_gallery!=None: sample_gallery.destroy()
    try:
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        new_image(im,file_path)
    except:
        pass
    

def upload_sample():
    sample_gallery=Toplevel()
    sample_gallery.geometry('3000x800')
    sample_gallery.title('Sample Images')
    sample_gallery.iconbitmap('.\\images\\icons\\gallery_hdpi.ico')
    sample_gallery.configure(background='#08052c')
    sample_text=Label(sample_gallery,text='Colorize a Sample Image')
    sample_text.configure(background='#08052c', foreground='Yellow', font='arial 30')
    sample_text.pack(side='top',pady=85)
    samples=os.listdir('.\\images\\samples')
    for sample in range(len(samples)):
        im=Image.open(f'.\\images\\samples\\{samples[sample]}')
        im.thumbnail(((sample_gallery.winfo_width()/6),(sample_gallery.winfo_height()/6)))
        im=ImageTk.PhotoImage(im)
        label=Label(sample_gallery,image=im,cursor="hand2")
        label.image=im
        label.pack(side='left', expand='yes')
        label.bind("<1>",lambda e,s=sample:upload_image(f'.\\images\\samples\\{samples[s]}',sample_gallery))

############################################################08052c#####################################################

def upload_image_style():
    file_path_s=filedialog.askopenfilename()
    try:
        uploaded=Image.open(file_path_s)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        new_image_style(im,file_path_s)
    except:
        pass
    
    
##########################################################################################################




#########################################Front page ##############################################

vc_img=Image.open('.\\images\\others\\My Art.jpg')
vc_img=ImageTk.PhotoImage(vc_img)
vc_label=Label(top,image=vc_img)
vc_label.image=vc_img
vc_label.pack(side='top',expand='yes')

           

###
colorizer=Button(top,text="Colorizer",command=colorize_1,padx=10,pady=5)
colorizer.configure(background='#e6d309',foreground='black',font=('arial',12,'bold'))
colorizer.place(relx=0.15,rely=0.89)

###

fil_button=Button(top,text="Filter",command=filter_1,padx=10,pady=5)
fil_button.configure(background='#e6d309',foreground='black',font=('arial',12,'bold'))
fil_button.place(relx=0.47,rely=0.89)

###

cartoon=Button(top,text="Cartoonify",command=cartoon_1,padx=10,pady=5)
cartoon.configure(background='#e6d309',foreground='black',font=('arial',12,'bold'))
cartoon.place(relx=0.75,rely=0.89)




top.mainloop()
