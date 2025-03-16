from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

import json

'''Замітки в json'''
notes = {
    "Ласкаво просимо!" : {
        "текст" : "Це найкращий додаток для заміток у світі!",
        "теги" : ["добро", "інструкція"]
    }
}

with open("notes_data.json", "w") as file:
    json.dump(notes, file)


class Widget(QMainWindow):
    def __init__(self):
      super().__init__()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      self.ui.list_notes.itemClicked.connect(self.show_note)

    def show_note(self):
        # отримуємо текст із замітки з виділеною назвою та відображаємо його в полі редагування
        key = self.ui.list_notes.selectedItems()[0].text()
        print(key)
        self.ui.field_text.setText(notes[key]["текст"])
        self.ui.list_tags.clear()
        self.ui.list_tags.addItems(notes[key]["теги"])
    
      
app = QApplication([])
ex = Widget()

with open("notes_data.json", "r") as file:
    notes = json.load(file)
ex.ui.list_notes.addItems(notes)

ex.show()
app.exec_()