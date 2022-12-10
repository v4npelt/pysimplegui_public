import PySimpleGUI as sg

# Modal window design pattern

layout = [[ sg.Text('Window 1'),],
          [sg.Input(do_not_clear=True)],
          [sg.Text('',size=(39,2), key='_OUTPUT_')],
          [sg.Button('Launch 2')]]

win1 = sg.Window('Window 1',layout)
while True:
    ev1, vals1 = win1.Read(timeout=100)
    if ev1 is None:
        break
    win1.FindElement('_OUTPUT_').Update(vals1[0])

    if ev1 == 'Launch 2':
        layout2 = [[sg.Text('Window 2')],       # note must create a layout from scratch every time. No reuse
                   [sg.Button('Exit')]]

        win2 = sg.Window('Window 2', layout2)
        win2.Finalize()
        win2.TKroot.transient()
        win2.TKroot.grab_set()
        win2.TKroot.focus_force()
        while True:
            ev2, vals2 = win2.Read()
            if ev2 in [None,'Exit']:
                win2.Close()
                break