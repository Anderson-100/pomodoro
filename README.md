# pomodoro.py

A simple Pomodoro timer, built in Python. <br>
<br>
To use it, simply download the files and run one of the following commands:
- **Default Mode:** ```python3 pomodoro.py```: *(20 minutes work / 5 minutes break)*
- **Personalized Mode:** ```python3 pomodoro.py {work_time} {break_time}``` <br>

This program runs in a never-ending loop; use `^C` to end it. <br>
<br>
**Requires:** 
- [Python 3](https://www.python.org/), due to the implementation of f-strings.
- [playsound](https://pypi.org/project/playsound/) library to play audio.

## What is Pomodoro?
Pomodoro is a popular studying and productivity technique that combines timed work sessions with breaks in between. For example, one popular configuration is 20-minute block of work with 5-minute breaks in between, although many people will have their own personal preference (including [Animedoro](https://youtu.be/bUjGZJIgse0)).

## Update Log
### v1.0 

*2021-08-16* <br>
Initial commit. Users can choose between the default 20/5 or personalize the time using command-line arguments. Currently uses sound effects from the popular 2018 game Among Us, although I am planning on implementing more themes.
