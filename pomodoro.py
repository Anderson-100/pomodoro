"""
A pomodoro timer based in Python. Can take in command-line arguments for  personalization.
Author: Anderson Hsiao
Last updated 2021-09-26
"""

# Imports
import os
import sys
import time
from playsound import playsound


DEFAULT_THEME = "among_us"
DEFAULT_WORK_TIME = 20
DEFAULT_BREAK_TIME = 5
DEFAULT_EXT_BREAK_TIME = 15

THEMES = os.listdir("pomodoro_audio")
CUSTOM_SETTINGS = os.listdir("custom_settings")

# Main Function
def main():
    try:
        # Default
        if len(sys.argv) == 1:
            timer(DEFAULT_THEME, DEFAULT_WORK_TIME, DEFAULT_BREAK_TIME, DEFAULT_EXT_BREAK_TIME)

        elif len(sys.argv) == 2:
            arg = sys.argv[1].lower()

            # User asking for help
            if sys.argv[1].lower() == "help":
                print_help()
                sys.exit(0)
            
            # Choosing a theme
            elif arg in THEMES:
                timer(arg, DEFAULT_WORK_TIME, DEFAULT_BREAK_TIME, DEFAULT_EXT_BREAK_TIME)

            # Choosing a custom setting
            elif f"{arg}.txt" in CUSTOM_SETTINGS:
                custom_setting(arg)

            # User enters an unknown value
            else:
                print("Theme or custom setting could not be found. Please use 'python3 pomodoro.py help' to see all available options.")
                sys.exit(1)

        elif len(sys.argv) == 3:
            timer(DEFAULT_THEME, int(sys.argv[1]), int(sys.argv[2]), DEFAULT_EXT_BREAK_TIME)

        elif len(sys.argv) == 4:
            timer(DEFAULT_THEME, int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

        
        elif len(sys.argv) == 5:
            timer(sys.argv[1].lower(), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))

        else:
            print("Error: Incorrect use of arguments. Please use 'python3 pomodoro.py help' for information on how to properly format arguments.")
            sys.exit(1)

    except ValueError:
        print("Error: Please enter integer values for times.")
        sys.exit(1)


# Prints out the help information
def print_help():
    print("""Input Format: 
    0 inputs: default settings (among_us theme, 20 mins work, 5 mins break, 15 mins extended break)
    1 input:  {theme or custom setting}
    2 inputs: {work_time} {break_time}
    3 inputs: {work_time} {break_time} {extended_break_time}
    4 inputs: {theme} {work_time} {break_time} {extended_break_time}
    """)

    print("Themes:")
    for theme in THEMES:
        print(f"    {theme}")

    print("\nCustom Settings:")
    for setting in CUSTOM_SETTINGS:
        # Remove the ".txt" at the end
        print(f"    {setting[:len(setting)-4]}")


# Custom settings function
# Parses the parameters from corresponding txt file
# then starts timer using those settings
def custom_setting(setting: str):
    setting_info = []
    with open(f"custom_settings/{setting}.txt") as file:
        for line in file:
            if "\n" in line:
                setting_info.append(line[:len(line)-1])
            else:
                setting_info.append(line)
    
    # print(setting_info)

    if setting_info[0] not in THEMES:
        print("Theme used in custom setting is not available. Make sure everything is spelled correctly.")
        sys.exit(1)

    try:
        timer(setting_info[0], int(setting_info[1]), int(setting_info[2]), int(setting_info[3]))
    except ValueError:
        print("An error occurred when parsing your custom settings. Make sure that all the values are correct.")
        sys.exit(1)


# Input times are in minutes
def timer(theme: str, work_time: int, break_time: int, ext_break_time: int):
    # Audio files
    work_done_audio = f"pomodoro_audio/{theme}/work_done.wav"
    break_done_audio = f"pomodoro_audio/{theme}/break_done.wav"

    cnt = 1
    while True:
        print(f"Round {cnt}!")
        print("Work:")
        countdown(work_time * 60)
        playsound(work_done_audio)

        # Extended break every 3rd iteration
        if cnt % 3 == 0:
            current_break_time = ext_break_time
        else:
            current_break_time = break_time
        print("Break:")
        countdown(current_break_time * 60)
        playsound(break_done_audio)
        cnt += 1

# Uses the time library to count down for the inputted number of seconds
def countdown(t: int):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

if __name__ == "__main__":
    main()
