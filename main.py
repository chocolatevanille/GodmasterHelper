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


def LoadStats(filePath):
    allLines = open(filePath, "r").readlines()
    allLines.pop(0)
    allLines.pop(0)

    for line in allLines:
        splitLine = line.strip().split('|')
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

    print("To quit, type q.\n")

    print("Please enter the full name of the god.\n")

    while True:
        action = input("Enter action or the name of the god who killed you.: ").lower()

        if action == "stats":
            PrintData()
            continue
        elif action == "save":
            filePath = input("Please provide a file path: ")
            SaveStats(filePath)
            continue
        elif action == "load":
            filePath = input("Please provide a file path: ")
            LoadStats(filePath)
            continue
        elif action == "reset":
            for god in poh:
                god.attempt_count = 0.0
                god.success_count = 0.0
                god.success_rate = 0.0
            print("Data reset successfully.\n")
            continue
        elif action == 'q':
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
            if god.name.lower() == action:
                god_exists = True

        if not god_exists:
            print("\nThis god does not exist. Please write out the god's full name.\n")
            continue

        for god in poh:
            god.attempt_count += 1
            if god.name.lower() != action:
                god.success_count += 1
            else:
                break

        print("\nYou have died to %s. Successfully updated data.\n" % action)


def PrintData():

    print("\nTotal Attempts: %d\n" % poh[0].attempt_count)

    for god in poh:
        god.UpdateSuccessRate()
        god.PrintStats()


def main():
    print()
    AddRun()


if __name__ == "__main__":
    main()

