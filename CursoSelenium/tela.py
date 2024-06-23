#metodo 1
# from kivy.lang import Builder
# from kivymd.app import MDApp
# from kivymd.uix.dialog import MDDialog
# from kivymd.uix.button import MDFlatButton

# kv = '''
# MDFloatLayout:
#     MDFlatButton:
#         text:"Confirmação"
#         pos_hint: {"center_x":0.5,"center_y":0.5}
#         on_release: app.mostraDialogo()
# '''

# class Main(MDApp):
#     dialog = None
#     def build(self):
#         return Builder.load_string(kv)
    
#     def mostraDialogo(self):
#         if not self.dialog:
#             self.dialog = MDDialog(
#                 text = "Deseja Prosseguir? ",
#                 buttons = [
#                     MDFlatButton(
#                         text = "Cancelar",
#                         theme_text_color = "Custom",
#                         text_color = self.theme_cls.primary_color,

#                     ),
#                     MDFlatButton(
#                         text = "Confirma",
#                         theme_text_color = "Custom",
#                         text_color = self.theme_cls.primary_color,

#                     ),
#                 ]
#             )
#         self.dialog.open()

# Main().run()


#metodo2
# from PySimpleGUI import PySimpleGUI as sg

# #Layout
# sg.theme('Reddit')
# layout = [
#     [sg.Text('Usuário'), sg.Input(key='usuario')],
#     [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],
#     [sg.Checkbox('Salvar o login')],
#     [sg.Button('Entrar')],
# ]
# #Janela
# janela = sg.Window('Tela de Login', layout)
# #Ler eventos
# while True:
#     eventos,valores = janela.read()
#     if eventos == sg.WINDOW_CLOSED:
#         break

#     if eventos ==  'Entrar':
#         if valores['usuarios'] == 'Iure' and valores['senha'] == '1234':
#             print('Bem vindo')

#metodo3
# pao = 0

# def comprar():
#     global pao
#     pao += 1
#     text = f'''
#     Você tem um total de {pao} comprados.
#     Abrigado por comprar na padaria Hello World
#     '''
#     texto_pao["text"] = text
    

# from tkinter import *

# janela = Tk()
# janela.title('Hello World')

# texto_orientacao = Label(janela, text='Clique no botão para comprar um pão')
# texto_orientacao.grid(column=0,row=0,padx=10,pady=10)

# botao = Button(janela,text="Comprar",command=comprar)
# botao.grid(column=0,row=2,padx=10,pady=10)

# texto_pao = Label(janela,text='')
# texto_pao.grid(column=0,row=4,padx=10,pady=10)
# janela.mainloop()