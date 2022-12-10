import PySimpleGUI as sg
import database
from random import randint

def modalProd():
    sg.change_look_and_feel('TanBlue')
    
    layout2 = [

    [sg.Text('Nome:', size=(5,0)), sg.InputText(size =(15,0),key='-NAME2-')],
    [sg.Text('Qtd:', size=(5,0)), sg.InputText(size =(15,0),key='-QTD2-')],
    [sg.Button('Enviar Dados'), sg.Button('Listar')],
    [sg.Listbox('', size=(80,10), key='-BOX2-')],
    [sg.Button('Sair')],
    
    ]

    window2 = sg.Window('Cadastro de Produtos',size=(875,480)).layout(layout2)
    window2.Finalize()
    window2.TKroot.transient()
    window2.TKroot.grab_set()
    window2.TKroot.focus_force()

    while True:
        event2, values2 = window2.Read()
        if values2 == sg.WIN_CLOSED:
            window2.close()
            break 

        if event2 == 'Sair':
            window2.close()
            break
              
        if event2 == ('Enviar Dados'):
            ID = randint(1, 999)
            NAME = values2['-NAME2-'].capitalize()
            QTD = values2['-QTD2-']
            sg.PopupOKCancel('Confirmar Cadastro?')
        
            if NAME != '':
                database.write(ID, NAME, QTD)
                window2.find_element('-NAME2-').update('')
                window2.find_element('-QTD2-').update('')
                sg.SystemTray.notify('Notification Title', 'This is the notification message')
        
        if event2 == ('Listar'):
            ID, NAME = database.read_data() 
            window2.find_element('-BOX2-').update(ID, NAME)
            #window2.find_element('-BOX2-').update('{}'.format(ID), '{}'.format(NAME))
            #window.find_element('-NAME-').update(NAME)
            #window.find_element('-ID-').update(ID)


    #modalProd()


def modalVendas():
    sg.change_look_and_feel('Tan Blue')

    frame_layout = [
                  [sg.T('----'*5)],                  
                  [sg.Text('Código:', size=(5, 1), pad=(5,0)), sg.Input('digite aqui:', size=(20, 1), pad=(5,0)), sg.Text('Fornecedor:', size=(9, 1), pad=(0,0)), sg.Input('digite aqui:',size=(20, 1), pad=(0,0)), sg.Button('OK', size=(3,0), key='-PESQ-'), sg.Button('Limpar', size=(5,0), key='-CLEAR-')],
                  [sg.Text('Produto:',size=(63, 0), pad=(5,0), background_color='grey')],
                  [sg.InputCombo(('Produtos', 'Vendas', 'Entradas', 'Clientes'),pad=(5,0), size=(70, 30)),  sg.FileSaveAs('Exportar Base de \n Dados (Excel)', tooltip=('Exportar Base de \n Dados (Excel)'), size=(15,0), key='-EXCEL-')],
               ]  
    
    layout3 = [
    [sg.Text('Cadastro de Vendas', text_color='grey', pad=(0,0), size=(80,1), font=("Helvetica",20),background_color='blue')],
    [sg.Text('Nome:',size=(5,0)),sg.InputText(size =(15,0),key='-NAME3-')],
    [sg.Button('Enviar Dados', pad=(3,5)), sg.Button('Listar', pad=(10,5))],
    [sg.Frame('', frame_layout, size=(100,0), pad=(5,5), font='Any 12', title_color='White')],
    #[sg.Text('Cadastro de Vendas', text_color='White', blackground_color='blue', size=(20, 1)], justification='left', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    #[sg.Text('Código',size=(5,0)),sg.Input(size=(15,0),key='-CODIGO-')],
    [sg.Listbox('', size=(140,13), key='-BOX3-')],
    [sg.Button('Sair')],
    
    ]

    window3 = sg.Window('Window 3', size=(1100,630)).layout(layout3)
    window3.Finalize()
    window3.TKroot.transient()
    window3.TKroot.grab_set()
    window3.TKroot.focus_force()

    while True:
        event3, values3 = window3.Read()
        if event3 == sg.WIN_CLOSED:
            window3.close()
            break  
        if event3 == ('Sair'):
            window3.close()
            break
              
        if event3 == ('Enviar Dados'):
            sg.PopupOKCancel('Confirmar Cadastro?')
            ID = randint(1, 999)
            NAME = values3['-NAME3-'].capitalize()
        
            if NAME != '':
                database.write(ID, NAME)
                window3.find_element('-NAME3-').update('')
        
        if event3 == ('Listar'):
            ID, NAME = database.read_data() 
            window3.find_element('-BOX3-').update(ID, NAME)

    #modalVendas()


def modalForn():
    sg.change_look_and_feel('Tan Blue')
    
    layout4 = [

    [sg.Text('Nome:',size=(5,0)),sg.InputText(size =(15,0),key='-NAME-')],
    [sg.Button('Enviar Dados'), sg.Button('Listar')],
    [sg.Listbox('', size=(80,10), key='-BOX-')],
    [sg.Button('Sair')],
    
    ]

    window4 = sg.Window('Window 4', layout4)
    window4.Finalize()
    window4.TKroot.transient()
    window4.TKroot.grab_set()
    window4.TKroot.focus_force()

    while True:
        event4, values4 = window4.Read()
        if event4 == sg.WIN_CLOSED:
            window4.close()
            break  
        if event4 in [None,'Sair']:
            window4.close()
              
        if event4 == ('Enviar Dados'):
            sg.PopupOKCancel('Confirmar Cadastro?')
            ID = randint(1, 999)
            NAME = values4['-NAME-'].capitalize()
        
            if NAME != '':
                database.write(ID, NAME)
                window4.find_element('-NAME-').update('')
        
        if event4 == ('Listar'):
            NAME = database.read_data() 
            window4.find_element('-BOX-').update(NAME)
         
    #modalForn()



def modalClientes():
    sg.change_look_and_feel('Tan Blue')
    
    layout5 = [

    [sg.Text('Nome:',size=(5,0)),sg.InputText(size =(15,0),key='-NAME-')],
    #[sg.Text('Código',size=(5,0)),sg.Input(size=(15,0),key='-CODIGO-')],
    [sg.Button('Enviar Dados'), sg.Button('Listar')],
    [sg.Listbox('', size=(80,10), key='-BOX-')],
    [sg.Button('Sair')],
    
    ]

    window5 = sg.Window('Window 5', layout5)
    window5.Finalize()
    window5.TKroot.transient()
    window5.TKroot.grab_set()
    window5.TKroot.focus_force()

    while True:
        event5, values5 = window5.Read()
        if event5 == sg.WIN_CLOSED:
            window5.close()
            break  
        if event5 in [None,'Sair']:
            window5.close()
              
        if event5 == ('Enviar Dados'):
            sg.PopupOKCancel('Confirmar Cadastro?')
            ID = randint(1, 999)
            NAME = values5['-NAME-'].capitalize()
        
            if NAME != '':
                database.write(ID, NAME)
                window5.find_element('-NAME-').update('')
        
        if event5 == ('Listar'):
            NAME = database.read_data() 
            window5.find_element('-BOX-').update(NAME)

        #modalClientes()



def modalUpDel(event):
    sg.change_look_and_feel('Tan Blue')
    
    layout7 = [

    [sg.Text('Nome:',size=(5,0)),sg.InputText(size =(15,0),key='-NAME-')],
    #[sg.Text('Código',size=(5,0)),sg.Input(size=(15,0),key='-CODIGO-')],
    [sg.Button('Enviar Dados'), sg.Button('Listar')],
    [sg.Listbox('', size=(80,10), key='-BOX-')],
    [sg.Button('Sair')],
    
    ]

    window7 = sg.Window('Window 7', layout7)
    window7.Finalize()
    window7.TKroot.transient()
    window7.TKroot.grab_set()
    window7.TKroot.focus_force()

    ID, NAME = event
    while True:
        window7.find_element('-ID-').update(ID)
        window7.find_element('-NAME-').update(NAME)
         
        event7, values7 = window7.Read()
        if event7 == sg.WIN_CLOSED:
            window7.close()
            break  
        if event7 in [None,'Sair']:
            window7.close()
              
        if event7 == ('Enviar Dados'):
            sg.PopupOKCancel('Confirmar Cadastro?')
            ID = randint(1, 999)
            NAME = values7['-NAME-'].capitalize()
        
            if NAME != '':
                database.write(ID, NAME)
                window7.find_element('-NAME-').update('')
        
        if event7 == ('Listar'):
            NAME = database.read_data() 
            window7.find_element('-BOX-').update(NAME)

    #modalUpDel()



        

   

