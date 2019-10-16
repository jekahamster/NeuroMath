from win32api import GetSystemMetrics
from SymbolFinder import SymbolFinder
from Recognizer import Recognizer

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

# Config.set("graphics", "resizable", "")
# Config.set("graphics", "width", "100")
# Config.set("graphics", "height", "500")

Window.clearcolor = (.70, .70, .70, 1)

color = 1
brushSize = 5

class Container(BoxLayout):
    prevAns = ""
    imgList = None
    recognizer = Recognizer()


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

    def recognize(self, canvas):
        PATH = "temp/temp_img.png"
        canvas.export_to_png(PATH)
        self.imgList = SymbolFinder().find(PATH)
        outputList = self.recognizer.recognize(self.imgList)
        temp_str = "".join(outputList)
        self.ids.text_input.text = temp_str
        try:
            self.ids.text_input.text += "=" + str(eval(temp_str))
        except SyntaxError:
            pass
        except ZeroDivisionError:
            pass
        self.prevAns = ""

    def adjust(self, text):
        if text == self.prevAns:
            return
        else:
            self.prevAns = text
        text = list(text)
        self.recognizer.adjust(self.imgList, text)


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
