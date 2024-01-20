from tkinter import *
from creational.singleton import Singleton

class Window(Tk, Singleton):
  def init(self):
    super().__init__()

  def __init__(self):
    print('create window')    

  