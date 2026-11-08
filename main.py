from kivy.app import App
from kivy.uix.label import Label

class ParthAIApp(App):
    def build(self):
        return Label(text='Hello Parth! Your Android App is Working!', font_size=24)

if __name__ == '__main__':
    ParthAIApp().run()
