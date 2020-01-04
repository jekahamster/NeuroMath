import threading

from recognizer import Recognizer
from settings_controller import SettingsController
from calculator import Calculator
if (SettingsController.finderMode == 0):
    from symbol_finder import SymbolFinder
elif (SettingsController.finderMode == 1):
    from recursive_symbol_finder import SymbolFinder
elif (SettingsController.finderMode == 2):
    from sector_symbol_finder import SymbolFinder


import kivy
from kivy.config import Config
SettingsController.loadFrom(SettingsController.DEFAULT_PATH)
Config.set("graphics", "resizable", SettingsController.windowResizable)
Config.set("graphics", "width", SettingsController.windowWidth)
Config.set("graphics", "height", SettingsController.windowHeight)
Config.set("kivy","window_icon", "nm1.ico")
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.theming import ThemeManager

# Config.write()
# Window.size = (900, 500)
# Window.clearcolor = (.70, .70, .70, 1)

color = 1
brushSize = 5

class Container(BoxLayout):
    prevAns = ""
    imgList = None
    recognizer = Recognizer()
    textColor = [1, 1, 1, 1] if (SettingsController.theme == "Dark") else [0, 0, 0, 1]

    def changeColor(self, c):
        global color
        color = c

    def changeBrushSize(self, d):
        global brushSize
        brushSize = d

    def clear(self, c):
        self.ids.text_input.text = ""
        with c.canvas:
            Color(0, 0, 0)
            Rectangle(pos=c.pos, size=c.size)

    def recognize(self, canvas):
        PATH = SettingsController.canvasImg
        canvas.export_to_png(PATH)
        self.ids.text_input.text = "Loading..."
        threading.Thread(target=self.recognizeInNewThread, args=(PATH, ), daemon=True).start()

    def recognizeInNewThread(self, PATH):
        self.imgList = SymbolFinder.find(PATH)
        outputList = self.recognizer.recognize(self.imgList)
        print(outputList)
        outputStr = "".join(outputList)
        self.ids.text_input.text = outputStr
        try:
            ans, mode = Calculator().calc(outputStr)
            print(mode)
            if mode == Calculator.DEFAULT:
                pass
            elif mode == Calculator.EQUALITY:
                self.ids.text_input.text += " = "+str(ans)
            elif mode == Calculator.INEQUALITY:
                self.ids.text_input.text += " is "+str(ans)
        except SyntaxError:
            pass
        except ZeroDivisionError:
            pass
        except TypeError:
            pass
        self.prevAns = ""

    def adjust(self, text):
        if text == self.prevAns:
            return
        else:
            self.prevAns = text
        self.ids.text_input.text = "Adjusting "+str(text) 
        text = list(text)
        threading.Thread(target=self.adjustInNewThread, args=(text, ), daemon=True).start()

    def adjustInNewThread(self, text):
        self.recognizer.adjust(self.imgList, text)
        self.ids.text_input.text = "".join(text)


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
    title = "NeuroMath"
    icon = "NM.ico"
    def build(self):
        self.theme_cls.theme_style = SettingsController.theme
        self.theme_cls.primary_palette = SettingsController.primaryPalette
        return Container()



app = NetworkApp()
app.run()
