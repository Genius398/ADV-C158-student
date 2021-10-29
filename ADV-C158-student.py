 from tkinter import *
 root=Tk()
 root.title("Addition")
 root.geometry("600x400")
 inputBox = Entry(root)
 inputBox.pack()
 
 def addition():
     number = 5
     getInput = inputBox.get()
     
     try:
         print(number + getInput)
         
     except(TypeError):
          messagebox.showinfo("Error", "Cant add two different data types")
          
 button = Button(root, text="Add", command = addition)
 button.pack()
     
 root.mainloop()