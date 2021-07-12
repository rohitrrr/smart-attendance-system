from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        img=Image.open(r"E:\python\system\image\upperbanner.jpg")
        img=img.resize((400,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        img = Image.open(r"E:\python\system\image\2.jpg")
        img = img.resize((400, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img)

        img = Image.open(r"E:\python\system\image\3.jpg")
        img = img.resize((400, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img)




        F_lbl=Label(self.root,image=self.photoimg)
        F_lbl.place(x=0,y=0,width=473,height=130)

        S_lbl = Label(self.root, image=self.photoimg2)
        S_lbl.place(x=500, y=0, width=500, height=130)

        T_lbl = Label(self.root, image=self.photoimg3)
        T_lbl.place(x=1000, y=0, width=550, height=130)

        ##backgorund image
        img4 = Image.open(r"E:\python\system\image\bg.jpg")
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.bgimage = ImageTk.PhotoImage(img4)

        BG_lbl = Label(self.root, image=self.bgimage)
        BG_lbl.place(x=0, y=130, width=1530, height=710)


        title_lbl=Label(BG_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="blue",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #button section
        #student
        stu_img = Image.open(r"E:\python\system\image\download.jpg")
        stu_img = stu_img.resize((220, 220), Image.ANTIALIAS)
        self.stuimage = ImageTk.PhotoImage(stu_img)

        B1 = Button(BG_lbl,image=self.stuimage,cursor="hand2")
        B1.place(x=200, y=75, width=220, height=220)

        B1o = Button(BG_lbl,text="STUDENT DETAILS",font=("times new roman",12,"bold"),bg="blue",fg="red",cursor="hand2")
        B1o.place(x=200, y=275, width=220, height=40)



        #button2
        stu_img2 = Image.open(r"E:\python\system\image\2.jpg")
        stu_img2 = stu_img2.resize((220, 220), Image.ANTIALIAS)
        self.stuimage2= ImageTk.PhotoImage(stu_img2)

        B1 = Button(BG_lbl,image=self.stuimage2,cursor="hand2")
        B1.place(x=450, y=75, width=220, height=220)

        B1o = Button(BG_lbl,text="FACE RECOGITION ",font=("times new roman",12,"bold"),bg="blue",fg="red",cursor="hand2")
        B1o.place(x=450, y=275, width=220, height=40)

        #button3
        stu_img3 = Image.open(r"E:\python\system\image\att.jpg")
        stu_img3 = stu_img3.resize((220, 220), Image.ANTIALIAS)
        self.stuimage3 = ImageTk.PhotoImage(stu_img3)

        B1 = Button(BG_lbl,image=self.stuimage3,cursor="hand2")
        B1.place(x=700, y=75, width=220, height=220)

        B1o = Button(BG_lbl,text="ATTENDACNE",font=("times new roman",12,"bold"),bg="blue",fg="red",cursor="hand2")
        B1o.place(x=700, y=275, width=220, height=40)

        #button4
        stu_img4 = Image.open(r"E:\python\system\image\help.jpg")
        stu_img4 = stu_img4.resize((220, 220), Image.ANTIALIAS)
        self.stuimage4 = ImageTk.PhotoImage(stu_img4)

        B1 = Button(BG_lbl,image=self.stuimage4,cursor="hand2")
        B1.place(x=950, y=75, width=220, height=220)

        B1o = Button(BG_lbl,text="HELP",font=("times new roman",12,"bold"),bg="blue",fg="red",cursor="hand2")
        B1o.place(x=950, y=275, width=220, height=40)
        

        #button5
        stu_img5 = Image.open(r"E:\python\system\image\traion.jpg")
        stu_img5 = stu_img5.resize((220, 220), Image.ANTIALIAS)
        self.stuimage5 = ImageTk.PhotoImage(stu_img5)

        B1 = Button(BG_lbl,image=self.stuimage5,cursor="hand2")
        B1.place(x=200, y=330, width=220, height=220)

        B1o = Button(BG_lbl,text="TRAINED DATA",font=("times new roman",12,"bold"),bg="blue",fg="red",cursor="hand2")
        B1o.place(x=200, y=510, width=220, height=40)
         
        #butoon6
        stu_img6 = Image.open(r"E:\python\system\image\photo.jpg")
        stu_img6 = stu_img6.resize((220, 220), Image.ANTIALIAS)
        self.stuimage6 = ImageTk.PhotoImage(stu_img6)

        B1 = Button(BG_lbl,image=self.stuimage6,cursor="hand2")
        B1.place(x=450, y=330, width=220, height=220)

        B1o = Button(BG_lbl,text="PHOTOS",font=("times new roman",12,"bold"),bg="blue",fg="red",cursor="hand2")
        B1o.place(x=450, y=510, width=220, height=40)

        #button7
        stu_img7 = Image.open(r"E:\python\system\image\dev.png")
        stu_img7 = stu_img7.resize((220, 220), Image.ANTIALIAS)
        self.stuimage7 = ImageTk.PhotoImage(stu_img7)

        B1 = Button(BG_lbl,image=self.stuimage7,cursor="hand2")
        B1.place(x=700, y=330, width=220, height=220)

        B1o = Button(BG_lbl,text="DEVLOPER",font=("times new roman",12,"bold"),bg="blue",fg="red",cursor="hand2")
        B1o.place(x=700, y=510, width=220, height=40)

        #button 8
        stu_img8 = Image.open(r"E:\python\system\image\exit.jpg")
        stu_img8 = stu_img8.resize((220, 220), Image.ANTIALIAS)
        self.stuimage8 = ImageTk.PhotoImage(stu_img8)

        B1 = Button(BG_lbl,image=self.stuimage8,cursor="hand2")
        B1.place(x=950, y=330, width=220, height=220)

        B1o = Button(BG_lbl,text="EXIT",font=("times new roman",12,"bold"),bg="blue",fg="red",cursor="hand2")
        B1o.place(x=950, y=510, width=220, height=40)

  







if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()
