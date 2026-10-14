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

from datetime import datetime

def time_delta(t1, t2):
    format_date = "%a %d %b %Y %H:%M:%S %z"

    date1 = datetime.strptime(t1, format_date)
    date2 = datetime.strptime(t2, format_date)

    delta = abs(int((date1 - date2).total_seconds()))

    return str(delta)

def f_time_delta():
    t = int(input("Enter T the  number of testcases : "))

    for t_itr in range(t):
        t1 = input("Enter t1 in the format 'Day dd Mon yyyy hh:mm:ss +xxxx' : ")

        t2 = input("Enter t2 in the format 'Day dd Mon yyyy hh:mm:ss +xxxx' : ")

        delta = time_delta(t1, t2)
        print(delta)

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

        elif choice == "2":
            f_time_delta()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()