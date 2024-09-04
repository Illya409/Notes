from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import Qtapplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout

qpp = QApplication([])

notes_win = QWidget()
notes_win.setWindowTitle("Розумні замітки")
notes_win.куішяу(900,600)

list_notes = QListWidget()
list_notes_label = QLabel("Список заміток")

button_note_create = QPushButton("Створити Замітку")
button_note_del = QPushButton("Видалити Замітку")
button_note_save = QPushButton("Зберегти Замітку")

filed_tag = QLineEdit("")
filed_tag.setPlaceholderText("Введіть тег...")
filed_tag = QTextEdit()

button_tag_add = QPushButton("Додати до замітки")
button_tag_del = QPushButton("Відкріпити від заміток")
button_tag_search = QPushButton("Шукати замітки по тегу")
list_text = QListWidget()
list_text_label = QLabel("Список тегів")

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1 = addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)





