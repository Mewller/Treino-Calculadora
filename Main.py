from PySimpleGUI import PySimpleGUI as sg   


# layout
sg.theme('Reddit')
layout = [
    [sg.Text('Conta:'), sg.Input(key='Conta')],
    [sg.Button('Calcular')]
    ,[sg.Output(size=(20, 15)), sg.Text('Meu deus, como isso foi dificil!')]
]

# janela
janela = sg.Window('calculadora', layout)

# eventos
while True:
    eventos, valores = janela.read()
    
    if eventos == sg.WINDOW_CLOSED:
        break
    if 'Calcular' in eventos :
        duvida = valores['Conta']
        if '+' in duvida:
            duvida1 = duvida.split('+')
        elif "*" in duvida:
            duvida1 = duvida.split('*')
        else:
            duvida1 = duvida.split('-')
        
    
    def soma():
        if "+" in duvida:
            res1, res2 = duvida1[0], duvida1[1]
            res1, res2 = int(res1), int(res2)
            res3 = res1 + res2
            print(f'Resultado de {res1}+{res2} é igual a: {res3}')
    def sub():
        if "-" in duvida:
            res1, res2 = duvida1[0], duvida1[1]
            res1, res2 = int(res1), int(res2)
            res3 = res1 - res2
            print(f'Resultado de {res1}-{res2} é igual a: {res3}')
    def vezes():
        if "*" in duvida:
            res1, res2 = duvida1[0], duvida1[1]
            res1, res2 = int(res1), int(res2)
            res3 = res1 * res2    
            print(f'Resultado de {res1}x{res2} é igual a: {res3}')

    if "+" in duvida:
        soma()
            
    elif '-' in duvida:
        sub()
        
    elif '*' in duvida:
        vezes()
        
    else:
        print('Função não cadastrada')
        
janela.mainloop()