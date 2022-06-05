#для начала скопируй сюда интерфейс "Умных заметок" и проверь его работу
#библиотеки какие-то
import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QVBoxLayout,  QLineEdit, QTextEdit, QInputDialog, QFormLayout

#всё нужное
app = QApplication([])
windows = QWidget()
windows.setWindowTitle('кто прочтёт тот кек')
windows.resize(900, 600)

#ещё нужное
text_zona = QTextEdit() #большая зона
iii = QListWidget() #зона ы
TEGI = QListWidget() #зона ЖЁСТКИХ ТЕГОВ
'''zapis = {
    "О привет": {
        "кек": "кароч\n прил 'умные ы и ТЕГИ'('умные заметки')",
        "ТЕГ_КРУТОЙ": ["пшел отсюда", "пример примера"]
    }
} #запись
with open("gik.json", "w", encoding = 'utf-8') as file:
    json.dump(zapis, file)'''

#батоны
b1 = QPushButton("Создать ы")
b2 = QPushButton("Удалить ы")
b3 = QPushButton("Засейфить ы")
b4 = QPushButton("ЗАТЕГАТЬ ПО ЖЁСТКОМУ")
b5 = QPushButton("УБРАТЬ ТЕГ")
b6 = QPushButton("Найти ы по ЖЁСТКОМУ ТЕГУ")

#TEG
TEG1 = QLabel("Список ы")
TEG2 = QLabel("Список ЖЁСТКИХ ТЕГОВ")

#поисковик
shrek = QLineEdit("")
shrek.setPlaceholderText("Вводи ЖЁСТКИЙ ТЕГ")

#шампуры
BOSS = QHBoxLayout()#он тут главный сникерс
colonna1 = QVBoxLayout()#он тут не главный
colonna2 = QVBoxLayout()#он ещё хуже

#эра Димки и Толика
dimka = QHBoxLayout()#тут сломался гелик))
tolik = QHBoxLayout()#а этот вовсе лох))))))))))))
dimka.addWidget(b1)
dimka.addWidget(b2)
tolik.addWidget(b4)
tolik.addWidget(b5)

#настройка колонны
colonna1.addWidget(text_zona)
colonna2.addWidget(TEG1)
colonna2.addWidget(iii)
colonna2.addLayout(dimka)
colonna2.addWidget(b3)

#настройка колонны 2: Возвращение shrek
colonna2.addWidget(TEG2)
colonna2.addWidget(TEGI)
colonna2.addWidget(shrek)
colonna2.addLayout(tolik)
colonna2.addWidget(b6)

#настройка сникерса
BOSS.addLayout(colonna1)
BOSS.addLayout(colonna2)

#функции
def pokashi_zapis():
    kluch = iii.selectedItems()[0].text()
    text_zona.setText(bukva_y[kluch]["кек"])
    TEGI.clear()
    TEGI.addItems(bukva_y[kluch]["ТЕГ_КРУТОЙ"])

def add_y():
    y_name, ok = QInputDialog.getText(windows, "Добавить ы", "Название ы: ")
    if y_name and ok != "":
        bukva_y[y_name] = {
        "кек": "",
        "ТЕГ_КРУТОЙ":[]
        }
        iii.addItem(y_name)
        TEGI.addItems(bukva_y[y_name]["ТЕГ_КРУТОЙ"])

def save_y():
    if iii.selectedItems():
        kluch = iii.selectedItems()[0].text()
        bukva_y[kluch]["кек"] = text_zona.toPlainText()
        with open("gik.json", "w", encoding="utf-8") as file:
            json.dump(bukva_y, file, sort_keys=True)
    else:
        print("'Ты чё с ума сошёл?' feat Karlson")

def del_y():
    if iii.selectedItems():
        kluch = iii.selectedItems()[0].text()
        del bukva_y[kluch]
        iii.clear()
        TEGI.clear()
        text_zona.clear()
        with open("gik.json", "w", encoding="utf-8") as file:
            json.dump(bukva_y, file)
    else:
        print("Ты хочешь удалить пустоту?")

def add_tag():
    if iii.selectedItems():
        kluch = iii.selectedItems()[0].text()
        TEG = shrek.text()
        if TEG not in bukva_y[kluch]["ТЕГ_КРУТОЙ"]:
            bukva_y[kluch]["ТЕГ_КРУТОЙ"].append(TEG)
            TEGI.addItem(TEG)
            with open("gik.json", "w", encoding="utf-8") as file:
                json.dump(bukva_y, file)
            with open("gik.json", "r", encoding = 'utf-8') as file:
                g = json.load(file)
                #TEGI.addItems(g[kluch]["ТЕГ_КРУТОЙ"])
        else:
            print("УЖЕ ЕСТЬ ТЕГ ЭТОТ")
    else:
        print("Ты куда ТЕГ ставить хочешь?")

def del_tag():
    if TEGI.selectedItems():
        kluch = iii.selectedItems()[0].text()
        TEG = TEGI.selectedItems()[0].text()
        bukva_y[kluch]["ТЕГ_КРУТОЙ"].remove(TEG)
        with open("gik.json", "w", encoding="utf-8") as file:
            json.dump(bukva_y, file)
        with open("gik.json", "r", encoding = 'utf-8') as file:
            g = json.load(file)
            TEGI.clear()
            TEGI.addItems(g[kluch]["ТЕГ_КРУТОЙ"])
    else:
        print("Ты какой ТЕГ удалять хочешь?")

def nayti_TEG():
    TAG = shrek.text()
    if b6.text() == "Найти ы по ЖЁСТКОМУ ТЕГУ" and TAG:
        y_filtor = {} #заметки по поиску м...
        for noty in bukva_y:
            if TAG in bukva_y[noty]["ТЕГ_КРУТОЙ"]:
                y_filtor[noty] = bukva_y[noty]
        b6.setText("Сбросить фильтр с моста")
        iii.clear()
        TEGI.clear()
        iii.addItems(y_filtor)
    elif b6.text() == "Сбросить фильтр с моста":
        shrek.clear()
        iii.clear()
        TEGI.clear()
        iii.addItems(bukva_y)
        
        b6.setText("Найти ы по ЖЁСТКОМУ ТЕГУ")



#ПОЕХАЛИ ╥┼├_╩╨╙╥╬╔ ╞и╤╥╩╚┼ ╥┼├╚ ═└╔─╚ ╧╞
iii.itemClicked.connect(pokashi_zapis)
b1.clicked.connect(add_y)
b2.clicked.connect(del_y)
b3.clicked.connect(save_y)
b4.clicked.connect(add_tag)
b5.clicked.connect(del_tag)
b6.clicked.connect(nayti_TEG)
windows.setLayout(BOSS)
windows.show()
with open("gik.json", "r", encoding = 'utf-8') as file:
    bukva_y = json.load(file)
iii.addItems(bukva_y)
app.exec()
#затем запрограммируй демо-версию функционала
