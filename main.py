# Author: Noëlle Barron
# For help, contact me at william.c.b.19@gmail.com

import PySimpleGUI as gui
import webbrowser 

gui.theme("DarkBlue")

class GodStats:
    attempt_count = 0.0
    success_count = 0.0
    success_rate = 0.0

    def __init__(self, name):
        self.name = name

    def update_success_rate(self):
        if self.attempt_count != 0.0:
            self.success_rate = self.success_count / self.attempt_count
        else:
            self.success_rate = 0.0

    def print_stats(self):
        print("Name: %s | Attempts: %d | Successes: %d | Success Rate: %f\n" %
              (self.name, self.attempt_count, self.success_count, self.success_rate))

# yes, literally all of them
gods = ['Vengefly King', 'Gruz Mother', 'False Knight', 'Massive Moss Charger', 'Hornet Protector', 'Gorb',
        'Dung Defender', 'Soul Warrior', 'Brooding Mawlek', 'Brothers Oro and Mato', 'Xero', 'Crystal Guardian',
        'Soul Master', 'Oblobbles', 'Sisters of Battle', 'Marmu', 'Flukemarm', 'Broken Vessel', 'Galien',
        'Paintmaster Sheo', 'Hive Knight', 'Elder Hu', 'The Collector', 'God Tamer', 'Troupe Master Grimm',
        'Watcher Knight', 'Uumuu', 'Winged Nosk', 'Great Nailsage Sly', 'Hornet Sentinel', 'Enraged Guardian',
        'Lost Kin', 'No Eyes', 'Traitor Lord', 'White Defender', 'Soul Tyrant', 'Markoth', 'Grey Prince Zote',
        'Failed Champion', 'Nightmare King Grimm', 'Pure Vessel', 'Absolute Radiance']

poh = []

for god in gods:
    poh.append(GodStats(god))

# filepath, boolean -> boolean
# loads the selected file, replacing the current data or 
# adding onto it depending on the selection of the user
def load_stats(file_path, overwrite):

    while True:
        try:
            all_lines = open(file_path, "r").readlines()
            all_lines.pop(0)
            all_lines.pop(0)

            if overwrite:
                for line in all_lines:
                    split_line = line.strip().split('|')
                    for god in poh:
                        if god.name == split_line[0]:
                            god.attempt_count = float(split_line[1])
                            god.success_count = float(split_line[2])
                            god.success_rate = float(split_line[3])
                return True
            else:
                for line in all_lines:
                    split_line = line.strip().split('|')
                    for god in poh:
                        if god.name == split_line[0]:
                            god.attempt_count += float(split_line[1])
                            god.success_count += float(split_line[2])
                            god.update_success_rate()
                return True
        except OSError:
            return False

# file_path -> None
# saves the current stats into a .txt file
def save_stats(file_path):
    while True:
        try:
            file = open(file_path, "w")
            file.write("Pantheon of Hallownest Progression Data\n")
            file.write("God|Attempts|Successes|Rate of Success\n")
            for god in poh:
                god.update_success_rate()
                file.write("%s|%d|%d|%f\n" % (god.name, god.attempt_count, god.success_count, god.success_rate))

            break
        except OSError:
            print("Invalid path.\n")
            file_path = input("Please try again or enter q to return.: ")
            if file_path == 'q':
                break

# None -> None
# makes all success rate calculation up to date
def update_success_rate():
    for god in poh:
        god.update_success_rate()

# str -> None
# given the name of a boss, updates the data
# to account for dying to them
def add_death(boss):
    for god in poh:
            god.attempt_count += 1
            if god.name != boss:
                god.success_count += 1
            else:
                break

# None -> None
# used to create the table displayed in Display Stats
def get_data():
    data = []
    for god in poh:
        god_data = []
        god_data.append(god.name)
        god_data.append(god.attempt_count)
        god_data.append(god.success_count)
        god_data.append(str(god.success_rate * 100) + '%')
        data.append(god_data)
    return data

# None -> None
# displays the table when the button Display Stats is pressed
def popup_stats():
    update_success_rate()
    headers = ["Boss", "Attempts", "Successes", "Success Rate"]
    data = get_data()
    layout = [
        [gui.Text("Here are your stats!")],
        [gui.Table(values=data,headings=headers)]
    ]
    window = gui.Window("Stats", layout, use_default_focus=False, finalize=True)
    event, values = window.read()
    window.close()
    return None

# None -> Boolean or str
# activates when a .txt file is chosen to be loaded
# creates a window that asks the user if they want to overwrite
# their current data or add the loaded data to it
def overwrite():
    layout = [
        [gui.Text("Would you like the loaded data to integrate your current data?")],
        [gui.Button(button_text='Yes, please keep my current data',key="-YES-",enable_events=True)],
        [gui.Button(button_text='No, overwrite my current data',key='-NO-',enable_events=True)],
        [gui.Button(button_text='Cancel',key='-CANCEL-',enable_events=True)]
    ]
    window = gui.Window("Load", layout, modal=True)
    while True:
        event, values = window.read()
        if event == '-YES-':
            window.close()
            return False
        elif event == '-NO-':
            window.close()
            return True
        elif event == gui.WIN_CLOSED or event == '-CANCEL-':
            window.close()
            return "cancel"

# None -> Boolean
# displays when the button Reset is pressed
# creates a window that asks the user if they are sure
# they want to reset
def confirm_reset():
    layout = [
        [gui.Text("Are you sure you would like to reset current data?",justification='center')],
        [gui.Column([[gui.Button(button_text='Yes',key="-YES-",enable_events=True)]],justification='center')],
        [gui.Column([[gui.Button(button_text='Cancel',key='-CANCEL-',enable_events=True)]],justification='center')]
    ]
    window = gui.Window("Reset", layout, modal=True)
    while True:
        event, values = window.read()
        if event == '-YES-':
            window.close()
            return True
        elif event == '-CANCEL-':
            window.close()
            return False
        elif event == gui.WIN_CLOSED:
            window.close()
            return False

# str -> None
# called when the button Undo is pressed
# given the name of a god, removes a death to that
# god
def undo(slayer):
    for god in poh:
        if god.name == slayer:
            god.attempt_count = god.attempt_count - 1
            break
        god.attempt_count = god.attempt_count - 1
        god.success_count = god.success_count - 1
    update_success_rate()

# None -> None
# called when a Reset is confirmed
def reset():
    for god in poh:
        god.attempt_count = 0.0
        god.success_count = 0.0
        god.success_rate = 0.0

# None -> None
# called when the Credits button is pressed
# it's me!
def display_credits():
    layout = [
        [gui.Text("Made by Noëlle Barron",justification='center')],
        [gui.Column([[gui.Button('GitHub',enable_events=True,key='-GITHUB-')]],
        justification='center')]
    ]
    window = gui.Window("Credits", layout, modal=True)
    url = 'https://github.com/chocolatevanille/PantheonofHallownestTracker'
    while True:
        event, values = window.read()
        if event == '-GITHUB-':
            webbrowser.open(url)
        elif event == gui.WIN_CLOSED:
            window.close()
            return None

button_menu_def = ['Boss', gods]

# window's layout design
layout_top = [  [gui.Text("Pantheon of Hallownest Progression Tracker")]]
            
layout_middle_left = [  [gui.Text("Who ended your run?"),
                        gui.ButtonMenu('Bosses',menu_def=button_menu_def,border_width=5, key='-SLAYER-')]]

layout_middle_right = [ [gui.Image(key='-IMAGE-',filename='imgs/The Knight.png',
                        expand_x=True,expand_y=True)]]

layout_bottom = [   [gui.Text('',key='-STATUS-')],
                    gui.Column([[gui.Button('Display Stats')]]),
                    gui.Column([[gui.FileBrowse(button_text='Load',key='-LOAD-',enable_events=True,file_types=(("Text Files", "*.txt"),))]]), 
                    gui.Column([[gui.Input(key='-SAVE-',visible=False,enable_events=True),gui.FileSaveAs(button_text='Save',file_types=(("Text Files", "*.txt"),))]]), 
                    gui.Column([[gui.Button('Reset',key='-RESET-')]]),
                    gui.Column([[gui.Button('Undo',key='-UNDO-')]]),
                    gui.Column([[gui.Button('Credits',key='-CREDITS-')]]),
                    gui.Column([[gui.Button('Close',key='-CLOSE-')]])]

layout = [
    [   
        layout_top,
        gui.Column(layout_middle_left),
        gui.VSeparator(),
        gui.Column(layout_middle_right),
        layout_bottom
    ]
]

# window creation
window = gui.Window('PoH Tracker', layout,size=(750,540),element_justification='center')

# event loop
def win_run():
    last_update = []
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED or event == '-CLOSE-':
            break
        elif event == '-SLAYER-':
            selection = values[event]
            if selection:
                add_death(selection)
                last_update.append(selection)
                image_name = 'imgs/' + selection + '.png'
                window['-IMAGE-'].update(image_name)
        elif event == 'Display Stats':
            window['-STATUS-'].update('Stats displayed.')
            popup_stats()
            continue
        elif event == '-LOAD-':
            path = values['-LOAD-']
            keep = overwrite()
            if keep != "cancel":
                success = load_stats(path, keep)
                if success:
                    window['-STATUS-'].update('Data loaded.')
                else:
                    window['-STATUS-'].update('Data failed to load.')
            else:
                window['-STATUS-'].update('Data not loaded.')
            continue
        elif event == '-SAVE-':
            path = values['-SAVE-']
            save_stats(path)
            continue
        elif event == '-UNDO-':
            if len(last_update) > 0:
                curr = last_update.pop()
                undo(curr)
                window['-STATUS-'].update('Removed death to ' + curr + '.')
                image_name = ''
                if len(last_update) > 0:
                    image_name = 'imgs/' + last_update[-1] + '.png'
                else:
                    image_name = 'imgs/The Knight.png'
                window['-IMAGE-'].update(image_name)
            else:
                window['-STATUS-'].update('Cannot undo. No further history.')
        elif event == '-RESET-':
            confirm = confirm_reset()
            if confirm:
                reset()
                window['-STATUS-'].update('All data reset to 0.')
            else:
                window['-STATUS-'].update('Reset canceled.')
            continue
        elif event == '-CREDITS-':
            window['-STATUS-'].update('Reset canceled.')
            display_credits()
            continue
    window.close()


def main():
    print()
    win_run()


if __name__ == "__main__":
    main()
