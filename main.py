from PyQt5 import QtWidgets, uic
from random import randint

app = QtWidgets.QApplication([])
ui = uic.loadUi("design.ui")
ui.setWindowTitle("Игра в 21")
ui.setFixedSize(431, 255)
schet1 = 0
schet2 = 0
def add1():
    ui.random_1.setText(str(randint(1,6)))
    num = int(ui.schet_1.text())+int(ui.random_1.text())
    ui.schet_1.setText(str(int(ui.schet_1.text())+int(ui.random_1.text())))
    if int(ui.schet_1.text()) >= 22:
        ui.add_2.setEnabled(False)
        ui.stay_2.setEnabled(False)
        ui.add_1.setEnabled(False)
        ui.stay_1.setEnabled(False)
        ui.label.setText("Победил Игрок 2")
        ui.label.setVisible(True)
    elif int(ui.schet_1.text()) == 21:
        ui.add_2.setEnabled(False)
        ui.stay_2.setEnabled(False)
        ui.add_1.setEnabled(False)
        ui.stay_1.setEnabled(False)
        ui.label.setText("Победил Игрок 1")
        ui.label.setVisible(True)
def add2():
    ui.random_2.setText(str(randint(1,6)))
    num = int(ui.schet_2.text())+int(ui.random_2.text())
    ui.schet_2.setText(str(int(ui.schet_2.text())+int(ui.random_2.text())))
    if int(ui.schet_2.text()) >= 22:
        ui.add_2.setEnabled(False)
        ui.stay_2.setEnabled(False)
        ui.add_1.setEnabled(False)
        ui.stay_1.setEnabled(False)
        ui.label.setText("Победил Игрок 1")
        ui.label.setVisible(True)
    elif int(ui.schet_2.text()) == 21:
        ui.add_2.setEnabled(False)
        ui.stay_2.setEnabled(False)
        ui.add_1.setEnabled(False)
        ui.stay_1.setEnabled(False)
        ui.label.setText("Победил Игрок 2")
        ui.label.setVisible(True)
def stay1():
    global schet1
    schet1 = int(ui.schet_1.text())
    ui.add_1.setEnabled(False)
    ui.stay_1.setEnabled(False)
    if schet2 != 0:
        if schet1 > schet2:
            ui.label.setText("Победил Игрок 1")
            ui.label.setVisible(True)
        elif schet1 < schet2:
            ui.label.setText("Победил Игрок 2")
            ui.label.setVisible(True)
        elif schet1 == schet2:
            ui.label.setText("Ничья")
            ui.label.setVisible(True)
def stay2():
    global schet2
    schet1 = int(ui.schet_2.text())
    ui.add_2.setEnabled(False)
    ui.stay_2.setEnabled(False)
    if schet1 != 0:
        if schet1 > schet2:
            ui.label.setText("Победил Игрок 1")
            ui.label.setVisible(True)
        elif schet1 < schet2:
            ui.label.setText("Победил Игрок 2")
            ui.label.setVisible(True)
        elif schet1 == schet2:
            ui.label.setText("Ничья")
            ui.label.setVisible(True)
ui.label.setVisible(False)
ui.add_1.clicked.connect(add1)
ui.add_2.clicked.connect(add2)
ui.stay_1.clicked.connect(stay1)
ui.stay_2.clicked.connect(stay2)

ui.show()
app.exec()