import urllib.request
import re
from tkinter import *
# from projectFile import check
def show():
    if(re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'),rm.get())):
        res = 0
        try:
            urllib.request.urlopen(ws.get())
        except:
            res = 1
        if(res==1):
            op.config(text='Sorry the website data can\' be accessed')
            ws.delete(0,END)
            rd.delete(0,END)
            rm.delete(0,END)
        else:
            op.config(text='Added Successfully.........')
    else:
        ws.delete(0,END)
        rd.delete(0,END)
        rm.delete(0,END)
        op.config(text='Something went wrong.......')
root = Tk()
root.title('Application Page...')
Label(root,text="ContentNotifier",fg="Orange",font=("Helvetia",15,"bold","italic"),height=10).grid(row=-0,column=14)
Label(root,text="\tThis tool will inform you through the gamil regarding your required data ",font=20).grid(row=1,column=15)
Label(root,text="based on the paramaeters you provided here.",font=20).grid(row=2,column=15)
Label(root,text="ADD YOURSELF NOW .....",font=20).grid(row=3,column=15)
Label(root,text="WELCOME ",width=30,font=35).grid(row=1,column=0)
Label(root,text="To the content notifier tool.... :",font=35).grid(row=2,column=0)

l=Label(root,text='Web Source : ' , fg='Indigo' ,font=40)
l1=Label(root,text='Required Data : ' , fg='Indigo' ,font=40 )
l2=Label(root,text='Receipent Mail: ' , fg='Indigo' ,font=40 )

ws=Entry(root)
rd=Entry(root)
rm=Entry(root)

l.grid(row=1,column=10)
l1.grid(row=2,column=10)
l2.grid(row=3,column=10)

ws.grid(row=1,column=13)
rd.grid(row=2,column=13)
rm.grid(row=3,column=13)

op=Label(root)
op.grid(row=6,column=13)
res=Button(root,text="SUBMIT",command=show, fg='Magenta',bg='AliceBlue',width=10,height=2,font=12)
res.grid(row=7,column=13)

root.mainloop()



