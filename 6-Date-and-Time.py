# ==================================================
# EXERCISE 1 : Calendar Module
# ==================================================

def calendar_module():
    import calendar

    month, day, year = map(int, input("Enter the space separated month, day and year : ").split())
    weekday = calendar.weekday(year, month, day)

    days = ["MONDAY", "TUESDAY", "WEDNESDAY","THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

    print(days[weekday])


# ==================================================
# EXERCISE 2 : Time Delta
# ==================================================

def time_delta():
    



# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("DATE AND TIME")
        print("================================")
        print("1. Calendar Module")
        print("2. Time Delta")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            calendar_module()

        # elif choice == "2":
        #     runner_up()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()