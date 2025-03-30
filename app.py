from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QInputDialog
from ui import Ui_MainWindow

import json

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.list_notes.itemClicked.connect(self.show_note)
        self.ui.button_note_create.clicked.connect(self.add_note)
        self.ui.button_note_save.clicked.connect(self.save_note)
        self.ui.button_note_del.clicked.connect(self.del_note)
        self.ui.button_tag_add.clicked.connect(self.add_tag)
        self.ui.button_tag_del.clicked.connect(self.del_tag)
        self.ui.button_tag_search.clicked.connect(self.search_tag)

    def add_note(self):
        note_name, ok = QInputDialog.getText( self, "Додати замітку", "Назва замітки:")
        if ok and note_name != "":
            notes[note_name] = {"текст" : "", "теги" : []}
            with open("notes_data.json", "w") as file:
                json.dump(notes, file, ensure_ascii=False)
            ex.ui.list_notes.addItem(note_name)

    def show_note(self):
        # отримуємо текст із замітки з виділеною назвою та відображаємо його в полі редагування
        key = self.ui.list_notes.selectedItems()[0].text()
        print(key)
        self.ui.field_text.setText(notes[key]["текст"])
        self.ui.list_tags.clear()
        self.ui.list_tags.addItems(notes[key]["теги"])
    
    def save_note(self):
        if self.ui.list_notes.selectedItems():
            key = self.ui.list_notes.selectedItems()[0].text()
            notes[key]["текст"] = self.ui.field_text.toPlainText()
            self.ui.list_tags.clear()
            self.ui.list_tags.addItems(notes[key]["теги"])
            with open("notes_data.json", "w") as file:
                json.dump(notes, file, ensure_ascii=False)
        else:
            print("Оберіть замітку для збереження")

    def del_note(self):
        if self.ui.list_notes.selectedItems():
            key = self.ui.list_notes.selectedItems()[0].text()
            del notes[key]
            self.ui.list_notes.clear()
            self.ui.field_text.clear()
            self.ui.list_tags.clear()
            self.ui.list_notes.addItems(notes.keys())
            with open("notes_data.json", "w") as file:
                json.dump(notes, file, ensure_ascii=False)
        else:
            print("Оберіть замітку для видалення")
    
    def add_tag(self):
        if self.ui.list_notes.selectedItems():
            key = self.ui.list_notes.selectedItems()[0].text()
            tag = self.ui.field_tag.text()
            if tag != "":
                notes[key]["теги"].append(tag)
                self.ui.list_tags.clear()
                self.ui.list_tags.addItems(notes[key]["теги"])
                with open("notes_data.json", "w") as file:
                    json.dump(notes, file, ensure_ascii=False)
            else:
                print("Введіть тег")
        else:
            print("Оберіть замітку для додавання тегу")
    
    def del_tag(self):
        if self.ui.list_notes.selectedItems():
            key = self.ui.list_notes.selectedItems()[0].text()
            tag = self.ui.list_tags.selectedItems()[0].text()
            notes[key]["теги"].remove(tag)
            self.ui.list_tags.clear()
            self.ui.list_tags.addItems(notes[key]["теги"])
            with open("notes_data.json", "w") as file:
                json.dump(notes, file, ensure_ascii=False)
        else:
            print("Оберіть замітку для видалення тегу")
    
    def search_tag(self):
        if self.ui.field_tag.text() != "":
            tag = self.ui.field_tag.text()
            self.ui.list_notes.clear()
            for key in notes.keys():
                if tag in notes[key]["теги"]:
                    self.ui.list_notes.addItem(key)
        else:
            print("Введіть тег для пошуку")
        self.ui.field_tag.clear()
    
      
app = QApplication([])
ex = Widget()

try:
    with open("notes_data.json", "r") as file:
        notes = json.load(file)
        ex.ui.list_notes.addItems(notes.keys())
except:
    notes = {
        "Ласкаво просимо!" : {
            "текст" : "Це найкращий додаток для заміток у світі!",
            "теги" : ["добро", "інструкція"]
        }
    }
    print("Помилка завантаження даних")
    with open("notes_data.json", "w") as file:
        json.dump(notes, file)
    ex.ui.list_notes.addItems(notes.keys())

ex.show()
app.exec_()