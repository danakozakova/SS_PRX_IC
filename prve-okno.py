from kivy.app import App
from kivy.uix.button import Button


class PrveOknoApp(App):
    def build(self):
        return Button(text="Ahoj, Kivy!")


PrveOknoApp().run()