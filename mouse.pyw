import pyautogui as pya
import psutil
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
file= open("sus.txt", "r")
contents= int(file.read())
file.close()
def check_battery():
    battery= psutil.sensors_battery()
    percentage= battery.percent
    if percentage <= 20 and contents == 0:
        return True
def popup(message):
    showinfo("Message", message)
event= check_battery()
if event:
    popup("Low power mode procedures are going to be executed")
    pya.moveTo(1689,1046,2)
    pya.click()
    pya.moveTo(1519,759,2)
    pya.click()
    pya.moveTo(1511,850,2)
    pya.click()
    pya.moveTo(1283,817,2)
    file1= open("sus.txt", "w")
    newco= contents+1
    file1.write(str(newco))
    file1.close()
