from tkinter import *
class calc:
    def __init__(self):
        window=Tk()
        self.num1=str()
        frame1=Frame(window)
        frame1.pack()

        frame2=Frame(window)
        frame2.pack()

        self.lbl=Label(frame1, text='SCREEN', bg='green')
        self.lbl.grid(row=0, column=0, ipadx=3, columnspan=3)

        bt9=Button(frame2, text="9", command=self.nine)
        bt8=Button(frame2, text="8", command=self.eight)
        bt7=Button(frame2, text="7", command=self.seven)
        btdiv=Button(frame2, text="/", command=self.divide)

        bt6=Button(frame2, text="6", command=self.six)
        bt5=Button(frame2, text="5", command=self.five)
        bt4=Button(frame2, text="4", command=self.four)
        bttim=Button(frame2, text="*", command=self.times)

        bt3=Button(frame2, text="3", command=self.three)
        bt2=Button(frame2, text="2", command=self.two)
        bt1=Button(frame2, text="1", command=self.one)
        btmin=Button(frame2, text="-", command=self.minus)

        bt0=Button(frame2, text="0", command=self.zero)
        btdot=Button(frame2, text=".", command=self.dot)
        btequ=Button(frame2, text="=", command=self.equal)
        btadd=Button(frame2, text="+", command=self.add)
        btcle=Button(frame2, text="C", command=self.clear)
        btdel=Button(frame2, text="del", command=self.dele)

        bt9.grid(row=2,column=0)
        bt8.grid(row=2,column=1)
        bt7.grid(row=2,column=2)
        btdiv.grid(row=2,column=3)

        bt6.grid(row=3,column=0)
        bt5.grid(row=3,column=1)
        bt4.grid(row=3, column=2)
        bttim.grid(row=3, column=3)

        bt3.grid(row=4,column=0)
        bt2.grid(row=4,column=1)
        bt1.grid(row=4, column=2)
        btmin.grid(row=4, column=3)

        bt0.grid(row=5,column=0)
        btdot.grid(row=5,column=1)
        btequ.grid(row=5, column=2)
        btadd.grid(row=5, column=3)

        btcle.grid(row=6, column=0)
        btdel.grid(row=6, column=1)

        window.mainloop()

    def nine(self):
        self.num1=self.num1+'9'
        self.lbl['text']=self.num1
    def eight(self):
        self.num1=self.num1+'8'
        self.lbl['text']=self.num1
    def seven(self):
        self.num1=self.num1+'7'
        self.lbl['text']=self.num1
    def divide(self):
        self.num1=self.num1+'/'
        self.lbl['text']=self.num1
    def six(self):
        self.num1=self.num1+'6'
        self.lbl['text']=self.num1
    def five(self):
        self.num1=self.num1+'5'
        self.lbl['text']=self.num1
    def four(self):
        self.num1=self.num1+'4'
        self.lbl['text']=self.num1
    def times(self):
        self.num1=self.num1+'*'
        self.lbl['text']=self.num1
    def three(self):
        self.num1=self.num1+'3'
        self.lbl['text']=self.num1
    def two(self):
        self.num1=self.num1+'2'
        self.lbl['text']=self.num1
    def one(self):
        self.num1=self.num1+'1'
        self.lbl['text']=self.num1
    def minus(self):
        self.num1=self.num1+'-'
        self.lbl['text']=self.num1
    def zero(self):
        self.num1=self.num1+'0'
        self.lbl['text']=self.num1
    def dot(self):
        self.num1=self.num1+'.'
        self.lbl['text']=self.num1
    def equal(self):
        try:
            self.lbl['text']=(str(eval(f'{self.num1}')))
            self.num1=(str(eval(f'{self.num1}')))
        except :
            self.lbl['text']=('Invalid')
        
        #self.num1=""
    def add(self):
        self.num1=self.num1+'+'
        self.lbl['text']=self.num1

    def clear(self):
        self.num1=str()
        self.lbl['text']=self.num1

    def dele(self):
        self.num1=self.num1[0:-1]
        self.lbl['text']=self.num1
 
calc()

        
        