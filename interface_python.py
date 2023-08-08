from tkinter import *
  
class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10

        #As duas linhas abaixo fazem a mesma coisa
        #self.sair.bind("<Button-1>", self.mudarTexto) #para usar use: 'def mudarTexto(self, event):' na definição da função mudarTexto 
        self.sair["command"] = self.mudarTexto
        
        self.sair.pack ()
  
    def mudarTexto(self):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"
  
  
root = Tk()
Application(root)
root.mainloop()
