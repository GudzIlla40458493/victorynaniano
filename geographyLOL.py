import random
from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(500, 500)

lbl = QLabel("Вікторина")
numberlbl = QLabel("Номер переможця")
start8tn = QPushButton("Дізнатися переможця")

main_line = QVBoxLayout()
main_line.addWidget(lbl)
main_line.addWidget(numberlbl)
main_line.addWidget(start8tn)

window.setLayout(main_line)



def banana():
    a = random.randint(1, 10)
    numberlbl.setText(str(a))



start8tn.clicked.connect(banana)
window.show()
app.exec()




