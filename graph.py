# -*- coding: utf-8 -*-
import tkinter as tk
import threading
import os, tkinter, tkinter.filedialog, tkinter.messagebox
from tkinter import filedialog
from tkinter import messagebox
import datetime
import time

import signal
import shutil
import os
from stat import *
import sys

import requests
from requests.auth import HTTPBasicAuth as hba
import json
import texttable as tt

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import csv
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

import glob

from tqdm import tqdm


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.pack(expand=1, fill=tk.BOTH, anchor=tk.NW)
        self.create_widgets()

    def create_widgets(self):
        '''
        self.txt = tk.StringVar()
        self.txt.set("0%")
        status = tk.Label(root, text="にゃんぱすー", borderwidth=2, relief="groove")
        status.pack(side=tk.BOTTOM, fill=tk.X)
        status.set("a")
        '''

        status = tk.Label(root, text="graph", borderwidth=2, relief="groove")
        status.place(x=10,y=50)

        button = tk.Button(self, text="dir", command=self.getapi)
        button.place(x=400, y=50)

        graphbutton = tk.Button(self, text="write", command=self.graph)
        graphbutton.place(x=450, y=50)

        exitbutton = tk.Button(self, text="Exit", command=self.Exit)
        exitbutton.place(x=580, y=50)

        deletebutton = tk.Button(self, text="delete", command=self.delete)
        deletebutton.place(x=500, y=50)

        # ラベルの作成
        # 「ファイル」ラベルの作成
        self.filename = tk.StringVar()

        label1 = tk.Label(self, textvariable=self.filename)
        label1.grid(row=0, column=0)

        # 参照ファイルパス表示ラベルの作成
        self.file1 = tk.StringVar()
        file1_entry = tk.Entry(self, textvariable=self.file1, width=50)
        file1_entry.grid(row=0, column=2)



    def delete(self):
        plt.close()

    def Exit(self):

        self.quit()  # ウインドウを消す
        sys.exit()  # アプリ終了

    def getapi(self):

        fTyp = [('Excelファイル', '*.csv')]
        iDir = os.path.abspath(os.path.dirname(__file__))
        print(iDir)
        print(fTyp)
        # tk.messagebox.showinfo('○×プログラム','処理ファイルを選択してください！')
        file = tk.filedialog.askopenfilenames(filetypes = fTyp,initialdir = iDir)
        print(file)
        # 処理ファイル名の出力
        messagebox.showinfo('参照ファイル1', file)

        self.file1.set(file)


    def graph(self):
        print(self.file1.get())

        #f=open(self.file1.get(),'r')
        f=open('/Users/akirakoumatsuoka/Desktop/removeG/remove/remove_08_190513033406_akitaka_08.csv','r')
        f = csv.reader(f)
        x = []
        y = []
        z = []
        for j in f:
            x.append(float(j[0]))
            y.append(float(j[1]))
            z.append(float(j[2]))
        fig = plt.figure()
        ax = Axes3D(fig)

        ax.plot(x, y, z, marker="o", linestyle='solid')
        plt.show()



root = tk.Tk()
root.geometry("650x100")
# root.geometry("800x360")
root.title("graph")

app = Application(master=root)
app.mainloop()

