import sys
import time
import sqlite3
import paramiko
# import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, \
    QVBoxLayout, QPushButton, QLabel, QGroupBox, QGridLayout, QMessageBox, QLineEdit, QDateEdit
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from datetime import datetime

sshclient = paramiko.SSHClient()
sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshclient.connect(hostname="89.223.66.96", username="root", password="kt+Kkm8WHJM.DV")

ftp = sshclient.open_sftp()
ftp.get("/home/fletbot/bron/data.db", "data.db")
db = sqlite3.connect("data.db")
cursor = db.cursor()


class HotelBookingApp(QWidget):
    """Инициализация класса панелей бронирования номера"""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.startDate = None
        self.stopDate = None
        hbox = QHBoxLayout(self)
        left_panel = QVBoxLayout()
        grid_layout = QGridLayout()
        # Создание и расположение пятидесяти кнопок и установка им цвета
        self.btn1 = QPushButton('1')
        self.btn2 = QPushButton('2')
        self.btn3 = QPushButton('3')
        self.btn4 = QPushButton('4')
        self.btn5 = QPushButton('5')
        self.btn6 = QPushButton('6')
        self.btn7 = QPushButton('7')
        self.btn8 = QPushButton('8')
        self.btn9 = QPushButton('9')
        self.btn10 = QPushButton('10')
        self.btn11 = QPushButton('11')
        self.btn12 = QPushButton('12')
        self.btn13 = QPushButton('13')
        self.btn14 = QPushButton('14')
        self.btn15 = QPushButton('15')
        self.btn16 = QPushButton('16')
        self.btn17 = QPushButton('17')
        self.btn18 = QPushButton('18')
        self.btn19 = QPushButton('19')
        self.btn20 = QPushButton('20')
        self.btn21 = QPushButton('21')
        self.btn22 = QPushButton('22')
        self.btn23 = QPushButton('23')
        self.btn24 = QPushButton('24')
        self.btn25 = QPushButton('25')
        self.btn26 = QPushButton('26')
        self.btn27 = QPushButton('27')
        self.btn28 = QPushButton('28')
        self.btn29 = QPushButton('29')
        self.btn30 = QPushButton('30')
        self.btn31 = QPushButton('31')
        self.btn32 = QPushButton('32')
        self.btn33 = QPushButton('33')
        self.btn34 = QPushButton('34')
        self.btn35 = QPushButton('35')
        self.btn36 = QPushButton('36')
        self.btn37 = QPushButton('37')
        self.btn38 = QPushButton('38')
        self.btn39 = QPushButton('39')
        self.btn40 = QPushButton('40')
        self.btn41 = QPushButton('41')
        self.btn42 = QPushButton('42')
        self.btn43 = QPushButton('43')
        self.btn44 = QPushButton('44')
        self.btn45 = QPushButton('45')
        self.btn46 = QPushButton('46')
        self.btn47 = QPushButton('47')
        self.btn48 = QPushButton('48')
        self.btn49 = QPushButton('49')
        self.btn50 = QPushButton('50')

        grid_layout.addWidget(self.btn1, 1, 1)
        grid_layout.addWidget(self.btn2, 1, 2)
        grid_layout.addWidget(self.btn3, 1, 3)
        grid_layout.addWidget(self.btn4, 1, 4)
        grid_layout.addWidget(self.btn5, 1, 5)
        grid_layout.addWidget(self.btn6, 2, 1)
        grid_layout.addWidget(self.btn7, 2, 2)
        grid_layout.addWidget(self.btn8, 2, 3)
        grid_layout.addWidget(self.btn9, 2, 4)
        grid_layout.addWidget(self.btn10, 2, 5)

        grid_layout.addWidget(self.btn11, 3, 1)
        grid_layout.addWidget(self.btn12, 3, 2)
        grid_layout.addWidget(self.btn13, 3, 3)
        grid_layout.addWidget(self.btn14, 3, 4)
        grid_layout.addWidget(self.btn15, 3, 5)
        grid_layout.addWidget(self.btn16, 4, 1)
        grid_layout.addWidget(self.btn17, 4, 2)
        grid_layout.addWidget(self.btn18, 4, 3)
        grid_layout.addWidget(self.btn19, 4, 4)
        grid_layout.addWidget(self.btn20, 4, 5)

        grid_layout.addWidget(self.btn21, 5, 1)
        grid_layout.addWidget(self.btn22, 5, 2)
        grid_layout.addWidget(self.btn23, 5, 3)
        grid_layout.addWidget(self.btn24, 5, 4)
        grid_layout.addWidget(self.btn25, 5, 5)
        grid_layout.addWidget(self.btn26, 6, 1)
        grid_layout.addWidget(self.btn27, 6, 2)
        grid_layout.addWidget(self.btn28, 6, 3)
        grid_layout.addWidget(self.btn29, 6, 4)
        grid_layout.addWidget(self.btn30, 6, 5)

        grid_layout.addWidget(self.btn31, 7, 1)
        grid_layout.addWidget(self.btn32, 7, 2)
        grid_layout.addWidget(self.btn33, 7, 3)
        grid_layout.addWidget(self.btn34, 7, 4)
        grid_layout.addWidget(self.btn35, 7, 5)
        grid_layout.addWidget(self.btn36, 8, 1)
        grid_layout.addWidget(self.btn37, 8, 2)
        grid_layout.addWidget(self.btn38, 8, 3)
        grid_layout.addWidget(self.btn39, 8, 4)
        grid_layout.addWidget(self.btn40, 8, 5)

        grid_layout.addWidget(self.btn41, 9, 1)
        grid_layout.addWidget(self.btn42, 9, 2)
        grid_layout.addWidget(self.btn43, 9, 3)
        grid_layout.addWidget(self.btn44, 9, 4)
        grid_layout.addWidget(self.btn45, 9, 5)
        grid_layout.addWidget(self.btn46, 10, 1)
        grid_layout.addWidget(self.btn47, 10, 2)
        grid_layout.addWidget(self.btn48, 10, 3)
        grid_layout.addWidget(self.btn49, 10, 4)
        grid_layout.addWidget(self.btn50, 10, 5)

        self.btn1.clicked.connect(lambda checked, i=1: self.showRoomInfo(1))
        self.btn2.clicked.connect(lambda checked, i=2: self.showRoomInfo(2))
        self.btn3.clicked.connect(lambda checked, i=3: self.showRoomInfo(3))
        self.btn4.clicked.connect(lambda checked, i=4: self.showRoomInfo(4))
        self.btn5.clicked.connect(lambda checked, i=5: self.showRoomInfo(5))
        self.btn6.clicked.connect(lambda checked, i=6: self.showRoomInfo(6))
        self.btn7.clicked.connect(lambda checked, i=7: self.showRoomInfo(7))
        self.btn8.clicked.connect(lambda checked, i=8: self.showRoomInfo(8))
        self.btn9.clicked.connect(lambda checked, i=9: self.showRoomInfo(9))
        self.btn10.clicked.connect(lambda checked, i=10: self.showRoomInfo(10))
        self.btn11.clicked.connect(lambda checked, i=11: self.showRoomInfo(11))
        self.btn12.clicked.connect(lambda checked, i=12: self.showRoomInfo(12))
        self.btn13.clicked.connect(lambda checked, i=13: self.showRoomInfo(13))
        self.btn14.clicked.connect(lambda checked, i=14: self.showRoomInfo(14))
        self.btn15.clicked.connect(lambda checked, i=15: self.showRoomInfo(15))
        self.btn16.clicked.connect(lambda checked, i=16: self.showRoomInfo(16))
        self.btn17.clicked.connect(lambda checked, i=17: self.showRoomInfo(17))
        self.btn18.clicked.connect(lambda checked, i=18: self.showRoomInfo(18))
        self.btn19.clicked.connect(lambda checked, i=19: self.showRoomInfo(19))
        self.btn20.clicked.connect(lambda checked, i=20: self.showRoomInfo(20))
        self.btn21.clicked.connect(lambda checked, i=21: self.showRoomInfo(21))
        self.btn22.clicked.connect(lambda checked, i=22: self.showRoomInfo(22))
        self.btn23.clicked.connect(lambda checked, i=23: self.showRoomInfo(23))
        self.btn24.clicked.connect(lambda checked, i=24: self.showRoomInfo(24))
        self.btn25.clicked.connect(lambda checked, i=25: self.showRoomInfo(25))
        self.btn26.clicked.connect(lambda checked, i=26: self.showRoomInfo(26))
        self.btn27.clicked.connect(lambda checked, i=27: self.showRoomInfo(27))
        self.btn28.clicked.connect(lambda checked, i=28: self.showRoomInfo(28))
        self.btn29.clicked.connect(lambda checked, i=29: self.showRoomInfo(29))
        self.btn30.clicked.connect(lambda checked, i=30: self.showRoomInfo(30))
        self.btn31.clicked.connect(lambda checked, i=31: self.showRoomInfo(31))
        self.btn32.clicked.connect(lambda checked, i=32: self.showRoomInfo(32))
        self.btn33.clicked.connect(lambda checked, i=33: self.showRoomInfo(33))
        self.btn34.clicked.connect(lambda checked, i=34: self.showRoomInfo(34))
        self.btn35.clicked.connect(lambda checked, i=35: self.showRoomInfo(35))
        self.btn36.clicked.connect(lambda checked, i=36: self.showRoomInfo(36))
        self.btn37.clicked.connect(lambda checked, i=37: self.showRoomInfo(37))
        self.btn38.clicked.connect(lambda checked, i=38: self.showRoomInfo(38))
        self.btn39.clicked.connect(lambda checked, i=39: self.showRoomInfo(39))
        self.btn40.clicked.connect(lambda checked, i=40: self.showRoomInfo(40))
        self.btn41.clicked.connect(lambda checked, i=41: self.showRoomInfo(41))
        self.btn42.clicked.connect(lambda checked, i=42: self.showRoomInfo(42))
        self.btn43.clicked.connect(lambda checked, i=43: self.showRoomInfo(43))
        self.btn44.clicked.connect(lambda checked, i=44: self.showRoomInfo(44))
        self.btn45.clicked.connect(lambda checked, i=45: self.showRoomInfo(45))
        self.btn46.clicked.connect(lambda checked, i=46: self.showRoomInfo(46))
        self.btn47.clicked.connect(lambda checked, i=47: self.showRoomInfo(47))
        self.btn48.clicked.connect(lambda checked, i=48: self.showRoomInfo(48))
        self.btn49.clicked.connect(lambda checked, i=49: self.showRoomInfo(49))
        self.btn50.clicked.connect(lambda checked, i=50: self.showRoomInfo(50))

        self.btn1.setStyleSheet("background-color: green")
        self.btn2.setStyleSheet("background-color: green")
        self.btn3.setStyleSheet("background-color: green")
        self.btn4.setStyleSheet("background-color: green")
        self.btn5.setStyleSheet("background-color: green")
        self.btn6.setStyleSheet("background-color: green")
        self.btn7.setStyleSheet("background-color: green")
        self.btn8.setStyleSheet("background-color: green")
        self.btn9.setStyleSheet("background-color: green")
        self.btn10.setStyleSheet("background-color: green")
        self.btn11.setStyleSheet("background-color: green")
        self.btn12.setStyleSheet("background-color: green")
        self.btn13.setStyleSheet("background-color: green")
        self.btn14.setStyleSheet("background-color: green")
        self.btn15.setStyleSheet("background-color: green")
        self.btn16.setStyleSheet("background-color: green")
        self.btn17.setStyleSheet("background-color: green")
        self.btn18.setStyleSheet("background-color: green")
        self.btn19.setStyleSheet("background-color: green")
        self.btn20.setStyleSheet("background-color: green")
        self.btn21.setStyleSheet("background-color: green")
        self.btn22.setStyleSheet("background-color: green")
        self.btn23.setStyleSheet("background-color: green")
        self.btn24.setStyleSheet("background-color: green")
        self.btn25.setStyleSheet("background-color: green")
        self.btn26.setStyleSheet("background-color: green")
        self.btn27.setStyleSheet("background-color: green")
        self.btn28.setStyleSheet("background-color: green")
        self.btn29.setStyleSheet("background-color: green")
        self.btn30.setStyleSheet("background-color: green")
        self.btn31.setStyleSheet("background-color: green")
        self.btn32.setStyleSheet("background-color: green")
        self.btn33.setStyleSheet("background-color: green")
        self.btn34.setStyleSheet("background-color: green")
        self.btn35.setStyleSheet("background-color: green")
        self.btn36.setStyleSheet("background-color: green")
        self.btn37.setStyleSheet("background-color: green")
        self.btn38.setStyleSheet("background-color: green")
        self.btn39.setStyleSheet("background-color: green")
        self.btn40.setStyleSheet("background-color: green")
        self.btn41.setStyleSheet("background-color: green")
        self.btn42.setStyleSheet("background-color: green")
        self.btn43.setStyleSheet("background-color: green")
        self.btn44.setStyleSheet("background-color: green")
        self.btn45.setStyleSheet("background-color: green")
        self.btn46.setStyleSheet("background-color: green")
        self.btn47.setStyleSheet("background-color: green")
        self.btn48.setStyleSheet("background-color: green")
        self.btn49.setStyleSheet("background-color: green")
        self.btn50.setStyleSheet("background-color: green")

        group_box = QGroupBox("Номера гостиниц от 1 до 50")
        group_box.setLayout(grid_layout)
        left_panel.addWidget(group_box)

        hbox.addLayout(left_panel, 3)
        self.right_panel = QVBoxLayout()
        self.right_panel.addStretch(100)
        hbox.addLayout(self.right_panel, 2)

        self.setLayout(hbox)

        self.setWindowTitle('Бронирование номеров в гостинице')
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def showRoomInfo(self, room_number):

        for i in reversed(range(self.right_panel.count())): # Удаление всех элементов правой панели и добавление новых
            widget = self.right_panel.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        self.room_number = room_number
        info_label = QLabel(f"Информация о номере {room_number}")
        self.setFilter = QPushButton("Выбрать дни пребывания")
        # Запрос к БД с информацией о номере
        roomInfo = cursor.execute(f"SELECT * FROM RoomDescriptions WHERE number={room_number}").fetchone()
        _, self.floor, self.type, self.onePlace, self.twoPlace, self.rooms, self.pl, self.price, self.checkinout = roomInfo
        bronData = ',\n'.join([' - '.join(i.split(' ')) for i in self.checkinout.split(';')])
        # Текст информации о номере
        info = f"""Этаж: {self.floor}
        Тип: {self.type}
        Количество одноместных кроватей: {self.onePlace}
        Количество двуместных кроватей: {self.twoPlace}
        Количество комнат: {self.rooms}
        Площадь: {self.pl} кв.м
        Цена: {self.price}
        Даты бронирования: {bronData}"""

        # Расположение кнопок для брони, скрытия и выбора дней
        placeholder_label = QLabel(info)
        book_button = QPushButton(f"Забронировать номер")
        book_button.clicked.connect(self.bookButton)
        reset_button = QPushButton(f"Скрыть информацию")
        reset_button.clicked.connect(self.reset_info)
        
        info_label.setStyleSheet("font-size: 20px;")
        info_label.move(20, 20)

        self.right_panel.addWidget(info_label)
        self.right_panel.addWidget(placeholder_label)

        self.right_panel.addWidget(book_button)
        self.right_panel.addWidget(reset_button)
        self.right_panel.addWidget(self.setFilter)
        self.setFilter.clicked.connect(self.openFilters)

        
    
    def bookButton(self):
        """Открытие окна бронирования номера с имеющимися исключениями"""
        if self.startDate is None or self.stopDate is None:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Ошибка бронирования")
            msgbox.setText("Вы еще не выбрали дни проживания и не можете забронировать номер")
            msgbox.exec()
            return
        
        self.bron = Bron(self)
        self.bron.show()

    
    def openFilters(self):
        """Открытие окна выбора дней пребывания"""
        self.addFilters = AddFiltersWindow(self)

    def reset_info(self):
        """Скрытие информации о номере"""
        for i in reversed(range(self.right_panel.count())):
            widget = self.right_panel.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()


class HotelMainApp(QWidget):
    """Класс главного экрана приложения"""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.accountName = "без аккаунта"
        self.isAuth = False
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Отель')
        """Расположение картинок, кнопок, информации об аккаунте и т.д"""
        label = QLabel('Гостиница', self)
        pixmap = QPixmap("zxc.png")
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont('Arial', 30))
        self.book_button = QPushButton('Забронировать номер', self)
        self.signin_button = QPushButton("Вход")
        self.register_button = QPushButton("Регистрация", self)
        self.exit_button = QPushButton('Выйти', self)
        self.signinfo = QLabel(f"Имя аккаунта: {self.accountName}")
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(self.book_button)
        vbox.addWidget(self.signin_button)
        vbox.addWidget(self.register_button)
        vbox.addWidget(self.exit_button)
        vbox.addWidget(self.signinfo)
        self.setLayout(vbox)
        self.signin_button.clicked.connect(self.openSignInWindow)
        self.register_button.clicked.connect(self.openRegistrationWindow)
        self.book_button.clicked.connect(self.openHotelBookingApp)
        self.exit_button.clicked.connect(self.signout)
        self.show()
    
    def openSignInWindow(self):
        """Открытие окна входа в аккаунт, если пользователь еще не авторизован"""
        if not self.isAuth:    
            self.signinWindow = SigniniWindow(self)
            self.signinWindow.show()

    def signout(self):
        """Открытие окна подтверждения выхода из акканута"""
        if self.isAuth:
            self.confirmexit = confirmExit(self)
            self.confirmexit.show()

    def openRegistrationWindow(self):
        """Открытие окна регистрации"""
        if not self.isAuth:
            self.registration_window = RegistrationWindow(self)
            self.registration_window.show()

    def openHotelBookingApp(self):
        '''Открытие окна информации о номерах с двумя панелями, обрабатывая ошибки'''
        if self.isAuth:
            self.initial_window = HotelBookingApp()
            self.initial_window.show()
        else:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Ошибка авторизации")
            msgbox.setText("Вы не можете забронировать номер без авторизации. Войдите в аккаунт или зарегистрируйтесь")
            msgbox.exec()


class AddFiltersWindow(QWidget):
    '''Установка промежутка дат для бронирования'''
    def __init__(self, clas: HotelBookingApp):
        super().__init__()
        self.clas = clas
        self.initUI()

    def initUI(self):
        """Создание двух виджетов с выбором даты, которые задают начало и конец пребывания"""
        self.setWindowTitle("Дата пребывания")
        self.hbox = QHBoxLayout()
        self.date1 = QDateEdit()
        self.date2 = QDateEdit()
        
        self.hbox.addWidget(self.date1)
        self.hbox.addWidget(self.date2)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(QLabel("Дата заселения - дата выселения"))
        self.vbox.addLayout(self.hbox)
        self.apply_button = QPushButton("Применить фильтр")
        self.vbox.addWidget(self.apply_button)
        self.apply_button.clicked.connect(self.applyFilter)
        self.setLayout(self.vbox)
        self.show()
    
    def applyFilter(self):
        '''Изменение цвета кнопок в зависимости от занятости номера в заданный промежуток'''
        redButtons = []
        greenButtons = []
        daterange = [self.date1.text(), self.date2.text()]
        lst = cursor.execute('SELECT number, checkinout FROM RoomDescriptions').fetchall()
        for num, checkinout in lst:
            lstt = [i.split(":") for i in checkinout.split(';')][:-1]
            isred = False
            for i in lstt:
                if check_intersection(daterange, i):
                    isred = True
                    break
            if isred:
                redButtons.append(num)
            else:
                greenButtons.append(num)
        self.clas.startDate = self.date1.text()
        self.clas.stopDate = self.date2.text()

        date1_obj = datetime.strptime(self.date1.text(), '%d.%m.%Y')
        date2_obj = datetime.strptime(self.date2.text(), '%d.%m.%Y')
        '''Проверка выбора дат'''
        if date1_obj > date2_obj:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Ошибка даты")
            msgbox.setText("Ошибка. Первая дата не может быть больше второй")
            msgbox.exec()
            return
        current_date = datetime.now().strftime('%d.%m.%Y')
        if datetime.strptime(current_date, '%d.%m.%Y') > date1_obj:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Ошибка даты")
            msgbox.setText("Ошибка. Первая дата не может быть выбрана до сегодняшнего дня")
            msgbox.exec()
            return
        

        makeRedOrGreen(redButtons, self.clas, "red")
        makeRedOrGreen(greenButtons, self.clas, "green")
        


class confirmExit(QWidget):
    '''Окно подтверждения выхода из аккаунта'''
    def __init__(self, clas: HotelMainApp):
        super().__init__()
        self.clas = clas
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Выход из аккаунта")
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.vbox.addWidget(QLabel("Вы действительно зотите выйти из акканута?"))
        self.yesbtn = QPushButton("Да")
        self.nobtn = QPushButton("Нет")
        self.yesbtn.clicked.connect(self.yesbtnf)
        self.nobtn.clicked.connect(self.nobtnf)
        self.hbox.addWidget(self.yesbtn)
        self.hbox.addWidget(self.nobtn)
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)

    def yesbtnf(self):
        self.clas.isAuth = False
        self.clas.accountName = "без аккаунта"
        self.clas.signinfo.setText(f"Имя аккаунта: {self.clas.accountName}")
        self.close()
        return
    
    def nobtnf(self):
        self.close()
        return


class SigniniWindow(QWidget):
    '''Окно входа в аккаунт'''
    def __init__(self, clas: HotelMainApp):
        super().__init__()
        self.clas = clas
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Вход в аккаунт")
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.setGeometry(10, 10, 180, 18)
        self.continue_button = QPushButton("Продолжить")
        self.ispassw = QLabel(" ")
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.ispassw)
        self.vbox.addWidget(QLabel("Введите имя пользователя:"))
        self.vbox.addWidget(self.username_input)
        self.vbox.addWidget(QLabel("Введите пароль:"))
        self.vbox.addWidget(self.password_input)
        self.vbox.addWidget(self.continue_button)
        self.continue_button.clicked.connect(self.sendPassword)
        self.setLayout(self.vbox)
        self.show()
    
    def sendPassword(self):
        '''Отправка пароля на проверку'''
        username = self.username_input.text().capitalize()
        password = self.password_input.text()
        user = cursor.execute(f'SELECT username FROM users WHERE username="{username}" AND password="{password}"').fetchone()
        if user is not None:
            self.ispassw.setText("Вход подтвержден")
            self.ispassw.setStyleSheet("color: green")
            self.clas.accountName = username
            self.clas.isAuth = True
            self.clas.signinfo.setText(f"Имя аккаунта: {username}")
        
        else:
            self.ispassw.setText("Неверное имя пользователя или пароль. Попробуйте еще раз")
            self.ispassw.setStyleSheet("color: red;")
        

class Bron(QWidget):
    '''Окно бронирования билета'''
    def __init__(self, clas: HotelBookingApp):
        self.clas = clas
        self.price = clas.price
        self.room = clas.room_number
        self.startDate = clas.startDate
        self.stopDate = clas.stopDate
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Оплата номера")
        self.card_input = QLineEdit()
        self.goden_input = QLineEdit()
        self.cvv_input = QLineEdit()
        self.pasportSer_input = QLineEdit()
        self.pasportNum_input = QLineEdit()
        self.apply_opl = QPushButton("Продолжить")
        self.apply_opl.clicked.connect(self.applyOplata)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(QLabel("Введите номер карты:"))
        self.vbox.addWidget(self.card_input)
        self.vbox.addWidget(QLabel("До:                                     CVV:"))
        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(self.goden_input)
        self.hbox1.addWidget(self.cvv_input)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addWidget(QLabel("Паспортные данные (серия, номер):"))
        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.pasportSer_input)
        self.hbox2.addWidget(self.pasportNum_input)
        self.vbox.addLayout(self.hbox2)
        date1_obj = datetime.strptime(self.startDate, '%d.%m.%Y')
        date2_obj = datetime.strptime(self.stopDate, '%d.%m.%Y')
        delta = date2_obj - date1_obj
        days = abs(delta.days) + 1
        self.vbox.addWidget(QLabel(f"К оплате: {self.price * days}"))
        self.vbox.addWidget(self.apply_opl)
        self.setLayout(self.vbox)
        self.show()

    def applyOplata(self):
        '''Оплата номера с проверкой данных на валидность'''
        card = self.card_input.text()
        goden = self.goden_input.text().replace("/", "").replace(" ", '').replace(".", "")
        if len(goden) != 4:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Ошибка валидности")
            msgbox.setText("Произошла ошибка. Невалидный срок годности карты")
            msgbox.exec()
            return

        goden = [goden[0:2], goden[2:4]]
        if not (goden[1].isnumeric() and goden[0].isnumeric() and int(goden[0]) <= 12 and int(goden[0]) >= 1):
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Ошибка валидности")
            msgbox.setText("Произошла ошибка. Невалидный срок годности карты")
            msgbox.exec()
            return

        cvv = self.cvv_input.text()
        if not (cvv.isnumeric() and len(cvv) == 3):
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Ошибка валидности")
            msgbox.setText("Произошла ошибка. Невалидный CVV код")
            msgbox.exec()
            return

        pasportSer = self.pasportSer_input.text()
        if not (pasportSer.isnumeric() and pasportSer[0] == "8" and len(pasportSer) == 4):
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Ошибка валидности")
            msgbox.setText("Произошла ошибка. Невалидная серия паспорта")
            msgbox.exec()
            return

        pasportNum = self.pasportNum_input.text()
        if not (pasportNum.isnumeric() and len(pasportNum) == 6):
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Ошибка валидности")
            msgbox.setText("Произошла ошибка. Невалидный номер паспорта")
            msgbox.exec()
            return

        if not isValidCard(card):
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Ошибка валидности")
            msgbox.setText("Произошла ошибка. Такого номера карты не существует")
            msgbox.exec()
            return
        
        sl = getDict(self.clas)
        if sl[self.room].palette().button().color().name() == "#ff0000":
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Повторная регистрация")
            msgbox.setText("Номер на этот промежуток или часть промежутка уже зарегистрирован")
            msgbox.exec()
            return
        
        sl[self.room].setStyleSheet("background-color: red")

        checkinout = cursor.execute(f"SELECT checkinout FROM RoomDescriptions WHERE number={self.room}").fetchone()[0]
        if checkinout == "":
            cursor.execute(f'UPDATE RoomDescriptions SET checkinout="{self.startDate}:{self.stopDate};" WHERE number={self.room}')
        else:
            cursor.execute(f'UPDATE RoomDescriptions SET checkinout="{checkinout}{self.startDate}:{self.stopDate};" WHERE number={self.room}')
        db.commit()

class RegistrationWindow(QWidget):
    '''Окно регистрации'''
    def __init__(self, clas: HotelMainApp):
        super().__init__()
        self.clas = clas
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Регистрация")
        self.name_input = QLineEdit()
        self.surname_input = QLineEdit()
        self.patronymic_input = QLineEdit()
        self.username_input = QLineEdit()
        self.password = QLineEdit()
        self.confirm_password = QLineEdit()
        self.setGeometry(300, 300, 300, 220)
        submit_button = QPushButton('Зарегистрироваться')
        self.phone_input = QLineEdit()
        submit_button.clicked.connect(self.submitData)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Имя:'))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel('Фамилия:'))
        layout.addWidget(self.surname_input)
        layout.addWidget(QLabel('Отчество:'))
        layout.addWidget(self.patronymic_input)
        layout.addWidget(QLabel('Имя пользователя:'))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Пароль:"))
        layout.addWidget(self.password)
        layout.addWidget(QLabel("Подтвердите пароль:"))
        layout.addWidget(self.confirm_password)
        layout.addWidget(QLabel("Номер телефона:"))
        layout.addWidget(self.phone_input)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def submitData(self):
        '''Отправка данных на проверку и обработка ошибок'''
        data = cursor.execute(f'SELECT username FROM users WHERE username="{self.username_input.text().capitalize()}"').fetchone()
        if data is not None:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Имя используется")
            msgbox.setText("Похоже, данное имя пользователя уже используется, попробуйте выбрать другое")
            msgbox.exec()
            return
        if self.password.text() != self.confirm_password.text():
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Ошибка ввода пароля")
            msgbox.setText("Ошибка ввода пароля. Пароли не совпадают")
            msgbox.exec()
            return

        data = cursor.execute(f'SELECT number FROM users WHERE number="{self.phone_input.text()}"').fetchone()
        phone = self.phone_input.text()

        if phone.startswith("+7") and len(phone) == 12 and phone[1:].isnumeric():
            if data is None:
                cursor.execute(F'''INSERT INTO users (
                               username,
                               password,
                               name,
                               surname,
                               patronymic,
                               number) VALUES (
                               "{self.username_input.text().capitalize()}",
                               "{self.password.text()}",
                               "{self.name_input.text().capitalize()}",
                               "{self.surname_input.text().capitalize()}",
                               "{self.patronymic_input.text().capitalize()}",
                               "{self.phone_input.text()}"
                               )''')
                db.commit()
                self.clas.isAuth = True
                self.clas.accountName = "без аккаунта"
                self.clas.signinfo.setText(f"Имя аккаунта: {self.username_input.text()}")
                msgbox = QMessageBox()
                msgbox.setWindowTitle("Успешная регистрация")
                msgbox.setText("Отлично, вы успешно зарегистрированы в системе.\nБыл выполнен автоматический вход")
                msgbox.exec()
                self.close()
                ftp.put("data.db", "/home/fletbot/bron/data.db")
                return
            else:
                msgbox = QMessageBox()
                msgbox.setWindowTitle("Номер используется")
                msgbox.setText("Похоже, данный номер телефона уже используется, попробуй изменить его")
                msgbox.exec()

        else:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Ошибка ввода номера")
            msgbox.setText("Ошибка. Номер не соответствует правилам.\n1. Номер должен начинаться с \"+7\"\n2. Номер должен состоять из 12 символов, включая \"+\"")
            msgbox.exec()


def check_intersection(date_range1, date_range2):
    '''Функция проверки дат на то, что вторая больше первой'''
    start_date1 = datetime.strptime(date_range1[0], "%d.%m.%Y")
    end_date1 = datetime.strptime(date_range1[1], "%d.%m.%Y")
    start_date2 = datetime.strptime(date_range2[0], "%d.%m.%Y")
    end_date2 = datetime.strptime(date_range2[1], "%d.%m.%Y")

    if start_date1 <= end_date2 and start_date2 <= end_date1:
        return True
    else:
        return False
    

def getDict(clas):
    '''Получение доступа к каждой кнопке номера'''
    return {
        1: clas.btn1,
        2: clas.btn2,
        3: clas.btn3,
        4: clas.btn4,
        5: clas.btn5,
        6: clas.btn6,
        7: clas.btn7,
        8: clas.btn8,
        9: clas.btn9,
        10: clas.btn10,
        11: clas.btn11,
        12: clas.btn12,
        13: clas.btn13,
        14: clas.btn14,
        15: clas.btn15,
        16: clas.btn16,
        17: clas.btn17,
        18: clas.btn18,
        19: clas.btn19,
        20: clas.btn20,
        21: clas.btn21,
        22: clas.btn22,
        23: clas.btn23,
        24: clas.btn24,
        25: clas.btn25,
        26: clas.btn26,
        27: clas.btn27,
        28: clas.btn28,
        29: clas.btn29,
        30: clas.btn30,
        31: clas.btn31,
        32: clas.btn32,
        33: clas.btn33,
        34: clas.btn34,
        35: clas.btn35,
        36: clas.btn36,
        37: clas.btn37,
        38: clas.btn38,
        39: clas.btn39,
        40: clas.btn40,
        41: clas.btn41,
        42: clas.btn42,
        43: clas.btn43,
        44: clas.btn44,
        45: clas.btn45,
        46: clas.btn46,
        47: clas.btn47,
        48: clas.btn48,
        49: clas.btn49,
        50: clas.btn50,
    }


def makeRedOrGreen(listOfRed: list, clas: HotelBookingApp, color: str):
    '''Изменение цветов кнопок в зависимости от занятости'''
    sl = getDict(clas)

    for i in listOfRed:
        sl[i].setStyleSheet(f"background-color: {color}")

    
def isValidCard(card_number):
    '''Проверка карты на валидность'''
    card_number = card_number.replace(' ', '')  # удаляем пробелы, если они есть
    if not card_number.isdigit():
        return False  # проверяем, что номер содержит только цифры

    if len(card_number) != 16:
        return False  # проверяем длину номера карты

    digits = list(map(int, card_number))  # преобразуем строку в список цифр

    for i in range(0, 16, 2):
        digits[i] *= 2  # умножаем каждую четную цифру на 2

    digits = [digit - 9 if digit > 9 else digit for digit in digits]  # вычитаем 9 из цифр, если они больше 9

    sum_digits = sum(digits)  # суммируем все цифры

    return sum_digits % 10 == 0  # возвращаем True, если сумма делится на 10 без остатка, иначе False

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = HotelMainApp()
    print(main_app.accountName)
    main_app.show()
    sys.exit(app.exec_())