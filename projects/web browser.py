import webbrowser
import tkinter as tk

root=tk.Tk()
root.geometry("400x150")
root.title("web browser")


def fb():
    webbrowser.open_new("www.facebook.com")
def yt():
    webbrowser.open_new("www.youtube.com")
def ig():
    webbrowser.open_new("www.instagram.com")
def tw():
    webbrowser.open_new("www.twitter.com")

def search():
    word=x.get()
    search="https://www.google.com/search?q="+word
    webbrowser.open_new(search)



x=tk.StringVar()
b1=tk.Button(root,text="facebook",fg="white",bg="#3b5998",command=fb)
b2=tk.Button(root,text="youtube",fg="white",bg="#ff0000",command=yt)
b3=tk.Button(root,text="instagram",fg="white",bg="#c13584",command=ig)
b4=tk.Button(root,text="twitter",fg="white",bg="#00acee",command=tw)


b1.place(x=10,y=70,width=80,height=30)
b2.place(x=100,y=70,width=80,height=30)
b3.place(x=190,y=70,width=80,height=30)
b4.place(x=280,y=70,width=80,height=30)


b6=tk.Button(root,text="Serach",fg="white",bg="#202020",command=search)
b6.place(x=320,y=10,width=70,height=50)
e1=tk.Entry(root,textvariable=x)
e1.place(x=10,y=10,width=300,height=50)


root.mainloop()
#url="www.youtube.com"
#word="paras"
#search="https://www.google.com/search?q="+
#webbrowser.open_new(search)
