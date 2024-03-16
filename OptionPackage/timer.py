import time


def timing():
    t = input("What time for countdown(1:01:01 format): ")
    t_list = list(map(lambda i: int(i), t.split(":")))
    seconds = t_list[0] * 3600 + t_list[1] * 60 + t_list[2]
    while seconds:
        hours = int(seconds / 3600)
        mins = int(seconds / 60) - hours * 60
        secs = seconds % 60
        print(f"{hours:02}:{mins:02}:{secs:02}")
        time.sleep(1)
        seconds -= 1
