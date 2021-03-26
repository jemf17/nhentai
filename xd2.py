from tkinter import * 
import tkinter as tk
from hentai import Hentai, Format
import os
import shutil
import requests
import msvcrt
import time

if os.path.isdir('H7u7H') == False:
  os.makedirs('H7u7H')
'''
def hour():
  a = True
  while a:
    r = '{}:{}:{}'.format((-3 + time.gmtime().tm_hour), time.gmtime().tm_min, time.gmtime().tm_sec)
    return r'''
def onEnter(event):
  codi = entry.get()
  entry.delete(0, tk.END)
  code(codi)
def code(codi):
#  print(codi)
  downloadH(codi)
def downloadH(code):
  try:
    doujin = Hentai(code)
    if os.path.isdir('H7u7H\{}'.format(code)) == False:
      doujin.download(progressbar=True )
      shutil.move('{}'.format(code), 'H7u7H')
    else:
      print('esta descargado')
  except requests.HTTPError:
    print('no existe esa wea')
body = Tk()
body.geometry('400x150')
canvas = tk.Canvas(body)
canvas.pack()
canvas.config(bg='#161616')
button = Button(canvas)

entry = tk.Entry(canvas)
entry.bind('<Return>', onEnter)
entry.place(x=140, y=50)
entry.pack()
button.config(command=code)
body.title("Nhentai App")
body.resizable(False, False)
body.iconbitmap('nhentai.ico')
body.config(bg='#161616')
body.mainloop()


    
