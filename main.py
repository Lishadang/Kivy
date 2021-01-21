from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        # layout = BoxLayout(orientation='vertical')
        #label1 = Label(text='Hello World')
        # label2 = Label(text='Label 2')
        # button = Button(text='Press Btn')
        # layout.add_widget(label1)
        # layout.add_widget(label2)
        # layout.add_widget(button)
        #return label
        #return layout

        layout = FloatLayout()
        ##label1 = Label(text='Hello', size_hint=(0.125,0.125), pos_hint={'center_x': 0.5, 'center_y':0.5})
        ##label2 = Label(text='There', size_hint=(0.5,0.7), pos_hint={'center_x':0.5, 'center_y':0.1})
        button = Button(text='Press Me', size=(50,50), size_hint=(None,None), pos=(500,100))
        ##layout.add_widget(label1)
        ##layout.add_widget(label2)
        layout.add_widget(button)

        return layout

if __name__ == '__main__':
    MyApp().run()