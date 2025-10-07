from customtkinter import *
from sys import *
import pygame
from Source.button import *

#导入模块

pygame.init()
pygame.mixer.init()

#-------------------------定义打开工具窗口的函数----------------------------#
def pygamePlayAudio():
    play = CTk()
    play.title("播放器")
    play.geometry("500x300")
    textAudio = CTkLabel(play, text="请输入音频文件路径")
    textAudio.grid(row=0, column=0)
    audioEntry = CTkEntry(play, font=("微软雅黑", 20))
    audioEntry.grid(row=0, column=1)
    def playMusic():
        audio = pygame.mixer.Sound(audioEntry.get())
        audio.play()
    btn = CTkButton(play, text="播放", command=playMusic)
    btn.grid(row=1, column=1)
    play.mainloop()
def tool(): #工具箱使用按钮打开程序
    main = CTk()
    main.title("工具箱")
    main.geometry("1000x600")
    hello = CTkLabel(main, text="欢迎使用某不知名工具箱", font=("微软雅黑", 20))
    hello.grid(row=0, column=1)

    ety = CTkEntry(main, font=("微软雅黑", 20)) #文本框自定义打开程序
    ety.grid(row=1, column=1)
    def sysEntryGet():
        system("start "+ety.get())  #获取文本框内容并拼接
    btnTrue = CTkButton(main, text="打开", 
                    command=sysEntryGet)    #打开按钮
    btnTrue.grid(row=1, column=2)
    btncmd = CTkButton(main, text="命令提示符", command=cmd)
    btncmd.grid(row=2, column=2)
    btncalc = CTkButton(main, text="计算器", command=calc)
    btncalc.grid(row=2, column=6)
    btnnotepad = CTkButton(main, text="记事本", command=notepad)
    btnnotepad.grid(row=3, column=2)
    btnmspaint = CTkButton(main, text="画图",command=mspaint)
    btnmspaint.grid(row=3, column=6)
    btnexplorer = CTkButton(main, text="文件资源管理器", command=explorer)
    btnexplorer.grid(row=4, column=2)
    btntaskmgr = CTkButton(main, text="任务管理器",  command=taskmgr)
    btntaskmgr.grid(row=4, column=6)
    btnregedit = CTkButton(main, text="注册表编辑器",  command=regedit)
    btnregedit.grid(row=5, column=2)
    btncode = CTkButton(main, text="VSCode", command=vscode)
    btncode.grid(row=5, column=6)
    btnchrome = CTkButton(main, text="Chrome", command=chrome)
    btnchrome.grid(row=6, column=2)
    btnedge = CTkButton(main, text="Edge", command=edge)
    btnedge.grid(row=6, column=6)
    btnbilibili = CTkButton(main, text="哔哩哔哩", command=bilibili)
    btnbilibili.grid(row=7, column=2)
    btnPlayAudio = CTkButton(main, text="播放音频", command=pygamePlayAudio)
    btnPlayAudio.grid(row=7, column=6)
    btnPip = CTkButton(main, text="pip安装工具", command=pip)
    btnPip.grid(row=8, column=2)

    btnexit = CTkButton(main, text="退出", command=exit)
    btnexit.grid(row=9, column=3)
    main.mainloop()
