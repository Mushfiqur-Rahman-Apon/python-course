from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        # 1st
        img = Image.open(r"college_images\image1.jpg")
        img = img.resize((510, 160), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        self.btn_1 = Button(self.root, image=self.photoimg, cursor="hand2")
        self.btn_1.place(x=0, y=0, width=540, height=160)


        # 2st
        img_2 = Image.open(r"college_images\image2.jpg")
        img_2 = img.resize((510, 160), Image.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        self.btn_2 = Button(self.root, image=self.photoimg_2, cursor="hand2")
        self.btn_2.place(x=540, y=0, width=540, height=160)

        # 1st
        img_3 = Image.open(r"college_images\images3.jpg")
        img_3 = img_3.resize((510, 160), Image.LANCZOS)
        self.photoimg_3 = ImageTk.PhotoImage(img)

        self.btn_1 = Button(self.root, image=self.photoimg, cursor="hand2")
        self.btn_1.place(x=1000, y=0, width=540, height=160)



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
    BD
Skip navigation
Sign in

  
    
    
  

  
    
    
    
  

  
    
      
      
    
    
      
      
    
  
Deewane (