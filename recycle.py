from kivy.app import App
from kivy.uix.recycleview import RecycleView

class RV(RecycleView):
    def __init__(self):
        super().__init__()
        content = ['hello', 'this is a string', 'another string']
        self.data = [{'text':item} for item in content]
        #self.data = [{'text':str(i)} for i in range(20)]


class PartyApp(App):
    def build(self):
        return RV()

PartyApp().run()