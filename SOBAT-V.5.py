# some improvements :

import datetime

import sys
import datetime
import time

SLEEP_CYCLE = 90
SLEEP_LATENCY = 0

# What is today function
month_names = {

    1: 'January', 2: 'February', 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August", 9: "September",
    10: "October", 11: "November", 12: "December"}


def today_date():
    today = datetime.date.today()
    day = today.day
    month = today.month
    month_name = month_names[month]
    print(f"== Today is {day} {month_name}, or ({today.year}-{today.month}-{today.day})")


def calculate_wakeup_times(bedtime):
    wake_times = []

    for cycles in range(1, 7):
        wake_time = bedtime + datetime.timedelta(minutes=SLEEP_CYCLE * cycles)
        wake_times.append(wake_time)

    return wake_times


def calculate_bedtimes(wakeup_time):
    bedtimes = []

    for cycles in range(6, 0, -1):
        bedtime = wakeup_time - datetime.timedelta(minutes=SLEEP_CYCLE * cycles)
        bedtime += datetime.timedelta(minutes=SLEEP_LATENCY)
        bedtimes.append(bedtime)

    return bedtimes


def print_times(times):
    cycles = len(times)

    while cycles > 0:
        i = len(times) - cycles
        time = times[i]

        print(f"{time.strftime('%I:%M %p')} -> [{cycles} cycles]")

        cycles -= 1


def scenario_one():
    now = datetime.datetime.now()
    print(f"The clock now is: {now.strftime('%I:%M %p')}")

    bedtime = now + datetime.timedelta(minutes=SLEEP_LATENCY)

    print(f"Bedtime will be:  {bedtime.strftime('%I:%M %p')}" + "\n")

    print("\nFor good sleep,Try to wake up at these times:")

    wake_times = calculate_wakeup_times(bedtime)

    print_times(wake_times)
    print(f"\nNOTE: Your current SLEEP_LATENCY is set to {SLEEP_LATENCY} minutes.")
    print("\nHave good Sleep user! \n")


def scenario_two():
    now = datetime.datetime.now()

    print(f"The clock now is: {now.strftime('%I:%M %p')}")

    bedtime = get_user_bedtime()

    bedtime += datetime.timedelta(minutes=SLEEP_LATENCY)

    print(f"Bedtime will be:: {bedtime.strftime('%I:%M %p')}" + "\n")
    print("\nFor good sleep,Try to wake up at these times:")
    wake_times = calculate_wakeup_times(bedtime)

    print_times(wake_times)
    print(f"\nNOTE: Your current SLEEP_LATENCY is set to {SLEEP_LATENCY} minutes.")
    print("\nHave good Sleep user! \n")


def scenario_three():
    wakeup_time = get_user_wakeup()

    print(f"Wakeup Time: {wakeup_time.strftime('%I:%M %p')}")
    print("\nTry to go to sleep at these times:")

    bedtimes = calculate_bedtimes(wakeup_time)

    print_times(bedtimes)
    print(f"\nNOTE: Your current SLEEP_LATENCY is set to {SLEEP_LATENCY} minutes.")
    print("\nHave good Sleep user! \n")


# Input functions

def get_user_bedtime():
    while True:
        bedtime_str = input("Enter bedtime (HH:MM AM/PM) or enter (q) to exit: ")

        if bedtime_str == 'q':
            print("\nQuitting program.. See you later!\n")
            sys.exit()

        print()  # Print empty line

        try:
            bedtime = datetime.datetime.strptime(bedtime_str, "%I:%M %p")
            break

        except ValueError:
            print("Invalid time format. Please enter in HH:MM AM/PM format")
            print("For example: 07:30 AM")
            print()

    return bedtime


def get_user_wakeup():
    while True:
        wakeup_str = input("Enter wakeup time (HH:MM AM/PM) or enter (q) to exit: ")

        if wakeup_str == 'q':
            print("\nQuitting program.. See you later!\n")
            sys.exit()

        print()  # Print empty line

        try:
            wakeup = datetime.datetime.strptime(wakeup_str, "%I:%M %p")
            break
        except ValueError:
            print("Invalid time format. Please enter in HH:MM AM/PM format")
            print("For example: 07:30 AM")
            print()

    return wakeup


# Main code
print("-------------------------------------")
print("Hello user,Welcome to (SOBAT) program\n (SOBAT) is a Sleep Cycle Calculator.")
today_date()
print("\n #Choose one of This Three Scenario:\n \nFirst Scenario:  -> [ I will sleep now   ]")
print("Second Scenario: -> [ Choose bedtime     ]")
print("Third Scenario:  -> [ Choose wakeup time ]\n")
print("(q) Quit from the progrm")
choice = input("Enter (1), (2), (3),or (q) to choose scenario: ")

if choice == "1":
    scenario_one()
elif choice == "2":
    scenario_two()
elif choice == "3":
    scenario_three()
elif choice == "q":
    print("\nQuitting program.. See you later!\n")
    sys.exit()
else:
    print("Invalid choice")
    print("Please enter 1, 2 or 3")
