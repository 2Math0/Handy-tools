import PySimpleGUI as sg
import delete_pages


if __name__ == "__main__" : 
    # Define the window's contents
    layout = [
        #ask for pdf path
        [sg.Text("PDF path")],
        [sg.Input(key='path')],

        # deleting pages
        [sg.Text('For pages you only want and delete the rest'), sg.Input(key='delete pages')],
        [sg.Text(text='Note: seperate pages with commas(,) with no spaces',text_color='#acacac')],
        [sg.Text(key='deleting pages is done')],

        #Buttons Action
        [sg.Button('Ok'), sg.Button('Quit')]

        ]

    # Create the window
    window = sg.Window('PDF Manipulator', layout)

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        # Output a message to the window
        if window['delete pages'].get() != '':
            dp = delete_pages.DeletePages()
            dp.delete_pages(window['path'].get(), dp.pages_to_list(window['delete pages'].get(), ','))
            print(window['path'].get())
            window['deleting pages is done'].update('Pages are deleted and new pdf was saved in the same directory with name')

    # Finish up by removing from the screen
    window.close()