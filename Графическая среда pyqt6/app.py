# from PyQt6.QtWidgets import QApplication, QMainWindow
#
# import sys # Только для доступа к аргументам командной строки
#
# # Приложению нужен один (и только один) экземпляр QApplication.
# # Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# # Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
# app = QApplication(sys.argv)
#
# # Создаём виджет Qt — окно.
#
# # window = QWidget()
# # window = QPushButton('Push Me')
# window = QMainWindow()
# window.show()  # Важно: окно по умолчанию скрыто.
#
# # Запускаем цикл событий.
# app.exec()
#
#
# # Приложение не доберётся сюда, пока вы не выйдете и цикл
# # событий не остановится.




# import sys
#
# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#
#
# # Подкласс QMainWindow для настройки главного окна приложения
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         #Задаем название окна
#         self.setWindowTitle("My App")
#         #Создаем виджет кнопку
#         button = QPushButton("Press Me!")
#         #Задаем размер окна
#         self.setFixedSize(QSize(400, 300))
#
#         # Устанавливаем центральный виджет Window.
#         self.setCentralWidget(button)
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()


from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        button = QPushButton('Нажми на меня!')
        button.setCheckable(True)
        #Подключаем кнопку к функции
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)

        self.setCentralWidget(button)
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
















if '__name__' == '__main__':
    main(sys.argv)