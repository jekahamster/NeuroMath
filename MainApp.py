from win32api import GetSystemMetrics

from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color

from kivymd.theming import ThemeManager

WINDOW_WIDTH  = GetSystemMetrics(0)
WINDOW_HEIGHT = GetSystemMetrics(1)

print(":::::", WINDOW_WIDTH)
print(":::::", WINDOW_HEIGHT)

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", str(int(WINDOW_WIDTH*10000/1280)))
Config.set("graphics", "height", "500")

Window.clearcolor = (.70, .70, .70, 1)



class Container(BoxLayout):
    pass

class NetworkApp(App):
    theme_cls = ThemeManager()
    title = "NetworkApp"
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Container()



app = NetworkApp()
app.run()
