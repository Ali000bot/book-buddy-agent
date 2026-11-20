from math import ceil


def pages_per_day(pages: int, days: int) -> int:
    """Calculate how many pages to read per day to finish on time."""
    if pages < 0:
        raise ValueError("Число страниц должно быть 0 или больше.")

    if days <= 0:
        raise ValueError("Число дней должно быть больше 0.")

    return ceil(pages / days)



def days_to_finish(pages: int, daily_pages: int) -> int:
    """Calculate how many days it takes to finish the remaining pages."""
    try:
        day_left = ceil(pages/ daily_pages)
    except ZeroDivisionError:
        print ("value for daily pages can not be 0")
    else:
        return day_left
        

print(days_to_finish(10, 0))
