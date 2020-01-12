# Author: willster191
# For help, contact: willster191 on Reddit or willster#1886 on Discord

class GodStats:
    attempt_count = 0.0
    success_count = 0.0
    success_rate = 0.0

    def __init__(self, name):
        self.name = name

    def UpdateSuccessRate(self):
        if self.attempt_count != 0.0:
            self.success_rate = self.success_count / self.attempt_count

    def PrintStats(self):
        print("Name: %s | Attempts: %d | Successes: %d | Success Rate: %f\n" %
              (self.name, self.attempt_count, self.success_count, self.success_rate))


vengefly_king = GodStats('Vengefly King')
gruz_mother = GodStats('Gruz Mother')
false_knight = GodStats('False Knight')
massive_moss_charger = GodStats('Massive Moss Charger')
hornet_protector = GodStats('Hornet Protector')
gorb = GodStats('Gorb')
dung_defender = GodStats('Dung Defender')
soul_warrior = GodStats('Soul Warrior')
brooding_mawlek = GodStats('Brooding Mawlek')
brothers = GodStats('Brothers Oro and Mato')
xero = GodStats('Xero')
crystal_guardian = GodStats('Crystal Guardian')
soul_master = GodStats('Soul Master')
oblobbles = GodStats('Oblobbles')
sisters_of_battle = GodStats('Sisters of Battle')
marmu = GodStats('Marmu')
flukemarm = GodStats('Flukemarm')
broken_vessel = GodStats('Broken Vessel')
galien = GodStats('Galien')
paintmaster_sheo = GodStats('Paintmaster Sheo')
hive_knight = GodStats('Hive Knight')
elder_hu = GodStats('Elder Hu')
the_collector = GodStats('The Collector')
god_tamer = GodStats('God Tamer')
troupe_master_grimm = GodStats('Troupe Master Grimm')
watcher_knight = GodStats('Watcher Knight')
uumuu = GodStats('Uumuu')
winged_nosk = GodStats('Winged Nosk')
great_nailsage_sly = GodStats('Great Nailsage Sly')
hornet_sentinel = GodStats('Hornet Sentinel')
enraged_guardian = GodStats('Enraged Guardian')
lost_kin = GodStats('Lost Kin')
no_eyes = GodStats('No Eyes')
traitor_lord = GodStats('Traitor Lord')
white_defender = GodStats('White Defender')
soul_tyrant = GodStats('Soul Tyrant')
markoth = GodStats('Markoth')
grey_prince_zote = GodStats('Grey Prince Zote')
failed_champion = GodStats('Failed Champion')
nightmare_king_grimm = GodStats('Nightmare King Grimm')
pure_vessel = GodStats('Pure Vessel')
absolute_radiance = GodStats('Absolute Radiance')

poh = [vengefly_king, gruz_mother, false_knight, massive_moss_charger, hornet_protector, gorb, dung_defender,
       soul_warrior, brooding_mawlek, brothers, xero, crystal_guardian, soul_master, oblobbles, sisters_of_battle,
       marmu, flukemarm, broken_vessel, galien, paintmaster_sheo, hive_knight, elder_hu, the_collector, god_tamer,
       troupe_master_grimm, watcher_knight, uumuu, winged_nosk, great_nailsage_sly, hornet_sentinel, enraged_guardian,
       lost_kin, no_eyes, traitor_lord, white_defender, soul_tyrant, markoth, grey_prince_zote, failed_champion,
       nightmare_king_grimm, pure_vessel, absolute_radiance]


def LoadStats(filePath):
    file = open(filePath, "r")
    allLines = file.readlines()
    allLines.pop(0)
    allLines.pop(0)

    for line in allLines:
        currLine = line.strip()
        splitLine = currLine.split('|')
        for god in poh:
            if god.name == splitLine[0]:
                god.attempt_count = float(splitLine[1])
                god.success_count = float(splitLine[2])
                god.success_rate = float(splitLine[3])
                continue

    print("Data loaded successfully.\n")


def SaveStats(filePath):
    file = open(filePath, "w")
    file.write("Pantheon of Hallownest Progression Data\n")
    file.write("God|Attempts|Successes|Rate of Success\n")
    for god in poh:
        file.write("%s|%d|%d|%f\n" % (god.name, god.attempt_count, god.success_count, god.success_rate))

    print("Data saved successfully.\n")


def AddRun():

    load_data = input("Would you like to load data? (y/n): ")

    if load_data == 'y':
        filePath = input("Please provide a file path: ")
        LoadStats(filePath)
    elif load_data != 'n':
        print("Error: Invalid input. Please try again.\n")
        AddRun()
        return

    print("\nTo save your data to a file, type save.\n")

    print("To load data from a file, type load.\n")

    print("To reset data, type reset.\n")

    print("Please enter the full name of the god.\n")

    while True:
        run_ender = input("Which god killed you?: ").lower()

        if run_ender == "stats":
            PrintData()
            continue
        elif run_ender == "save":
            filePath = input("Please provide a file path: ")
            SaveStats(filePath)
            continue
        elif run_ender == "load":
            filePath = input("Please provide a file path: ")
            LoadStats(filePath)
            continue
        elif run_ender == "reset":
            for god in poh:
                god.attempt_count = 0.0
                god.success_count = 0.0
                god.success_rate = 0.0
            print("Data reset successfully.\n")
            continue
        elif run_ender == 'q':
            save = input("Would you like to save before quitting? (y/n): ")
            while save != 'y' and save != 'n':
                print("Error: Invalid input. Please try again.\n")
                save = input("Would you like to save before quitting? (y/n): ")
            if save == 'y':
                filePath = input("Please provide a file path: ")
                SaveStats(filePath)
            break

        god_exists = False

        for god in poh:
            if god.name.lower() == run_ender:
                god_exists = True

        if not god_exists:
            print("\nThis god does not exist. Please write out the god's full name.\n")
            continue

        for god in poh:
            god.attempt_count = god.attempt_count + 1
            if god.name.lower() != run_ender:
                god.success_count = god.success_count + 1
            else:
                break

        print("\nYou have died to %s. Successfully updated data.\n" % run_ender)


def PrintData():

    print("\nTotal Attempts: %d\n" % vengefly_king.attempt_count)

    for god in poh:
        god.UpdateSuccessRate()
        god.PrintStats()


def main():
    print()
    AddRun()


if __name__ == "__main__":
    main()

