import PySimpleGUI as sg
import os.path

sg.theme('DarkBlue16')

picture_view_column = [
    [
        sg.Text("In progress, picture viewer"),
    ]
]

menu_selection_column = [
    [
        sg.Combo(['Background', 'Mikazuki Villa Day'])
    ],
    [
        sg.Combo(['Character', 'Iroha', 'Yachiyo', 'Kagome'])
    ]
]

JSON_view_row = [
    [
        sg.Text("In progress, JSON viewer")
    ]
]

layout = [
    [
       [
        sg.Column(picture_view_column),
        sg.VerticalSeparator(),
        sg.Column(menu_selection_column)
       ],
        [sg.HorizontalSeparator(),],
        [sg.Text("In progress, JSON viewer")]
    ]
]

window = sg.Window("Magia Record JSON Creator", layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()