# convert all units of time in seocnds

def time_in_seconds(day, hour, minute, sec):
    day = day * 24 * 3600
    hour *= 3600
    minute *= 60
    sec = sec 
    return print('Time in seconds: ', day + hour + minute + sec)

time_in_seconds(4, 5, 20, 10)