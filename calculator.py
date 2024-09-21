from tkinter import *       #Python, GUI Toolkit
root=Tk()           #instance of Tk() class and used as main/parent window


root.title("Calculator")
root.geometry("570x600")
root.resizable(False,False)
root.configure(bg="lavender")

equation=""
def clear():        #to clear the widget or labelresult variable
    global equation
    equation=""
    labelresult.configure(text=equation)

def show(value):        #to display operand and operators in the labelresult variable
    global equation
    equation+=value
    labelresult.configure(text=equation)

def calculate():     #to compute the result
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    labelresult.configure(text=result)


def backspace():        #to remove rightmost operator or operand from the widget
    global equation
    equation=equation[:-1]
    labelresult.configure(text=equation)




labelresult=Label(root,text="",width=40,height=7,font=("bold,50"),bg="#fff",fg="#4f0fbd")   # to display equation as result
labelresult.pack()  #adds widget to parent window


#adding buttons to the calculator
Button(root,text="C",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:clear()).place(x=10,y=170)
Button(root,text="<=",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:backspace()).place(x=143,y=170)
Button(root,text="/",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("/")).place(x=276,y=170)
Button(root,text="%",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("%")).place(x=409,y=170)

Button(root,text="9",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("9")).place(x=10,y=255)
Button(root,text="8",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("8")).place(x=143,y=255)
Button(root,text="7",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("7")).place(x=276,y=255)
Button(root,text="*",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("*")).place(x=409,y=255)

Button(root,text="6",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("6")).place(x=10,y=340)
Button(root,text="5",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("5")).place(x=143,y=340)
Button(root,text="4",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("4")).place(x=276,y=340)
Button(root,text="-",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("-")).place(x=409,y=340)

Button(root,text="3",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("3")).place(x=10,y=425)
Button(root,text="2",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("2")).place(x=143,y=425)
Button(root,text="1",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("1")).place(x=276,y=425)
Button(root,text="+",width=5,height=1,font=("blurry",29,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("+")).place(x=409,y=425)

Button(root,text="0",width=10,height=1,font=("blurry",31,"bold"),bg="white",fg="pink",bd=3,command=lambda:show("0")).place(x=10,y=510)
Button(root,text="=",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:calculate()).place(x=276,y=510)
Button(root,text=".",width=5,height=1,font=("blurry",30,"bold"),bg="white",fg="pink",bd=3,command=lambda:show(".")).place(x=409,y=510)


root.mainloop() #to start the tkinter loop and wait for user input to update the window