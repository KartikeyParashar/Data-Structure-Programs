# importing calendar module
import calendar


def main():
    # To take month and year input from the user
    while True:
        try:
            yy = int(input("Enter year: "))
        except ValueError:
            print("Please Enter a valid value")
        else:
            if len(str(yy)) > 4:
                print("Please Enter a valid year")
                pass
            else:
                break

    while True:
        try:
            mm = int(input("Enter month: "))
        except ValueError:
            print("Please Enter month in digit format")
        else:
            if mm > 12:
                print("Please Enter a valid month")
            else:
                break
    # display the calendar
    print(calendar.month(yy, mm))


main()
