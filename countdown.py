import time

print("\nThis simple program takes an input time and counts down to zero!")

hours = int(input("Enter the number of hours you would like to set this timer for: "))
minutes = int(input("Enter the number of minutes you would like to set this timer for: "))
seconds = int(input("Enter the number of seconds you would like to set this timer for: "))

#Plural Bools
plural_hour = True if hours != 1 else False
if plural_hour:
    h = "hours"
else:
    h = "hour"

plural_min = True if minutes != 1 else False
if plural_min:
    m = "minutes"
else:
    m = "minute"

plural_sec = True if seconds != 1 else False
if plural_sec:
    s = "seconds"
else:
    s = "second"

confirmation = str(input(f"You would like to set a countdown for {hours} {h}, {minutes} {m} and {seconds} {s}? (y or n): "))

total_in_sec = (hours * (60**2)) + (minutes * 60) + seconds

def countdown():
    timer = total_in_sec
    for t in range(timer, 0, -1):
        second_count = t % 60
        minute_count = int(t / 60) % 60
        hour_count = int(t / 3600) 
        print(f"\n{hour_count:.0f}:{minute_count:.0f}:{second_count:.0f}")
        time.sleep(1)
    print("Timer Complete!")


def main():
    if confirmation.lower() == "y":
        countdown()
    elif confirmation.lower() == "n":
        print("\nPlease enter the correct time")
    else:
        print("\n\033[1mERROR:\033[0m Invalid Entry: Please enter \"y\" or \"n\"")

main()