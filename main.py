# Author: willster191
# For help, contact willster191 on Reddit or willster#1886 on Discord


class GodStats:
    attempt_count = 0.0
    success_count = 0.0
    success_rate = 0.0

    def __init__(self, name):
        self.name = name

    def update_success_rate(self):
        if self.attempt_count != 0.0:
            self.success_rate = self.success_count / self.attempt_count

    def print_stats(self):
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


def load_stats(file_path):
    while True:
        try:
            all_lines = open(file_path, "r").readlines()
            all_lines.pop(0)
            all_lines.pop(0)

            for line in all_lines:
                split_line = line.strip().split('|')
                for god in poh:
                    if god.name == split_line[0]:
                        god.attempt_count = float(split_line[1])
                        god.success_count = float(split_line[2])
                        god.success_rate = float(split_line[3])
                        continue

            print("Data loaded successfully.\n")
            break
        except OSError:
            print("File does not exist.\n")
            file_path = input("Please try again or enter q to return.: ")
            if file_path == 'q':
                break


def save_stats(file_path):
    while True:
        try:
            file = open(file_path, "w")
            file.write("Pantheon of Hallownest Progression Data\n")
            file.write("God|Attempts|Successes|Rate of Success\n")
            for god in poh:
                god.update_success_rate()
                file.write("%s|%d|%d|%f\n" % (god.name, god.attempt_count, god.success_count, god.success_rate))

            print("Data saved successfully.\n")
            break
        except OSError:
            print("Invalid path.\n")
            file_path = input("Please try again or enter q to return.: ")
            if file_path == 'q':
                break


def add_run():

    load_data = input("Would you like to load data? (y/n): ")

    while True:
        if load_data == 'y':
            file_path = input("Please provide a file path: ")
            load_stats(file_path)
            break
        elif load_data != 'n':
            print("Error: Invalid input. Please try again.\n")
        else:
            break

    print("\nTo save your data to a file, type save.\n")

    print("To load data from a file, type load.\n")

    print("To reset data, type reset.\n")

    print("To view your data, type stats.\n")

    print("To record a successful completion of PoH, type success.\n")

    print("To quit, type q.\n")

    print("Please enter the full name of the god.\n")

    while True:
        action = input("Enter action or the name of the god who killed you.: ").lower()

        if action == "stats":
            print_data()
            continue
        elif action == "save":
            file_path = input("Please provide a file path: ")
            save_stats(file_path)
            continue
        elif action == "load":
            file_path = input("Please provide a file path: ")
            load_stats(file_path)
            continue
        elif action == "reset":
            for god in poh:
                god.attempt_count = 0.0
                god.success_count = 0.0
                god.success_rate = 0.0
            print("Data reset successfully.\n")
            continue
        elif action == 'success':
            for god in poh:
                god.attempt_count += 1
                god.success_count += 1
            print("You have ascended. Congratulations!\n")
        elif action == 'q':
            save = input("Would you like to save before quitting? (y/n): ")
            while save != 'y' and save != 'n':
                print("Error: Invalid input. Please try again.\n")
                save = input("Would you like to save before quitting? (y/n): ")
            if save == 'y':
                file_path = input("Please provide a file path: ")
                save_stats(file_path)
            break

        god_exists = False

        for god in poh:
            if god.name.lower() == action:
                god_exists = True

        if not god_exists:
            print("\nThis god does not exist. Please write out the god's full name.\n")
            print("If you are unsure how to spell a god's name, type stats.\n")
            continue

        for god in poh:
            god.attempt_count += 1
            if god.name.lower() != action:
                god.success_count += 1
            else:
                break

        print("\nYou have died to %s. Successfully updated data.\n" % action)


def print_data():

    print("\nTotal Attempts: %d\n" % poh[0].attempt_count)

    for god in poh:
        god.update_success_rate()
        god.print_stats()


def main():
    print()
    add_run()


if __name__ == "__main__":
    main()

