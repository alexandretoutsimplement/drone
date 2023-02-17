#!/usr/bin/env python
#-*- coding utf-8*-
import sys
import tkinter as tk
from PyQt5.QtWidgets import QApplication, QWidjet, QFormLayoutQPushButton, QLineEdit, Qlabel

app = QApplication.instance()
if not app:
        app = QApplication(sys.argv)

fen = QWidget()

fen.setWindowTittle("manette")

tkl=tk.TK()

h=tk1.winfo_screenheight()

w=tk1.winfo_screenwidth()

fen.resize(w,h)

layout = QFormLayout(fen)
monter = QPushButton("monter")
lineEdit1 = QLineEdit()
decendre = QPushButton("décendre")
lineEdit2 = QLineEdit()
pivgauche = QPushButton("pivoter à gauche")
lineEdit3 = QLineEdit()
pivdroite = QPushButton("pivoter à droite")
label1a=QLabel()
label1b=QLabel()
label2=QLabel()
label3a=QLabel()
label3b=QLabel()

layout.addRow(label1a, monter, label1b)
layout.addRow(pivgauche, label2, pivdroite)
layout.addRow(label3a, decendre, label3b)

fen.setLayout(layout)

fen.show()

app.exec()

