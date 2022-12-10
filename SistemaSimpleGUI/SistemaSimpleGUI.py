import PySimpleGUI as sg
from random import randint
import database 
from modais import *
import pandas as pd 


WIN_W=70
WIN_H=40


#ID = ''
#NAME = database.read_data()
#front()
class TelaPython:
    def __init__(self):
        #sg.change_look_and_feel('Random')
        sg.change_look_and_feel('DarkTanBlue')
        #layout
     
        #[sg.Image(r'C:\PySimpleGUI\Logos\PySimpleGUI_Logo_320.png')],
        #[sg.Image('image/bank.png')],
      
        #frame_logo = [
        #         [sg.Image('images/logo.png', size=(100,100))],
        #         [sg.T('Text inside of a frame')],
        #         [sg.CB('Check 1'), sg.CB('Check 2')],
        #            
        #      ]

        frame_layout = [
                  [sg.T('')],                
                  [sg.Button('Produtos', size=(13,0)), sg.Button('+', size=(3,0), key='-CADPROD-'), sg.Button('Vendas', size=(13,0)), sg.Button('+', size=(3,0), key='-CADVEND-')],
                  [sg.Button('Entradas', size=(13,0)), sg.Button('+', size=(3,0), key='-CADENTRA-'), sg.Button('Clientes', size=(13,0)), sg.Button('+', size=(3,0), key='-CADCLIE-')],
               ]
        
        frame_layout2 = [
                  [sg.T('----'*5)],                  
                  [sg.Text('Termo de Pesquisa:',size=(15, 1)), sg.Input('digite aqui:',size=(42, 1)), sg.Button('OK', size=(3,0), key='-PESQ-'), sg.Button('Limpar', size=(5,0), key='-CLEAR-')],
                  [sg.Text('Base de Dados:',size=(15, 1)), sg.InputCombo(('Produtos', 'Vendas', 'Entradas', 'Clientes'), size=(40, 10), key='-COMBO-'),  sg.FileSaveAs('Exportar Base de \n Dados (Excel)', file_types=(("All Files", "*.*"),), default_extension='excel' , tooltip=('Exportar Base de \n Dados (Excel)'), size=(15,0), key='-EXCEL-')],
               ]
        frame_layout3 = [
                  [sg.T('----'*5)],                  
                  [sg.Button('Estoque Menor ou \n Igual a:', size=(20,0), key='-MAIOR_MENOR-')],
                  [sg.Input('', size=(23,0), key='-QTDE-')],
                  [sg.Button('Total Vendido', size=(20,0), key='-TOT_VEND-')],
                ]
        layout = [
            [sg.Text('',size=(10,0))],
            [sg.Text('',size=(10,0)), sg.Text('',size=(10,0)), sg.Text('CONTROLE VENDAS PYTHON!',text_color='White', size=(50, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
            [sg.Image('images/logo3.png', pad=(5,15))],
            #[sg.Frame('My Frame logo', frame_logo, pad=(25,20), background_color='yellow', font='Any 12', title_color='White')],
      
            [sg.Button('Relatórios',font='Any 15', pad=(25,0), size=(15,1)), sg.VerticalSeparator(pad=None), 
            sg.Button('Livro Caixa',font='Any 15', pad=(25,0), size=(15,1)), 
            sg.Button('', button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='images/caixa4.png', image_size=(43, 43), image_subsample=3, border_width=2, size=(6,8), tooltip='Operações de Caixa', key='-REGCAIXA-'),
            sg.Text('',size=(10,0)),sg.Text('',size=(10,0)),sg.Text('',size=(10,0)),sg.Text('',size=(10,0)),sg.Text('',size=(10,0)),
            sg.SaveAs('Relatório Contábil', tooltip=('Relatório Contábil'), font='Any 15',pad=(25,0), size=(15,1), key='-REL_CONT-')],
            [sg.Text('-'*296,size=(1000,0), pad=(25,0))], 
            [sg.Text('Tipo de Venda:',text_color='Black', background_color='grey', size=(15, 0), pad=(25,0), justification='center', font=("Helvetica", 13), relief=sg.RELIEF_RIDGE), sg.Input('', size=(144,0))],
            [sg.Frame('My Frame Title', frame_layout, pad=(25,0), font='Any 12', title_color='White'), sg.Frame('My Frame Title', frame_layout2, pad=(25,0), font='Any 12', title_color='White'), sg.Frame('My Frame Title', frame_layout3, pad=(25,0), font='Any 12', title_color='White')],  
            [sg.Text('...',size=(5,0), pad=(25,0))], 

            #[sg.Output(size=(167,20), pad=(25,0), key='-BOX-')],
            #[sg.HorizontalSeparator(pad=None)],
            
            [sg.Table(size=(1200,20), pad=(25,0), key='-TB-', values=[['SD'], ["DSVSDV"], ['wefwe']], headings=[["codigo"],["nome"],["qtd"]],
            col_widths=[10], auto_size_columns=False, enable_events=True, justification='left') ],
      
      
            ]
        # Janela Inicial
        self.janela = sg.Window("Dados do Usuário", location=(0,0), size=(1350,700), resizable=True).layout(layout)
    
 
    def Iniciar(self):
        while True:
            button, values = self.janela.Read()
            if values == sg.WIN_CLOSED:
                self.janela.close()
                break 

            #%%%%%%%%%%% PRODUTOS %%%%%%%%%%%%%
            if button == 'Produtos':
                DATA = database.read_data()
                #for items in DATA:
                #self.janela.find_element('-BOX-').update(DATA)
                self.janela.find_element('-TB-').update(DATA)
                print(DATA)
                
        
            if button == ('-CADPROD-'):
                modalProd()
                

            #%%%%%%%%%%% EVENTS %%%%%%%%%%%%%%
            #event = self.janela.find_element('-TB-').get()

            if button == ('-MAIOR_MENOR-'):
                ver =  values['-QTDE-']
                data = database.read_data()    
                for items in data:
                #    for qtd in items[2]:
                #        if qtd <= int(ver):
                    if int(ver) >= int(items[2]):
                        self.janela.find_element('-TB-').update(items)
                        print(items)
                        #return data
            
            if button == ('-EXCEL-'):
                #excel = self.janela.find_element('-COMBO-').get()
                if values == sg.InputCombo:
                    pass
                #      base = ['produtos', 'vendas' ,'entradas', 'clientes']
                # value = base[excel]
                # *args = database.read_data(value)
                # with open('archive.xlsx', 'w') as f_obj:
                #     result = f_obj.write(*args)
                #     planilha = pd.read_excel(result)   
                #     planilha.to_excel(pandas.xlsx)  

                #planilha = pd.read_excel('excel')                 

            #%%%%%%%%%%% VENDAS %%%%%%%%%%%%%%%%%
            if button == 'Vendas':
                ID, NAME = database.read_data()
                print(ID, NAME)
                self.janela.find_element('-TB-').update(ID, NAME)

            if button == ('-CADVEND-'):
                modalVendas()

            #%%%%%%%%%%% FORNECEDOR %%%%%%%%%%%%%%
            if button == 'Fornecedor':
                ID, NAME = database.read_data()
                print(ID, NAME)
                self.janela.find_element('-TB-').update(ID, NAME)

            if button == ('-CADENTRA-'):
                modalForn()

                
            #%%%%%%%%%%% CLIENTES %%%%%%%%%%%
            if button == 'Clientes':
                ID, NAME = database.read_data()
                print(ID, NAME)
                self.janela.find_element('-TB-').update(ID, NAME)

            if button == ('-CADCLIE-'):
                modalClientes()
                

            #%%%%%%%%%%% UP/DEL %%%%%%%%%%%
            if button == ('Editar'):
                modalUpDel()
     
         
              

  
tela = TelaPython()
tela.Iniciar() 


#if __name__ == '__main__':
#    sg.theme('DarkAmber')
#    main()



 

# TEMAS PARA TELA 

#SystemDefault
#Reddit
#Topanga
#GreenTan
#Dark
#LightGreen
#Dark2
#Black
#Tan
#TanBlue
#DarkTanBlue
#DarkAmber
#DarkBlue
#Reds
#Green
#BluePurple
#Purple
#BlueMono
#GreenMono
#BrownBlue
#BrightColors
#NeutralBlue
#Kayak
#SandyBeach
#TealMono

