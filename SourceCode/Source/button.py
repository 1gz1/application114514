from customtkinter import *
from os import system

def cmd():
    system("start cmd")

def calc():
    system("start calc")

def notepad():
    system("start notepad")

def mspaint():
    system("start mspaint")

def explorer():
    system("start explorer")

def taskmgr():
    system("start taskmgr")

def regedit():
    system("start regedit")

def vscode():
    try:
        system("start code")
    except:
        err = CTk()
        err.title("错误")
        err.geometry("200x100")
        errmsg = CTkLabel(err, text="未安装VSCode")
        errmsg.pack()
        err.mainloop()

def chrome():
    try:
        system("start chrome")
    except:
        err = CTk()
        err.title("错误")
        err.geometry("200x100")
        errmsg = CTkLabel(err, text="未安装Chrome")
        errmsg.pack()
        err.mainloop()

def edge():
    try:
        system("start msedge")
    except:
        err = CTk()
        err.title("错误")
        err.geometry("200x100")
        errmsg = CTkLabel(err, text="未安装Edge")
        errmsg.pack()
        err.mainloop()

def bilibili():
    try:
        system("start https://www.bilibili.com/")
    except:
        err = CTk()
        err.title("错误")
        err.geometry("200x100")
        errmsg = CTkLabel(err, text="你是不是卸载浏览器了？")
        errmsg.pack()
        err.mainloop()
        
def pip():
    try:
        pipt = CTk()
        pipt.title("pip工具")
        pipt.geometry("600x500")
        def install_pygame():
            system("pip install pygame")
        def install_pandas():
            system("pip install pandas")
        def install_numpy():
            system("pip install numpy")
        def install_matplotlib():
            system("pip install matplotlib")
        def install_pyinstaller():
            system("pip install pyinstaller")
        pg = CTkButton(pipt, text="安装pygame", command=install_pygame)
        pg.pack()
        pd = CTkButton(pipt, text="安装pandas", command=install_pandas)
        pd.pack()
        np = CTkButton(pipt, text="安装numpy", command=install_numpy)
        np.pack()
        mp = CTkButton(pipt, text="安装matplotlib", command=install_matplotlib)
        mp.pack()
        pi = CTkButton(pip, text="安装pyinstaller", command=install_pyinstaller)
        pi.pack()
        pipt.mainloop()
    except:
        err = CTk()
        err.title("错误")
        err.geometry("200x100")
        errmsg = CTkLabel(err, text="pip未安装或未配置环境变量")
        errmsg.pack()
        err.mainloop()