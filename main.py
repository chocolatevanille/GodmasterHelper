# Author: Noëlle Barron
# For help, contact me at william.c.b.19@gmail.com

import PySimpleGUI as gui
import webbrowser 
import re

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

class HogStats:
    badge = 'badges/no_badge_s.png'

    def __init__(self,name):
        self.name = name

    def print_stats(self):
        print("Name: %s | Badge: %s\n" %
              (self.name, self.badge))

# list of pantheons
pantheons_names = [ 'Pantheon of the Master', 'Pantheon of the Artist', 'Pantheon of the Sage', 
                    'Pantheon of the Knight',  'Pantheon of Hallownest']

# gods in each pantheon
# yes, literally all of them
poh_gods = ['Vengefly King', 'Gruz Mother', 'False Knight', 'Massive Moss Charger', 'Hornet Protector', 'Gorb',
        'Dung Defender', 'Soul Warrior', 'Brooding Mawlek', 'Brothers Oro and Mato', 'Xero', 'Crystal Guardian',
        'Soul Master', 'Oblobbles', 'Sisters of Battle', 'Marmu', 'Flukemarm', 'Broken Vessel', 'Galien',
        'Paintmaster Sheo', 'Hive Knight', 'Elder Hu', 'The Collector', 'God Tamer', 'Troupe Master Grimm',
        'Watcher Knight', 'Uumuu', 'Winged Nosk', 'Great Nailsage Sly', 'Hornet Sentinel', 'Enraged Guardian',
        'Lost Kin', 'No Eyes', 'Traitor Lord', 'White Defender', 'Soul Tyrant', 'Markoth', 'Grey Prince Zote',
        'Failed Champion', 'Nightmare King Grimm', 'Pure Vessel', 'Absolute Radiance']

potk_gods = ['Enraged Guardian', 'Lost Kin', 'No Eyes', 'Traitor Lord', 'White Defender', 'Failed Champion',
        'Markoth', 'Watcher Knight', 'Soul Tyrant', 'Pure Vessel']

pots_gods = ['Hive Knight', 'Elder Hu', 'The Collector', 'God Tamer', 'Troupe Master Grimm', 'Galien', 
        'Grey Prince Zote', 'Uumuu', 'Hornet Sentinel', 'Great Nailsage Sly']

pota_gods = ['Xero', 'Crystal Guardian', 'Soul Master', 'Oblobbles', 'Mantis Lords', 'Marmu', 'Nosk', 'Flukemarm',
        'Broken Vessel', 'Paintmaster Sheo']

potm_gods = ['Vengefly King', 'Gruz Mother', 'False Knight', 'Massive Moss Charger', 'Hornet Protector', 'Gorb', 
        'Dung Defender', 'Soul Warrior', 'Brooding Mawlek', 'Brothers Oro and Mato']

poh = []
potk = []
pots = []
pota = []
potm = []

# initialize lists of gods with classes
for god in poh_gods:
    poh.append(GodStats(god))
for god in potk_gods:
    potk.append(GodStats(god))
for god in pots_gods:
    pots.append(GodStats(god))
for god in pota_gods:
    pota.append(GodStats(god))
for god in potm_gods:
    potm.append(GodStats(god))

pantheons_data = [potm,pota,pots,potk,poh]

# gods in Hall of Gods
hog_gods = ['Gruz Mother', 'Vengefly King', 'Brooding Mawlek', 'False Knight', 'Failed Champion',
            'Hornet Protector', 'Hornet Sentinel', 'Massive Moss Charger', 'Flukemarm', 'Mantis Lords',
            'Sisters of Battle', 'Oblobble', 'Hive Knight', 'Broken Vessel', 'Lost Kin', 'Nosk',
            'Winged Nosk', 'The Collector', 'God Tamer', 'Crystal Guardian', 'Enraged Guardian', 'Uumuu',
            'Traitor Lord', 'Grey Prince Zote', 'Soul Warrior', 'Soul Master', 'Soul Tyrant',
            'Dung Defender', 'White Defender', 'Watcher Knight', 'No Eyes', 'Marmu', 'Galien',
            'Markoth', 'Xero', 'Gorb', 'Elder Hu', 'Oro and Mato', 'Paintmaster Sheo', 'Nailsage Sly',
            'Pure Vessel', 'Grimm', 'Nightmare King', 'Radiance']

hog = []

# initialize Hall of Gods data
for god in hog_gods:
    hog.append(HogStats(god))

hog_keys = []

# create list of keys for Hall of Gods gods
for god in hog_gods:
    god_key = god.upper()
    god_key = re.sub(r' ','-',god_key)
    god_key = '-' + god_key + '-'
    hog_keys.append(god_key)


# filepath, boolean -> boolean
# loads the selected file, replacing the current data or 
# adding onto it depending on the selection of the user
def load_stats(file_path, overwrite):

    while True:
        try:
            all_lines = open(file_path, "r").readlines()
            all_lines.pop(0)
            all_lines.pop(0)

            curr = poh
            for line in all_lines:
                split_line = line.strip().split('|')
                if 'Pantheon of the Master' in split_line[0]:
                    curr = potm
                    continue
                elif 'Pantheon of the Sage' in split_line[0]:
                    curr = pots
                    continue
                elif 'Pantheon of the Artist' in split_line[0]:
                    curr = pota
                    continue
                elif 'Pantheon of the Knight' in split_line[0]:
                    curr = potk
                    continue
                elif 'Hall of Gods' in split_line[0]:
                    curr = hog
                    continue
                if curr != hog:
                    for god in curr:
                        if god.name == split_line[0]:
                            if overwrite:
                                god.attempt_count = float(split_line[1])
                                god.success_count = float(split_line[2])
                                god.success_rate = float(split_line[3])
                                continue
                            else:
                                god.attempt_count += float(split_line[1])
                                god.success_count += float(split_line[2])
                                god.update_success_rate()
                elif curr == hog and overwrite:
                    for god in hog:
                        if god.name == split_line[0]:
                            god.badge = str(split_line[1])
                            continue
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
            file.write("Pantheon of the Master Progression Data\n")
            file.write("God|Attempts|Successes|Rate of Success\n")
            for god in potm:
                god.update_success_rate()
                file.write("%s|%d|%d|%f\n" % (god.name, god.attempt_count, god.success_count, god.success_rate))
            file.write("Pantheon of the Artist Progression Data\n")
            file.write("God|Attempts|Successes|Rate of Success\n")
            for god in pota:
                god.update_success_rate()
                file.write("%s|%d|%d|%f\n" % (god.name, god.attempt_count, god.success_count, god.success_rate))
            file.write("Pantheon of the Sage Progression Data\n")
            file.write("God|Attempts|Successes|Rate of Success\n")
            for god in pots:
                god.update_success_rate()
                file.write("%s|%d|%d|%f\n" % (god.name, god.attempt_count, god.success_count, god.success_rate))
            file.write("Pantheon of the Knight Progression Data\n")
            file.write("God|Attempts|Successes|Rate of Success\n")
            for god in potk:
                god.update_success_rate()
                file.write("%s|%d|%d|%f\n" % (god.name, god.attempt_count, god.success_count, god.success_rate))
            file.write("Hall of Gods Progression Data\n")
            file.write("God|Badge\n")
            for god in hog:
                file.write("%s|%s\n" % (god.name, god.badge))
            break
        except OSError:
            print("Invalid path.\n")
            file_path = input("Please try again or enter q to return.: ")
            if file_path == 'q':
                break

# str -> lst of GodStats elements
# given the name of a pantheon, return its data array
def get_pantheon_data(curr_pantheon):
    return pantheons_data[pantheons_names.index(curr_pantheon)]

# None -> None
# makes all success rate calculation up to date
def update_success_rate(curr_pantheon):
    gods = get_pantheon_data(curr_pantheon)
    for god in gods:
        god.update_success_rate()

# str -> None
# given the name of a boss, updates the data
# to account for dying to them
def add_death(boss,curr_pantheon):
    gods = get_pantheon_data(curr_pantheon)
    for god in gods:
            god.attempt_count += 1
            if god.name != boss:
                god.success_count += 1
            else:
                break

# None -> None
# used to create the table displayed in Display Stats
def get_data(curr_pantheon):
    data = []
    gods = get_pantheon_data(curr_pantheon)
    for god in gods:
        god_data = []
        god_data.append(god.name)
        god_data.append(god.attempt_count)
        god_data.append(god.success_count)
        god_data.append(str(god.success_rate * 100) + '%')
        data.append(god_data)
    return data

# None -> None
# displays the table when the button Display Stats is pressed
def popup_stats(curr_pantheon):
    update_success_rate(curr_pantheon)
    headers = ["Boss", "Attempts", "Successes", "Success Rate"]
    data = get_data(curr_pantheon)
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
        [gui.Text("Would you like the loaded data to integrate your current data?", justification='center')],
        [gui.Column([[gui.Button(button_text='Yes, please keep my current data',key="-YES-",enable_events=True)]],justification='center')],
        [gui.Column([[gui.Button(button_text='No, overwrite my current data',key='-NO-',enable_events=True)]],justification='center')],
        [gui.Column([[gui.Button(button_text='Cancel',key='-CANCEL-',enable_events=True)]],justification='center')]
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
def undo(slayer,curr_pantheon):
    gods = get_pantheon_data(curr_pantheon)
    for god in gods:
        if god.name == slayer:
            god.attempt_count = god.attempt_count - 1
            break
        god.attempt_count = god.attempt_count - 1
        god.success_count = god.success_count - 1
    update_success_rate(curr_pantheon)

# None -> None
# called when a Reset is confirmed
def reset(curr_pantheon):
    gods = get_pantheon_data(curr_pantheon)
    for god in gods:
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

# str -> str
# given the name of a pantheon, returns the key to its menu button
def get_pantheon_key(pantheon):
    return pantheon_keys[pantheons_names.index(pantheon)]


# str -> str
# given the name of a God, return their badge in Hall of Gods
def get_badge(curr):
    for god in hog:
        if god.name == curr:
            return god.badge

# str -> str
# given the key of a god in hog_keys, return the name of the god
def get_hog_name(god_key):
    return hog_gods[hog_keys.index(god_key)]

# str -> [str,bool]
# given the name of a god, display the three badges for HoG, let
# the user click on the new badge, and update the data in the god's 
# HogStats before returning the new badge and whether the badge was
# changed
def change_badge(curr_god):
    layout = [
        [gui.Button(image_source='badges/attuned.png',key='-ATTUNED-',button_color=gui.TRANSPARENT_BUTTON),
        gui.Button(image_source='badges/ascended.png',key='-ASCENDED-',button_color=gui.TRANSPARENT_BUTTON),
        gui.Button(image_source='badges/radiant.png',key='-RADIANT-',button_color=gui.TRANSPARENT_BUTTON)]
    ]
    window = gui.Window("Choose new completion status",layout,size=(240,100),element_justification='center',margins=(6,20))
    while True:
        event, values = window.read()
        changed = False
        if event == gui.WIN_CLOSED: # when window closes
            break
        elif event == '-ATTUNED-':
            for god in hog:
                if god.name == curr_god:
                    check = god.badge
                    god.badge = 'badges/attuned_s.png'
                    if check != god.badge:
                        changed = True
                    break
            window.close()
            return ['badges/attuned_s.png',changed]
        elif event == '-ASCENDED-':
            for god in hog:
                if god.name == curr_god:
                    check = god.badge
                    god.badge = 'badges/ascended_s.png'
                    if check != god.badge:
                        changed = True
                    break
            window.close()
            return ['badges/ascended_s.png',changed]
        elif event == '-RADIANT-':
            for god in hog:
                if god.name == curr_god:
                    check = god.badge
                    god.badge = 'badges/radiant_s.png'
                    if check != god.badge:
                        changed = True
                    break
            window.close()
            return ['badges/radiant_s.png',changed]
    window.close()
    return ['',False]

# Hall of Gods display
# called when user clicks on Hall of Gods button
def display_HoG():
    boss_names = [
            ['Gruz Mother', 'Vengefly King', 'Brooding Mawlek', 'False Knight', 'Failed Champion', 'Hornet Protector', 'Hornet Sentinel', 'Massive Moss Charger', 'Flukemarm', 'Mantis Lords', 'Sisters of Battle'],
            ['Oblobble', 'Hive Knight', 'Broken Vessel', 'Lost Kin', 'Nosk', 'Winged Nosk', 'The Collector', 'God Tamer', 'Crystal Guardian', 'Enraged Guardian', 'Uumuu'],
            ['Traitor Lord', 'Grey Prince Zote', 'Soul Warrior', 'Soul Master', 'Soul Tyrant', 'Dung Defender', 'White Defender', 'Watcher Knight', 'No Eyes', 'Marmu', 'Galien'],
            ['Markoth', 'Xero', 'Gorb', 'Elder Hu', 'Oro and Mato', 'Paintmaster Sheo', 'Nailsage Sly', 'Pure Vessel', 'Grimm', 'Nightmare King', 'Radiance']
        ]
        
    layout = [
        [gui.Text('Hall of Gods')],
        [gui.Text('', key='-STATUS-')],
    ]
    
    for column_bosses in boss_names:
        column_layout = [
            [gui.Button(image_source=get_badge(boss), key=f'-{boss.replace(" ", "-").upper()}-', button_color=gui.TRANSPARENT_BUTTON), gui.Text(boss)]
            for boss in column_bosses
        ]
        layout.append(gui.Column(column_layout, justification='left'))
    window = gui.Window('Hall of Gods',layout,size=(700,480),element_justification='center')
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED: # when window closes
            break
        elif event in hog_keys:
            curr_god = get_hog_name(event)
            new_badge = change_badge(curr_god)
            if new_badge[0] != '':
                window[event].update(image_filename=new_badge[0])
            if new_badge[1]:
                window['-STATUS-'].update('Updated status of ' + curr_god)
    window.close()

poh_menu_def = ['Boss', poh_gods]
potk_menu_def = ['Boss', potk_gods]
potm_menu_def = ['Boss', potm_gods]
pota_menu_def = ['Boss', pota_gods]
pots_menu_def = ['Boss', pots_gods]
pantheon_menu_def = ['Pantheon', pantheons_names]
pantheon_keys = ['-POTM-SLAYER-','-POTA-SLAYER-','-POTS-SLAYER-','-POTK-SLAYER-','-POH-SLAYER-']

# generate new layout

# window's layout design
layout_top = [  [gui.Text("Pantheon of Hallownest Progression Tracker")]]
            
layout_middle_left = [  [gui.Text("Who ended your run?"),
                        gui.ButtonMenu('Bosses',menu_def=poh_menu_def,border_width=5,key='-POH-SLAYER-',visible=True),
                        gui.ButtonMenu('Bosses',menu_def=potk_menu_def,border_width=5,key='-POTK-SLAYER-',visible=False),
                        gui.ButtonMenu('Bosses',menu_def=pota_menu_def,border_width=5,key='-POTA-SLAYER-',visible=False),
                        gui.ButtonMenu('Bosses',menu_def=potm_menu_def,border_width=5,key='-POTM-SLAYER-',visible=False),
                        gui.ButtonMenu('Bosses',menu_def=pots_menu_def,border_width=5,key='-POTS-SLAYER-',visible=False)],
]

layout_middle_right = [ [gui.Image(key='-IMAGE-',filename='imgs/The Knight.png',
                        expand_x=True,expand_y=True)]]

layout_bottom = [   [gui.Text('',key='-STATUS-')],
                    gui.Column([[gui.Button('Display Stats')]]),
                    gui.Column([[gui.Button('Hall of Gods',key='-HALL-OF-GODS-')]]),
                    gui.Column([[gui.FileBrowse(button_text='Load',key='-LOAD-',enable_events=True,file_types=(("Text Files", "*.txt"),))]]), 
                    gui.Column([[gui.Input(key='-SAVE-',visible=False,enable_events=True),gui.FileSaveAs(button_text='Save',file_types=(("Text Files", "*.txt"),))]]), 
                    gui.Column([[gui.Button('Reset',key='-RESET-')]]),
                    gui.Column([[gui.Button('Undo',key='-UNDO-')]]),
                    gui.Column([[gui.Button('Credits',key='-CREDITS-')]]),
                    gui.Column([[gui.Button('Close',key='-CLOSE-')]])
]

layout_pantheon = [ [gui.Text('Current pantheon: Pantheon of Hallownest',key='-CURRENT-PANTHEON-'),
                    gui.ButtonMenu('Pantheons',menu_def=pantheon_menu_def,border_width=5, key='-PANTHEON-')]
]

layout = [
    [   
        layout_top,
        gui.Column(layout_middle_left),
        gui.VSeparator(),
        gui.Column(layout_middle_right),
        layout_bottom,
        layout_pantheon
    ]
]
# problem: can't get layout_bottom to appear at the bottom for some painful reason

# window creation
window = gui.Window('PoH Tracker', layout,size=(750,540),element_justification='center')

# event loop
def win_run():
    # active pantheon
    # default to Pantheon of Hallownest
    active_pantheon = 'Pantheon of Hallownest'
    last_update = []
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED or event == '-CLOSE-': # when window closes
            break
        if event == '-PANTHEON-':
            selection = values[event] # get name of new pantheon
            if selection != active_pantheon:
                act_key = get_pantheon_key(active_pantheon)
                new_key = get_pantheon_key(selection)
                last_update = []
                window[act_key].update(visible=False) # hide curr list of bosses
                window[new_key].update(visible=True)
                window['-CURRENT-PANTHEON-'].update('Current pantheon: ' + selection)
                window['-IMAGE-'].update('imgs/The Knight.png')
                active_pantheon = selection # change current pantheon
                window['-STATUS-'].update('Changed to the ' + selection + '.')
            elif selection == active_pantheon:
                window['-STATUS-'].update('You are already tracking the ' + selection + '.')
        elif event in pantheon_keys: # when user chooses the god who killed them
            selection = values[event] # get name of slayer
            if selection: 
                add_death(selection,active_pantheon) # add death to data
                window['-STATUS-'].update('Death to ' + selection + ' recorded.')
                last_update.append(selection) # record who killed them in queue for undo
                image_name = 'imgs/' + selection + '.png' # display killer >:3
                window['-IMAGE-'].update(image_name)
        elif event == 'Display Stats': # when user displays stats
            window['-STATUS-'].update('Stats displayed.')
            popup_stats(active_pantheon) # display stats in new window
            continue
        elif event == '-HALL-OF-GODS-':
            window['-STATUS-'].update('Hall of Gods displayed.')
            display_HoG()
            continue
        elif event == '-LOAD-': # when user attempts to load data
            path = values['-LOAD-']
            keep = overwrite() # ask if they would like to overwrite their current data
            if keep != "cancel": # if load is not canceled 
                success = load_stats(path, keep) # load data
                if success:
                    window['-STATUS-'].update('Data loaded.')
                else:
                    window['-STATUS-'].update('Data failed to load.')
            else:
                window['-STATUS-'].update('Data not loaded.')
            continue
        elif event == '-SAVE-': # when user attempts to save data
            path = values['-SAVE-']
            save_stats(path) # save data to .txt file
            continue
        elif event == '-UNDO-': # when user wants to undo death recording
            if len(last_update) > 0: # check if there is something to undo
                curr = last_update.pop() # remove most recent recorded death from queue
                undo(curr,active_pantheon) # remove death from data
                window['-STATUS-'].update('Removed death to ' + curr + '.')
                image_name = ''
                if len(last_update) > 0:
                    image_name = 'imgs/' + last_update[-1] + '.png'
                else:
                    image_name = 'imgs/The Knight.png'
                window['-IMAGE-'].update(image_name)
            else:
                window['-STATUS-'].update('Cannot undo. No further history.')
        elif event == '-RESET-': # when user wants to reset all data
            confirm = confirm_reset() # ask them if they are sure
            if confirm:
                reset(active_pantheon) # if sure, reset all data
                window['-STATUS-'].update('All data for ' + active_pantheon + ' reset to 0.')
            else:
                window['-STATUS-'].update('Reset canceled.')
            continue
        elif event == '-CREDITS-': # when the user wants to see who made the program for some reason
            window['-STATUS-'].update('Reset canceled.')
            display_credits() # hey it's me! wait didn't i already do that jo-
            continue
    window.close()


def main():
    print()
    win_run()


if __name__ == "__main__":
    main()
