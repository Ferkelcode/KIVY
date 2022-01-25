#base
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
import socket
from pyobjus import autoclass  # Specific to iOS
from kivy.core.window import Window
Window.clearcolor = (1,1,1,1)


#define 2 screens
class HomeScreen(Screen):
    pass
class SettingScreen(Screen):
    pass

#HomeScreen

GUI = Builder.load_file('main.kv')

class MainApp(App):
    def build(self):
        return GUI
MainApp().run()  


# Client using iPhone and kivy
import time
from kivy.uix.textinput import TextInput




# This client code was built using python when building the kivy-ios project
class Client(App):
    counter = 0
    def build(self):
        # Specific to iOS
        Bridge = autoclass('bridge')
        self.br = Bridge.alloc().init()
        #Magnetometer
        self.br.startMagnetometer()
        #Gyroscope
        self.br.startGyroscope()
        #accelerometer
        self.br.motionManager.setAccelerometerUpdateInterval_(0.1)
        self.br.startAccelerometer()


        # ip found using socket.gethostbyname(socket.gethostname()) on the server (my computer)
        #: include kv
        '''
        g = GridLayout(
                       cols=1
                       ScreenManager:
                           id: screen_manager
                           HomeScreen:
                               name: 'home_screen'
                               id:home_screen
                           SettingsScreen:
                                name: 'setting_screen'
                                id:setting_screen)
                                '''
        g = GridLayout(cols=1)
        b = Button(
            text='Start',
            font_size=66,
            bold=True,
            color='#33BAFF',
            on_release=self.go)
        self.l = Label()
        self.host = TextInput(text='192.168.0.63')
        g.add_widget(b)
        g.add_widget(self.host)
        g.add_widget(self.l)
        g.add_widget(Image(source='logo.png'))
        return g

    def go(self, *args):
        HOST = '192.168.0.63'  # The server's hostname or IP address
        HOST = self.host.text
        PORT = 65436  # The port used by the server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #to open a TCP connection
        self.s.connect((HOST, PORT)) #conncet to computer

        while True:
            time.sleep(.25)
            self.send_msg()

    def send_msg(self, *args):
        self.counter += 1
        '''
        magnet_data = 'magnet', self.br.mg_x, self.br.mg_y, self.br.mg_z # iOS specific
        #self.s.sendall(str(magnet_data).encode('utf-8'))
        gyro_data = 'gyro', self.br.gy_x, self.br.gy_y, self.br.gy_z # iOS specific
        #self.s.sendall(str(gyro_data).encode('utf-8'))
        acc_data = 'acc', self.br.ac_x, self.br.ac_y, self.br.ac_z # iOS specific
        #self.s.sendall(str(acc_data).encode('utf-8'))
        data = magnet_data, gyro_data, acc_data, ' ',
        '''
        data='magnet', self.br.mg_x, self.br.mg_y, self.br.mg_z, 'gyro', self.br.gy_x, self.br.gy_y, self.br.gy_z, 'acc', self.br.ac_x, self.br.ac_y, self.br.ac_z, ' '
        self.s.sendall(str(data).encode('utf-8'))


    def on_stop(self):
        self.s.close()
Client().run()



'''
# This client code was built using python when building the kivy-ios project
class Client(App):
    counter = 0
    def build(self):
        # Specific to iOS
        Bridge = autoclass('bridge')
        self.br = Bridge.alloc().init()
        self.br.startGyroscope()

        # ip found using socket.gethostbyname(socket.gethostname()) on the server (your computer)
        g = GridLayout(cols=1)
        b = Button(
            text='Start',
            font_size=66,
            bold=True,
            color='#33BAFF',
            on_release=self.go)
        self.l = Label()
        self.host = TextInput(text='192.168.0.63')
        g.add_widget(b)
        g.add_widget(self.host)
        g.add_widget(self.l)
        g.add_widget(Image(source='logo.png'))
        return g

    def go(self, *args):
        HOST = '192.168.0.63'  # The server's hostname or IP address
        HOST = self.host.text
        PORT = 65436  # The port used by the server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #to open a TCP connection
        self.s.connect((HOST, PORT)) #conncet to computer

        while True:
            time.sleep(.25)
            self.send_msg()

    def send_msg(self, *args):
        self.counter += 1
        gyro_data = self.br.gy_x, self.br.gy_y, self.br.gy_z # iOS specific
        self.s.sendall(str(gyro_data).encode('utf-8'))

    def on_stop(self):
        self.s.close()
        
     


# This client code was built using python when building the kivy-ios project
class Client(App):
    counter = 0
    def build(self):
        # Specific to iOS
        Bridge = autoclass('bridge')
        self.br = Bridge.alloc().init()
        self.br.motionManager.setAccelerometerUpdateInterval_(0.1)
        self.br.startAccelerometer()


        # ip found using socket.gethostbyname(socket.gethostname()) on the server (your computer)
        g = GridLayout(cols=1)
        b = Button(
            text='Start',
            font_size=66,
            bold=True,
            color='#33BAFF',
            on_release=self.go)
        self.l = Label()
        self.host = TextInput(text='192.168.0.63')
        g.add_widget(b)
        g.add_widget(self.host)
        g.add_widget(self.l)
        g.add_widget(Image(source='logo.png'))
        return g

    def go(self, *args):
        HOST = '192.168.0.63'  # The server's hostname or IP address
        HOST = self.host.text
        PORT = 65436  # The port used by the server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #to open a TCP connection
        self.s.connect((HOST, PORT)) #conncet to computer

        while True:
            time.sleep(.25)
            self.send_msg()

    def send_msg(self, *args):
        self.counter += 1
        acc_data = self.br.ac_x, self.br.ac_y, self.br.ac_z # iOS specific
        self.s.sendall(str(acc_data).encode('utf-8'))

    def on_stop(self):
        self.s.close()


        '''

    



   