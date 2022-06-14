import tkinter
from tkinter import*
import random
questions = [
    "How many Keywords are there in C programming language ?",
    "Which of the following functions takes A console Input in Python?",
    "which of the following is the Capital of India?",
    "Which of the Following is must to Execute a Python Code?",
    "The Taj Mahal is located in?",
    "The append Method adds value to the list at the.. ?",
    "Which of the following is not a costal city of the India ?",
    "Which of the following is executed in browser(client side)?",
    "Which of the following Keyword is used to create a function in Python ?",
    "To Declare a Global variable in python we use the keyword ?",
]

answers_choice =[
    ["23","32","33","43",],
    ["get()","input()","gets()","scan()",],
    ["Mumbai","Delhi","Chennai","Lucknow",],
    ["Turbo C","Py Interpreter","Notepad","IDE",],
    ["Patna","Delhi","Banaras","Agra",],
    ["custom location","end","center","begnining",],
    ["Bengaluru","Kochin","Mumbai","Vishakhapatnam",],
    ["perl","css","python","java",],
    ["function","void","function","def",],
    ["all","var","let","global",],
]

answers = [1,1,1,1,3,1,0,1,3,3]

user_answer =[]


indexes =[]
def gen():
    global indexes
    while(len(indexes) < 10):
        x=random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    print(indexes)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    Labelimage=Label(
        root,
        background="#FFFF00",
    )
    Labelimage.pack(pady=(50,30))
    Labelresulttext=Label(
        root,
        font=("consolas",20),
        background="#FFFF00",
    )
    Labelresulttext.pack()
    if score >= 50:
        img = PhotoImage(file="great.png")
        Labelimage.configure(image=img)
        Labelimage.image=img
        Labelresulttext.configure(text="You Are Excellent!!!!!!") 
    elif score >=35 and score < 50:
        img = PhotoImage(file="ok.png")
        Labelimage.configure(image=img)
        Labelimage.image=img
        Labelresulttext.configure(text="You Can Do Better!!!!!!") 
    else:
        img = PhotoImage(file="Bad.png")
        Labelimage.configure(image=img)
        Labelimage.image=img
        Labelresulttext.configure(text=" Better Luck Next Time!!!!!!") 


def calc():
    global indexes,user_answer,answers
    x=0
    score=0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score=score + 10
        x += 1
    print(score)
    showresult(score)


ques =1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x=radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 10:
            lblQuestion.config(text =questions[indexes[ques]])
            r1['text']=answers_choice[indexes[ques]][0]
            r2['text']=answers_choice[indexes[ques]][1]
            r3['text']=answers_choice[indexes[ques]][2]
            r4['text']=answers_choice[indexes[ques]][3]
            ques += 1

    else:
        print(indexes)
        print(user_answer)
        calc()
    

def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion=Label(
        root,
        text=questions[indexes[0]],
        font=("consolas",16),
        width=500,
        justify="center",
        wraplength=400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)

    r1= Radiobutton(
        root,
        text =answers_choice[indexes[0]][0] ,
        font =("Times",12),
        value=0,
        variable=radiovar,
        command=selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2= Radiobutton(
        root,
        text=answers_choice[indexes[0]][1] ,
        font =("Times",12),
        value=1,
        variable=radiovar,
        command=selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3= Radiobutton(
        root,
        text =answers_choice[indexes[0]][2] ,
        font =("Times",12),
        value=2,
        variable=radiovar,
        command=selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4= Radiobutton(
        root,
        text =answers_choice[indexes[0]][3] ,
        font =("Times",12),
        value=3,
        variable=radiovar,
        command=selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    Labelimage.destroy()
    Labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()

 
root = tkinter.Tk()
root.title("QuizStar")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)


img1 = PhotoImage(file="transparentGradHat.png")

Labelimage = Label(
    root,
    image = img1,
    background="#ffffff"
)
Labelimage.pack(pady=(40,0))

Labeltext=Label(
    root,
    text="Quizstar",
    font=("Comic sans MS",24,'bold'),
    background="#ffffff",

)
Labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image = img2,
    relief=FLAT,
    border=0,
    command= startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text="Read The Rules And\nClick Start Once You Are Ready",
    background="#ffffff",
    font=("Consolas",14),
    justify="center",
    )
lblInstruction.pack(pady=(10,100))

lblRules = Label(
    root,
    text="This Quiz contains 10 questions\n Choose right one\nOnce you select radio button that will be a final choice\nhence think before you select",
    background="#000000",
    width=100,
    font=("Times",14),
    foreground="#FACA2F",
)
lblRules.pack()
root.mainloop()