def minutes_to_seconds(minutes):
    seconds = minutes * 60
    return seconds


def seconds_to_minutes(seconds):
    minutes = seconds // 60
    return minutes


if __name__ == '__main__':
    minutes = 60
    print('Minutes →', minutes)
    seconds = minutes_to_seconds(minutes)
    print('Seconds →', seconds)
    new_minutes = seconds_to_minutes(seconds)
    print('Minutes →', new_minutes)
