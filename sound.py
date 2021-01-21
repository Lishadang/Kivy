from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout

class SoundPlayer(BoxLayout):

    def play_sound(self):
        sound = SoundLoader.load('audio.mp3')

        if sound:
            sound.volume = 0.3
            sound.play()

class HelloApp(App):
    def build(self):
        return SoundPlayer

HelloApp().run()