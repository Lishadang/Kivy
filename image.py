from kivy.app import App
from kivy.uix.image import Image, AsyncImage



class MyImage(Image):
    pass

class MyApp(App):
    def build(self):
        return MyImage()
        #return Image(source='dfd.png')

MyApp().run()