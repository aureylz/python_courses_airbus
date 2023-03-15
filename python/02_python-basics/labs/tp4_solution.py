from datetime import datetime
from zoneinfo import ZoneInfo
from time import sleep

# TP 4 - Bonus tu use date libraries

print("Date time")

print(
    f"""4.1.1 - Use one of the datetime module functions to displays the current time in your zone: 
    {datetime.now().time()}"""
)


def what_time_is_it():
    print(
        f"""4.1.2 - Wrap the above code into a new function to display the current time in your zone: 
    {datetime.now().time()}"""
    )


what_time_is_it()


def what_zulu_time_is_it():
    print(
        f"""4.1.3 - Modify the earlier created function to display the current time in UTC:
    {datetime.utcnow().time()} (Zulu)"""
    )


what_zulu_time_is_it()


def what_zulu_time_is_it_fancy(display_format: str):
    # formatting https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    print(
        f"""4.1.4 - Modify again the function to accept a time formatter to customize the time display format:
    {datetime.utcnow().time().strftime(display_format)}"""
    )


def what_time_is_it_fancy_39(display_format: str, time_zone: str):
    # zoneinfo Python >= 3.9 https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo
    print(
        f"""4.1.4 - Python >= 3.9:
    {datetime.now(ZoneInfo(time_zone)).time().strftime(display_format)} in {time_zone}"""
    )


def what_time_is_it_fancy(display_format: str, time_zone: str):
    print(
        f"""4.1.4 - Python >= 3.9:
    {datetime.now(ZoneInfo(time_zone)).time().strftime(display_format)} in {time_zone}"""
    )


what_zulu_time_is_it_fancy("It is %-I %p past by %S mn")
what_time_is_it_fancy_39("%H:%M:%S", "US/Pacific")


def what_time_is_it_smart(display_format: str = "%H:%M:%S", in_zulu_time: bool = False):
    if in_zulu_time:
        current_date = datetime.utcnow().time().strftime(display_format)
    else:
        current_date = datetime.now().time().strftime(display_format)
    print(
        f"""4.1.5 - Now make the parameters optional, if not provided, display time in your current zone:
    {current_date} in {'UTC' if in_zulu_time else 'CET' }"""
    )


def what_time_is_it_smart_39(display_format: str = "%H:%M:%S", time_zone: str = "CET"):
    print(
        f"""4.1.5 - Python >= 3.9:
    {datetime.now(ZoneInfo(time_zone)).time().strftime(display_format)} in {time_zone}"""
    )


what_time_is_it_smart()
what_time_is_it_smart(in_zulu_time=True)
what_time_is_it_smart_39()
what_time_is_it_smart_39(time_zone="Europe/Paris")

print("Functions")


def simple_clock(duration: int = 3):
    print(
        f"""4.2.1 - Create a function that displays the current time during 1 mn and refresh every second:"""
    )
    for sec in range(duration):
        print(datetime.now().time())
        sleep(1)


def simple_clock_even_odd(duration: int = 6):
    print(
        f"""4.2.2 - Modify the above function so that it displays even seconds differently"""
    )
    for sec in range(duration):
        current_time = datetime.now().time()
        if current_time.second % 2 == 0:
            display_format = "%H:%M:%S (Even)"
        else:
            display_format = "%H:%M:%S (Odd)"
        print(f"{current_time.strftime(display_format)}")
        sleep(1)


simple_clock()
simple_clock_even_odd(5)


def simple_timer(duration: int = 12):
    print(
        """4.2.3 - Create a countdown time that displays a * each second, but starts displaying the 10 remaining seconds"""
    )
    for count_down in range(duration, 0, -1):
        if count_down > 10:
            print("*", end="")
        else:
            print(count_down, end=" ")
        sleep(1)


def simple_timer_alt(duration: int = 12):
    print("""4.2.3 - Alternate way""")
    while duration >= 0:
        if duration > 10:
            print("*", end="")
        else:
            print(duration, end=" ")
        sleep(1)
        duration -= 1


simple_timer()
simple_timer_alt()
