from datetime import datetime, timedelta

movie_periods = [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7)),
    (datetime(2024, 9, 1), datetime(2024, 9, 3)),
    (datetime(2024, 9, 6), datetime(2024, 9, 12)),
]


def expand_periods(movie_periods):
    all_dates = []
    for start, end in movie_periods:
        current_date = start
        while current_date <= end:
            all_dates.append(current_date)
            current_date += timedelta(days=1)
    return all_dates


expanded_dates = expand_periods(movie_periods)


for date in expanded_dates:
    print(date)
