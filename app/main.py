from kivy.app import App
from gui.mainwindow import MainWindow

class MapleApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    MapleApp().run()