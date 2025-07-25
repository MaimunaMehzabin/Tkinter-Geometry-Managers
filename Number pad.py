from tkinter import *

root = Tk()
root.title('Number Pad')
root.geometry('220x300')

nums = [
    [7,8,9],
    [4,5,6],
    [1,2,3],
    ['#',0,'*']
]

for i in range(4):
    root.columnconfigure(i,weight=1,minsize=75)
    root.rowconfigure(i,weight=1,minsize=50)
    
for i in range(4):
    for j in range(3):
        
        frame = Frame(master=root, relief=RAISED, borderwidth=7, bg="#d0efff")
        frame.grid(row=i, column=j, sticky="nsew")
        
        lable = Label(master=frame, text=nums[i][j], bg="#d0efff", font=("Times New Roman", 18))
        lable.pack(expand=True, fill="both", padx=5, pady=5)
        
root.mainloop()