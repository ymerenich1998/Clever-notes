# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.notes_win = QtWidgets.QWidget(MainWindow)
        self.notes_win.setObjectName("notes_win")
        self.field_text = QtWidgets.QTextEdit(self.notes_win)
        self.field_text.setGeometry(QtCore.QRect(10, 10, 511, 521))
        self.field_text.setObjectName("field_text")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.notes_win)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(530, 10, 265, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.col_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.col_1.setContentsMargins(0, 0, 0, 0)
        self.col_1.setObjectName("col_1")
        self.list_notes_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.list_notes_label.setObjectName("list_notes_label")
        self.col_1.addWidget(self.list_notes_label)
        self.list_notes = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.list_notes.setObjectName("list_notes")
        self.col_1.addWidget(self.list_notes)
        self.row_1 = QtWidgets.QHBoxLayout()
        self.row_1.setObjectName("row_1")
        self.button_note_create = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_note_create.setObjectName("button_note_create")
        self.row_1.addWidget(self.button_note_create)
        self.button_note_del = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_note_del.setObjectName("button_note_del")
        self.row_1.addWidget(self.button_note_del)
        self.col_1.addLayout(self.row_1)
        self.button_note_save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_note_save.setObjectName("button_note_save")
        self.col_1.addWidget(self.button_note_save)
        self.list_tags_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.list_tags_label.setObjectName("list_tags_label")
        self.col_1.addWidget(self.list_tags_label)
        self.list_tags = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.list_tags.setObjectName("list_tags")
        self.col_1.addWidget(self.list_tags)
        self.field_tag = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.field_tag.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.field_tag.setText("")
        self.field_tag.setObjectName("field_tag")
        self.col_1.addWidget(self.field_tag)
        self.row_2 = QtWidgets.QHBoxLayout()
        self.row_2.setObjectName("row_2")
        self.button_tag_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_tag_add.setObjectName("button_tag_add")
        self.row_2.addWidget(self.button_tag_add)
        self.button_tag_del = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_tag_del.setObjectName("button_tag_del")
        self.row_2.addWidget(self.button_tag_del)
        self.col_1.addLayout(self.row_2)
        self.button_tag_search = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_tag_search.setObjectName("button_tag_search")
        self.col_1.addWidget(self.button_tag_search)
        MainWindow.setCentralWidget(self.notes_win)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Розумні замітки"))
        self.field_text.setPlaceholderText(_translate("MainWindow", "Введіть замітку..."))
        self.list_notes_label.setText(_translate("MainWindow", "Список заміток"))
        self.button_note_create.setText(_translate("MainWindow", "Створити замітку"))
        self.button_note_del.setText(_translate("MainWindow", "Видалити замітку"))
        self.button_note_save.setText(_translate("MainWindow", "Зберегти замітку"))
        self.list_tags_label.setText(_translate("MainWindow", "Список тегів"))
        self.field_tag.setPlaceholderText(_translate("MainWindow", "Введіть тег..."))
        self.button_tag_add.setText(_translate("MainWindow", "Додати до замітки"))
        self.button_tag_del.setText(_translate("MainWindow", "Відкріпити від замітки"))
        self.button_tag_search.setText(_translate("MainWindow", "Шукати замітку по тегу"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

