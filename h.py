from tkinter import * 
import tkinter as tk
from hentai import Hentai, Format
import os 
import shutil
import requests
import msvcrt
import shlex, subprocess
import time


class Windown():
    body = Tk()
    size = '400x150'
    color ='#161616'
    canvas = tk.Canvas(body)
    entry = tk.Entry(canvas)
    codi = entry.get()
    button = tk.Button(canvas)
    ico = 'nhentai.ico'
    value = 3

    def check_file(self):
        if os.path.isdir('H7u7H') == False:
            os.makedirs('H7u7H')
    def params_body(self):
        self.body.geometry(self.size)
        self.body.title("Nhentai App")
        self.body.resizable(False, False)
        self.body.iconbitmap(self.ico)
        self.body.config(bg= self.color)
        self.body.mainloop()
    def params_label(self, num):
      label = Label(self.body)
      if num == 0:
        frame2 = PhotoImage(file='Murimuri.gif', format="gif -index 2")
      elif num == 1:
        frame2 = PhotoImage(file='Murimuri.gif', format="gif -index 2")
      else:
        frame2 = PhotoImage(file='Murimuri.gif', format="gif -index 2")
      print('pero si entra a la funcion {}'.format(self.value))
      label.configure(image=frame2)
    def params_canvas(self):
        self.canvas.pack()
        self.canvas.config(bg=self.color)      
    def params_entry(self, onEnter):
        self.entry.bind('<Return>', onEnter)
        self.entry.place(x=140, y=50)
        self.entry.pack()
    def start(self, onEnter):
        self.check_file()
        self.params_canvas()
        self.params_entry(onEnter)
        self.params_label(self.value)
        self.params_body()
windowns = Windown()
def onEnter(event):
  codi = windowns.entry.get()
  windowns.entry.delete(0, tk.END)
  code(codi)
def code(codi):
  time.sleep(100)
  downloadH(codi)
def downloadH(code):
  try:
    doujin = Hentai(code)
    if os.path.isdir('H7u7H\{}'.format(code)) == False:
      doujin.download(progressbar=True )
      shutil.move('{}'.format(code), 'H7u7H')
    else:
      windowns.value = 0
  except requests.HTTPError:
    windowns.value = 1
    print('da error')


windowns.start(onEnter)


