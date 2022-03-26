from datetime import datetime
from config import teachers


def get_period(day: str):
    current_seconds = 3600 * (datetime.now().hour + (datetime.now().minute / 60))
    if current_seconds < 27000 or current_seconds > 53000:
        return None

    periods = {
        (27000, 33120): ["1", teachers[0]] if day == "1" else ["2", teachers[1]],
        ((33120+480), 39600): ["3", teachers[2]] if day == "1" else ["4", teachers[3]],
        ((39660+480), 43920): ["5", teachers[4]],
        (47268, 52776): ["6", teachers[5]] if day == "1" else ["7", teachers[6]],

    }
    for key in reversed(periods):
        if key[0] < current_seconds < key[1]:
            return periods[key]

    return None
