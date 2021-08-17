"""
A pomodoro timer based in Python. Can take in command-line arguments for  personalization.
Author: Anderson Hsiao
Version 1.0 
2021-08-16
"""

# Imports
import os
import sys
import time

# Input times are in minutes
def main(work_time, break_time):
    # Audio files
    work_done_audio = "pomodoro_audio/emergency.wav"
    break_done_audio = "pomodoro_audio/drip.wav"

    cnt = 1
    while True:
        print(f"Round {cnt}!")
        print("Work:")
        countdown(work_time * 60)
        os.system("afplay " + work_done_audio)

        print("Break:")
        countdown(break_time * 60)
        os.system("afplay " + break_done_audio)

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
    """
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")
    """

    if len(sys.argv) == 3:
        main(int(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv) == 1:
        main(20, 5)
    else:
        print("Error:\nMust include 2 arguments: {work_time} and {break_time}")
