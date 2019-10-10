from win32api import GetSystemMetrics

from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivymd.theming import ThemeManager

WINDOW_WIDTH  = GetSystemMetrics(0)
WINDOW_HEIGHT = GetSystemMetrics(1)

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "10000")
Config.set("graphics", "height", "500")

Window.clearcolor = (.70, .70, .70, 1)

color = 1
brushSize = 5
print(CheckBox().events())

class Container(BoxLayout):
    def changeColor(self, c):
        global color
        color = c

    def changeBrushSize(self, d):
        global brushSize
        brushSize = d

    def clear(self, c):
        with c.canvas:
            Color(0, 0, 0)
            Rectangle(pos=c.pos, size=c.size)


class CanvasWidget(Widget):
    def on_touch_down(self, touch):
        global brushSize

        if (touch.x > self.pos[0]+self.size[0]-brushSize):
            return
        elif (touch.x < self.pos[0]+brushSize):
            return
        elif (touch.y > self.pos[1]+self.size[1]-brushSize):
            return
        elif (touch.y < self.pos[1]+brushSize):
            return
        with self.canvas:
            global color
            if color == 1:
                Color(1, 1, 1)
            else:
                Color(0, 0, 0)

            Ellipse(pos=(touch.x-brushSize/2, touch.y-brushSize/2), size=(brushSize, brushSize))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=brushSize)

    def on_touch_move(self, touch):
        print(1)
        global brushSize
        if (touch.x > self.pos[0]+self.size[0]-brushSize):
            return
        elif (touch.x < self.pos[0]+brushSize):
            return
        elif (touch.y > self.pos[1]+self.size[1]-brushSize):
            return
        elif (touch.y < self.pos[1]+brushSize):
            return
        else:
            try:
                touch.ud['line'].points += [touch.x, touch.y]
            except KeyError:
                pass

class NetworkApp(App):
    theme_cls = ThemeManager()
    title = "NetworkApp"
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Container()



app = NetworkApp()
app.run()
