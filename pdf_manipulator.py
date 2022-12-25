import PySimpleGUI as sg
import fitz



# deleting pages
def pages_to_list(string, seprator):
    if seprator not in string:
        return [int(string)-1]

    #this will make list of numbers
    #int(x) parse each element as int
    #lambda x: int(x) - 1 will make each page number translated into list indexes
    return list(map(lambda x: int(x) - 1, string.split(seprator)))

def delete_pages(path, cutted_pages):
    sys_director = '/' if '/' in path else '\\'
    path_in_sys = path.split(sys_director)[0:-1]
    pdf_name = path.split(sys_director)[-1].split('.')[0]
    #new pdf name
    path_in_sys.append('%s cutted.pdf'%pdf_name)

    f = fitz.open(path)
    f.select(cutted_pages)
    f.save(sys_director.join(path_in_sys))


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
        delete_pages(window['path'].get(), pages_to_list(window['delete pages'].get(), ','))
        print(window['path'].get())
        window['deleting pages is done'].update('Pages are deleted and new pdf was saved in the same directory with name')

# Finish up by removing from the screen
window.close()