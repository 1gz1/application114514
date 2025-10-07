from customtkinter import *
from Source.window import *
from Source.progs import *
from Source.const import *

def sign():
    global userName, passWord
    rg = CTk()
    rg.geometry('500x300')
    rg.title('注册信息(关掉窗口进入登录界面)')
    set_default_color_theme('dark-blue')
    CTkLabel(rg, text='用户名').pack()
    user = CTkEntry(rg)            #用户名输入框
    user.pack()
    CTkLabel(rg, text='密码').pack()
    password = CTkEntry(rg)
    password.pack()
    def rigister():
        global userName, passWord
        Sure = CTk()
        Sure.geometry('300x200')
        Sure.title('确认信息')
        u = CTkLabel(Sure, text="用户名:"+user.get())
        u.pack()
        p = CTkLabel(Sure, text="密码:"+password.get())
        p.pack()
        userName = user.get()
        passWord = password.get()
        CTkButton(Sure, text='确认', command = Sure.destroy).pack()
        Sure.mainloop()
    CTkButton(rg, text='注册', command = rigister).pack()
    rg.mainloop()

def programlog():
    global userName, passWord
    root = CTk()
    root.geometry("500x350")
    root.title("Constant")
    lblname = CTkLabel(root, text="用户名：", font=("微软雅黑", 20))
    lblname.pack()
    nme = CTkEntry(root, font=("微软雅黑", 20))
    nme.pack()
    lblpswd = CTkLabel(root, text="密码：", font=("微软雅黑", 20))
    lblpswd.pack()
    passw = CTkEntry(root, font=("微软雅黑", 20), show="*")
    passw.pack()
    def login():
        if nme.get() == userName and passw.get() == passWord:
            tool()
        else:
            logerror = CTk()
            logerror.geometry("300x100")
            logerror.title("错误")
            logerrorlbl = CTkLabel(logerror, text="用户名或密码错误", font=("微软雅黑", 20))
            logerrorlbl.pack()
            logerrorbtn = CTkButton(logerror, text="确定", command=logerror.destroy)
            logerrorbtn.pack()
            logerror.mainloop()
    btn = CTkButton(root, text="登录", font=("微软雅黑", 20), command=login)
    btn.pack()
    root.mainloop()

progress()
sign()