from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
#from kivy.uix.textinput import TextInp

class cardGame(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.add_widget(Image(source="cards/1_clubs.jpeg"))
        #self.user = TextInput(multiline = False)
        #self.window.add_widget(self.user)

        self.button = Button(text="Lower")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        self.button = Button(text="Higher")
        self.button.bind(on_press=self.callback2)
        self.window.add_widget(self.button)

        self.button = Button(text="Next")
        self.button.bind(on_press=self.callback3)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, event):

        return self.window

    def callback2(self, event):

        return self.window

    def callback3(self, event):
        self.window.add_widget(Image(source="cards/1_hearts.jpeg"))
        return self.window

if __name__ == "__main__":
    cardGame().run()