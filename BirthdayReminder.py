import datetime
import os


def add_birthday(filename):
    name = input("Enter the name: ")
    date_str = input("Enter the birthday (DD-MM-YYYY): ")
    with open(filename, 'a') as file:
        file.write(f"{name},{date_str}\n")
    print("Birthday added successfully!")


def view_birthdays(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print("Saved Birthdays:")
            for line in file:
                name, date_str = line.strip().split(',')
                print(f"{name} - {date_str}")
    else:
        print("No birthdays saved yet.")


def check_upcoming_birthdays(filename):
    if os.path.exists(filename):
        today = datetime.date.today()
        with open(filename, 'r') as file:
            print("Upcoming Birthdays:")
            for line in file:
                name, date_str = line.strip().split(',')
                birth_date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
                # Get the birthday date this year
                next_birthday = birth_date.replace(year=today.year)
                if today <= next_birthday <= today + datetime.timedelta(days=30):
                    print(f"{name} - {next_birthday.strftime('%d-%m-%Y')}")
    else:
        print("No birthdays saved yet.")


def main():
    filename = "birthdays.txt"
    while True:
        print("\nBirthday Reminder App")
        print("1. Add Birthday")
        print("2. View Birthdays")
        print("3. Check Upcoming Birthdays")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_birthday(filename)
        elif choice == '2':
            view_birthdays(filename)
        elif choice == '3':
            check_upcoming_birthdays(filename)
        elif choice == '4':
            print("Exiting the Birthday Reminder App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
