from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text=self.a)

    def init(self, a):
        self.a = a

t = TestApp()
t.init("asd")
t.run()
