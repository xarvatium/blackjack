import PySimpleGUI as sg 

window = sg.Window(title="Blackjack", layout=[[sg.Text("Please select one of the options below:")], [sg.Button("Singleplayer")], [sg.Button("Multiplayer")], [sg.Button("Quit")]], margins=(100, 50))
def singleWindow():
    single_window = sg.Window(title="Singleplayer", layout=[[sg.Text("Singleplayer")]])
    return

while True:
    event, values = window.read()
    if event == "Quit" or event == sg.WIN_CLOSED:
        break
    elif event == "Singleplayer":
        single_window = sg.Window(title="Singleplayer", layout=[[sg.Text("Singleplayer")]])

window.close()