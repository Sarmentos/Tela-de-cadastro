from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'),sg.Input(key='Usuario')],
    [sg.Text('Senha'),sg.Input(key='Senha',password_char='*')],
    [sg.Checkbox('Salvar o login ?')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuarios'] == 'Lucas' and valores['Senha'] == 123456789:
            print('Bem-vendo ao mundo de Lucas!')