import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        #super().__init__(**kwargs)
        self.cols = 1
        super(MyGridLayout, self).__init__(**kwargs)
        self.topGrid = GridLayout()
        self.bottomGrid = GridLayout()

        self.topGrid.cols = 2
        self.bottomGrid.cols = 1

        self.tarefinha = False

        self.topGrid.add_widget(Label(text="Frente:"))
        self.frente = TextInput(multiline=False)
        self.topGrid.add_widget(self.frente)

        self.topGrid.add_widget(Label(text="Fundo:"))
        self.fundo = TextInput(multiline=False)
        self.topGrid.add_widget(self.fundo)

        self.topGrid.add_widget(Label(text="Direita:"))
        self.direita = TextInput(multiline=False)
        self.topGrid.add_widget(self.direita)

        self.topGrid.add_widget(Label(text="Esquerda:"))
        self.esquerda = TextInput(multiline=False)
        self.topGrid.add_widget(self.esquerda)

        self.topGrid.add_widget(Label(text="Resultado:", font_size=20))
        self.resultado = Label(text=" ", font_size=20)
        self.topGrid.add_widget(self.resultado)

        self.button = Button(text="Calcular")
        self.button.bind(on_press=self.calc)
        self.topGrid.add_widget(self.button)

        self.checkButton = CheckBox()
        self.checkButton.bind(active=self.tarefa_escolha)

        self.bottomGrid.add_widget(Label(text="Tarefinha:"))
        self.bottomGrid.add_widget(self.checkButton)

        self.topGrid.add_widget(self.bottomGrid)
        self.add_widget(self.topGrid)
        
    
        

    def tarefa_escolha(self, instance, value):
        if value:
            self.tarefinha = True
        else:
            self.tarefinha = False

    def calc(self, instance):
        #print(self.frente.text)
        try:
            x = (2500 if self.tarefinha else 3600)
            self.resultado.text = str(((float(self.frente.text) + float(self.fundo.text)) * (float(self.direita.text) + float(self.esquerda.text))) / x)
        except:
            self.resultado.text = "0"
        
        self.resultado.text = self.resultado.text + (" tarefas" if float(self.resultado.text) >= 2 else " tarefa")

        

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()
