def get_sum_hour(start_hour, duration_hour, am_or_pm):
    if am_or_pm == "PM":
        start_hour = start_hour + 12
    sum = start_hour + duration_hour
    return sum

def get_sum_minutes(start_minute, duration_minute):
    sum_minutes = start_minute + duration_minute
    if sum_minutes > 60:
        sum_minutes -= 60
        return sum_minutes, 1
    else:
        return sum_minutes, 0

def get_new_time(sum_hour, sum_minutes, pm_flag, i, day):
    days = {"Monday": 0, "Tuesday" : 1, "Wednesday" : 2, "Thursday" : 3, "Friday" : 4, "Saturday" : 5, "Sunday" : 6}
    new_time = f"{sum_hour}:{str(sum_minutes).zfill(2)} "
    if pm_flag == True:
        new_time += f"PM"
    else:
        new_time += f"AM"
    if day:
        new_day = ""
        j = i + days[day.title()]
        while j >= 7:
            j -= 7
        for key, val in days.items():
            if val == j:
                new_day = key
                break
        new_time += f", {new_day}"
    if i == 1:
        new_time += f" (next day)"
    elif i > 1:
        new_time += f" ({i} days later)"
    return new_time


def add_time(start, duration, day=None):
    time_start, am_or_pm = start.split(' ')
    start_hour, start_minute = time_start.split(':')
    duration_hour, duration_minute = duration.split(':')
    pm_flag = False

    sum_minutes, add_1 = get_sum_minutes(int(start_minute), int(duration_minute))
    sum_hour = get_sum_hour(int(start_hour), int(duration_hour), am_or_pm) + add_1 

    i = 0
    if sum_hour >= 24:
        while not sum_hour <= 24:
            sum_hour -= 24
            i += 1
    if sum_hour == 24:
        sum_hour -= 12
        i += 1
    elif sum_hour >= 12 and sum_minutes > 0:
        if sum_hour > 12:
            sum_hour -= 12
        pm_flag = True
    new_time = get_new_time(sum_hour, sum_minutes, pm_flag, i, day)
    return new_time

print(add_time("11:59 PM", "24:05"))