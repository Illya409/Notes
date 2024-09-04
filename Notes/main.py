from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout

app = QApplication([])

notes_win = QWidget()
notes_win.setWindowTitle("Розумні замітки")
notes_win.resize(900,600)

list_notes = QListWidget()
list_notes_label = QLabel("Список заміток")

button_note_create = QPushButton("Створити Замітку")
button_note_del = QPushButton("Видалити Замітку")
button_note_save = QPushButton("Зберегти Замітку")

filed_tag = QLineEdit("")
filed_tag.setPlaceholderText("Введіть тег...")
filed_text = QTextEdit()

button_tag_add = QPushButton("Додати до замітки")
button_tag_del = QPushButton("Відкріпити від заміток")
button_tag_search = QPushButton("Шукати замітки по тегу")
list_tag = QListWidget()
list_tag_label = QLabel("Список тегів")

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(filed_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tag_label)
col_2.addWidget(list_tag)
col_2.addWidget(filed_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)
col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)

notes_win.setLayout(layout_notes)

notes_win.show()
app.exec_()




































