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
    '''
    def params_label(self, num = NONE):
      label = Label(self.body, bg= self.color)
      if num == 0:
        frame2 = PhotoImage(file='Murimuri.gif', format="gif -index 2")
        label.configure(image=nextframe, text='')
        
      elif num == 1:
        frame2 = PhotoImage(file='Murimuri.gif', format="gif -index 2")
        label.configure(image=nextframe, text='')
       
      else:
       label.configure(text='hola mundo')
        
      label.pack()
      print('pero si entra a la funcion {}'.format(num))
      '''
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
        #self.params_label()
        self.params_body()
windowns = Windown()
def onEnter(event):
  codi = windowns.entry.get()
  windowns.entry.delete(0, tk.END)
  code(codi)
def code(codi):
  downloadH(codi)
def downloadH(code):
  try:
    doujin = Hentai(code)
    if os.path.isdir('H7u7H\{}'.format(code)) == False:
      doujin.download(progressbar=True)
      windowns.params_label(3)
      shutil.move('{}'.format(code), 'H7u7H')
    else:
      print('esta descargado')
      windowns.params_label(1)
  except requests.HTTPError:
    windowns.params_label(0)
    print('da error')


windowns.start(onEnter)


