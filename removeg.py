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

from pylab import *

import glob

from tqdm import tqdm
from scipy import signal

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

        status = tk.Label(root, text="にゃんぱすー", borderwidth=2, relief="groove")
        status.place(x=10,y=50)

        button = tk.Button(self, text="dir", command=self.getapi)
        button.place(x=400, y=50)

        graphbutton = tk.Button(self, text="dp", command=self.graph)
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

        fTyp = [("", ".csv")]
        iDir = os.path.abspath(os.path.dirname(__file__))

        # tk.messagebox.showinfo('○×プログラム','処理ファイルを選択してください！')
        file = filedialog.askdirectory(initialdir=iDir)

        # 処理ファイル名の出力
        messagebox.showinfo('参照ファイル1', file)

        self.file1.set(file)


    def graph(self):
        print(self.file1.get())
        filename = []

        # path = '/Users/akirakoumatsuoka/desktop/data'
        i = 0
        for infile in glob.glob(os.path.join(self.file1.get(), '*.csv')):
            # print (infile)
            filename.append(infile)
            # print(filename[i])
            # i=i+1


        name = 'A-B'




        for i in tqdm(filename):

            fo1 = open(i, 'r')
            f1 = csv.reader(fo1)

            Ax = []
            Ay = []
            Az = []
            Alx = []
            Aly = []
            Alz = []
            Gx = []
            Gy = []
            Gz = []
            Time=[]
            csvlist=[]
            file = os.path.basename(i)
            file1 = open("./remove/remove_" + file, 'w')

            writer1 = csv.writer(file1, lineterminator='\n')
            count=0

            for p,a in enumerate(f1):

                time=(a[0])
                ax=float(a[1])
                ay=float(a[2])
                az=float(a[3])
                alx=float(a[4])
                aly=float(a[5])
                alz=float(a[6])
                gx = float(a[7])
                gy = float(a[8])
                gz = float(a[9])
                Time.append(time)
                Ax.append(ax)
                Ay.append(ay)
                Az.append(az)
                Alx.append(alx)
                Aly.append(aly)
                Alz.append(alz)
                Gx.append(gx)
                Gy.append(gy)
                Gz.append(gz)
            vx=0
            vy=0
            vz=0
            x=0
            y=0
            z=0
            xx=0
            yy=0
            zz=0
            pitch=0
            roll=0
            yaw=0
            cgx=0
            cgy=0
            cgz=0
            a=0.9
            ox=0
            oy=0
            oz=0
            #filter2 = signal.firwin(numtaps=51, cutoff=0.01, fs=1/0.025, pass_zero=False)
            """
            y2 = signal.lfilter(filter2, 1, Ax)
            print(y2)
            F2 = np.fft.fft(y2)
            Amp2 = np.abs(F2/(len(Ax)/2))

            F=np.fft.ifft(F2)
            F= F.real 
            #print(F)
            """
            # データのパラメータ
            N = len(Ax)            # サンプル数
            dt = 0.025          # サンプリング間隔
            fq1, fq2 = 5, 40    # 周波数
            fc = 0.01            # カットオフ周波数
            t = np.arange(0, N*dt, dt) # 時間軸
            freq = np.linspace(0, 1.0/dt, N) # 周波数軸
            
            F = np.fft.fft(Ax)
            F = F/(len(Ax)/2)
            F[0] = F[0]/2
            F2 = F.copy()
            F2[(freq < fc)] = 0
            F2[(freq > 1/(dt*2))] = 0
            # 高速逆フーリエ変換（時間信号に戻す）
            x = np.fft.ifft(F2)

            # 振幅を元のスケールに戻す
            x = np.real(x*N)


            F = np.fft.fft(Ay)
            F = F/(len(Ay)/2)
            F[0] = F[0]/2
            F2 = F.copy()
            F2[(freq < fc)] = 0
            F2[(freq > 1/(dt*2))] = 0
            # 高速逆フーリエ変換（時間信号に戻す）
            y = np.fft.ifft(F2)

            # 振幅を元のスケールに戻す
            y = np.real(y*N)

            F = np.fft.fft(Az)
            F = F/(len(Az)/2)
            F[0] = F[0]/2
            F2 = F.copy()
            F2[(freq < fc)] = 0
            F2[(freq > 1/(dt*2))] = 0
            # 高速逆フーリエ変換（時間信号に戻す）
            z = np.fft.ifft(F2)

            # 振幅を元のスケールに戻す
            z = np.real(z*N)
        
            
            for i ,a in enumerate(x):
                """
                cgx=Ax[i]*a+(1-a)*cgx
                cgy=Ay[i]*a+(1-a)*cgy
                cgz=Az[i]*a+(1-a)*cgz
            
                cx=Ax[i]-cgx
                cy=Ay[i]-cgy
                cz=Az[i]-cgz
                
                xx=cx-ox
                yy=cy-oy
                zz=cz-oz

                ox=cx
                oy=cy
                oz=cz

                if(i==0):

                    continue
                """

                
                csvlist.append(Time[i])
                csvlist.append(x[i])
                csvlist.append(y[i])
                csvlist.append(z[i])
                csvlist.append(Alx[i])
                csvlist.append(Aly[i])
                csvlist.append(Alz[i])
                csvlist.append(Gx[i])
                csvlist.append(Gy[i])
                csvlist.append(Gz[i])
                writer1.writerow(csvlist)
                csvlist=[]
            file1.close()




            fo1.close()



root = tk.Tk()
root.geometry("650x100")
# root.geometry("800x360")
root.title("reconstruct")

app = Application(master=root)
app.mainloop()
