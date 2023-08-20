

def twelve_to_twentyfour(hours, minutes, period):
    try:
        if (0 <= hours <= 12) and (0 <= minutes <= 59) and (period == 'am' or period == 'pm'):
            if period == 'am' and hours < 12:
                return f"{hours:02d}{minutes:02d}HRS"
            if period == 'am' and hours ==12:
                return f"00{minutes:02d}HRS"
            if period == 'pm' and hours < 12:
                return f"{hours+12:02d}{minutes:02d}HRS"
            if period == 'pm' and hours ==12:
                return f"{hours:02d}{minutes:02d}HRS"
        else:
            return "Enter a valid time. Hours between 0 - 12, minutes between 0 - 59 & period either am / pm."
    except TypeError:
        print("TypeError: Ensure Minutes and Hours are interger values.")

def get_value_input(prompt):
    while True:
        try:
            value = int(input(f"{prompt}: "))
            break
        except ValueError:
            print("ValueError: Ensure Entered Value Is An Integer")
    return value

print("Enter the time values below.")
hours = get_value_input("Hours (int)")
minutes = get_value_input("Minutes (int)")
period = input("Period (am / pm): ")

print(twelve_to_twentyfour(hours, minutes, period))


    