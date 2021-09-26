"""
A pomodoro timer based in Python. Can take in command-line arguments for  personalization.
Author: Anderson Hsiao
Last updated 2021-09-26
"""

# Imports
import sys
import time
from playsound import playsound

DEFAULT_THEME = "among_us"
DEFAULT_WORK_TIME = 20
DEFAULT_BREAK_TIME = 5
DEFAULT_EXT_BREAK_TIME = 15

# Main Function
def main():
    if len(sys.argv) == 1:
        timer(DEFAULT_THEME, DEFAULT_WORK_TIME, DEFAULT_BREAK_TIME, DEFAULT_EXT_BREAK_TIME)

    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == "help":
            print("""Input Format: 
                0 inputs: default settings (among_us theme, 20 mins work, 5 mins break, 15 mins extended break)
                1 input:  {theme}
                2 inputs: {work_time} {break_time}
                3 inputs: {work_time} {break_time} {extended_break_time}
                4 inputs: {theme} {work_time} {break_time} {extended_break_time}
                """)
            print("""Available Themes:
                among_us
                hype
                andersons_special""")
            sys.exit(0)
        
        timer(sys.argv[1].lower(), DEFAULT_WORK_TIME, DEFAULT_BREAK_TIME, DEFAULT_EXT_BREAK_TIME)
        

    elif len(sys.argv) == 3:
        try:
            timer(DEFAULT_THEME, int(sys.argv[1]), int(sys.argv[2]), DEFAULT_EXT_BREAK_TIME)
        except ValueError:
            print("Error: Please enter integer values for times.")
            sys.exit(1)

    elif len(sys.argv) == 4:
        try:
            timer(DEFAULT_THEME, int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        except ValueError:
            print("Error: Please enter integer values for times.")
            sys.exit(1)

    
    elif len(sys.argv) == 5:
        try:
            timer(sys.argv[1].lower(), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
        except ValueError:
            print("Error: Please enter integer values for times.")
            sys.exit(1)

    else:
        print("Error: Incorrect use of arguments. Please use 'python3 pomodoro.py help' for information on how to properly format arguments.")
        sys.exit(1)


# Input times are in minutes
def timer(theme, work_time, break_time, ext_break_time):
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
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

if __name__ == "__main__":
    main()
