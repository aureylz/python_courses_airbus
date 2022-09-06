from datetime import datetime
from zoneinfo import ZoneInfo
from time import sleep
import json
import csv
import os

print ('TP N°3 (Python Basics)')
print('Functions')

print(f"""3.1.1 - Use one of the datetime module functions to displays the current time in your zone: 
    {datetime.now().time()}""")


def what_time_is_it():
    print(f"""3.1.2 - Wrap the above code into a new function to display the current time in your zone: 
    {datetime.now().time()}""")


what_time_is_it()


def what_zulu_time_is_it():
    print(f"""3.1.3 - Modify the earlier created function to display the current time in UTC:
    {datetime.utcnow().time()} (Zulu)""")


what_zulu_time_is_it()


def what_zulu_time_is_it_fancy(display_format: str):
    # formatting https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    print(f"""3.1.4 - Modify again the function to accept a time formatter to customize the time display format:
    {datetime.utcnow().time().strftime(display_format)}""")


def what_time_is_it_fancy_39(display_format: str, time_zone: str):
    # zoneinfo Python >= 3.9 https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo
    print(f"""3.1.4 - Python >= 3.9:
    {datetime.now(ZoneInfo(time_zone)).time().strftime(display_format)} in {time_zone}""")


def what_time_is_it_fancy(display_format: str, time_zone: str):
    print(f"""3.1.4 - Python >= 3.9:
    {datetime.now(ZoneInfo(time_zone)).time().strftime(display_format)} in {time_zone}""")


what_zulu_time_is_it_fancy('It is %-I %p past by %S mn')
what_time_is_it_fancy_39('%H:%M:%S', 'US/Pacific')


def what_time_is_it_smart(display_format: str = '%H:%M:%S', in_zulu_time: bool = False):
    if in_zulu_time:
        current_date = datetime.utcnow().time().strftime(display_format)
    else:
        current_date = datetime.now().time().strftime(display_format)
    print(f"""3.1.5 - Now make the parameters optional, if not provided, display time in your current zone:
    {current_date} in {'UTC' if in_zulu_time else 'CET' }""")


def what_time_is_it_smart_39(display_format: str = '%H:%M:%S', time_zone: str = 'CET'):
    print(f"""3.1.5 - Python >= 3.9:
    {datetime.now(ZoneInfo(time_zone)).time().strftime(display_format)} in {time_zone}""")


what_time_is_it_smart()
what_time_is_it_smart(in_zulu_time=True)
what_time_is_it_smart_39()
what_time_is_it_smart_39(time_zone='Europe/Paris')


def simple_clock(duration: int = 3):
    print(f"""3.2.1 - Create a function that displays the current time during 1 mn and refresh every second:""")
    for sec in range(duration):
        print(datetime.now().time())
        sleep(1)


def simple_clock_even_odd(duration: int = 6):
    print(f"""3.2.2 - Modify the above function so that it displays even seconds differently""")
    for sec in range(duration):
        current_time = datetime.now().time()
        if current_time.second % 2 == 0:
            display_format = "%H:%M:%S (Even)"
        else:
            display_format = "%H:%M:%S (Odd)"
        print(f'{current_time.strftime(display_format)}')
        sleep(1)


simple_clock()
simple_clock_even_odd(5)


def simple_timer(duration: int = 12):
    print("""3.2.3 - Create a countdown time that displays a * each second, but starts displaying the 10 remaining seconds""")
    for count_down in range(duration, 0, -1):
        if count_down > 10:
            print('*', end='')
        else:
            print(count_down, end=' ')
        sleep(1)


def simple_timer_alt(duration: int = 12):
    print("""3.2.3 - Alternate way""")
    while duration >= 0:
        if duration > 10:
            print('*', end='')
        else:
            print(duration, end=' ')
        sleep(1)
        duration -= 1


simple_timer()
simple_timer_alt()


def save_as_json(**kwargs):
    print("""Create a function that accepts an arbitrary number of key / value parameters and save it as json""")
    try:
        with open('my_dict.json', 'wt') as json_file:
            json.dump({k: v for k, v in kwargs.items()}, json_file, indent=2)
    except (PermissionError, IOError) as ex:
        print(ex)


save_as_json(plane_1='A220', plane_2='A320', plane_3='A330', plane_4='A350')



print('3.3.2')
with open('tp3_airbus_family.csv') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)  # skip header
    for line in reader:
        print(line)

print('3.3.3')
titles = ['name', 'seating', 'range']
with open('tp3_airbus_family.csv') as f:
    reader = csv.DictReader(f, titles)
    next(reader)  # skip header
    for line in reader:
        print(line)

# 3.3.4

print('3.3.4a')
titles = ['name', 'seating', 'range']
aircrafts = []
with open('tp3_airbus_family.csv') as infile:
    reader = csv.DictReader(infile, titles)
    next(reader)  # skip header
    for line in reader:
        aircrafts.append({'name': line['name'], 'seating': line['seating'], 'range': line['range']})
with open('tp3_airbus_family.json', 'w') as outfile:
    outfile.write(json.dumps(aircrafts))

print('3.3.4b')
titles = ['name', 'seating', 'range']
with open('tp3_airbus_family.csv') as infile:
    reader = csv.DictReader(infile, titles)
    next(reader)  # skip header
    with open('tp3_airbus_family.json', 'w') as outfile:
        first_line = True
        outfile.write('[\n')
        for line in reader:
            if not first_line:
                outfile.write(',\n')
            outfile.write(json.dumps({'name': line['name'], 'seating': line['seating'], 'range': line['range']}, indent=4))
            first_line = False
        outfile.write('\n]')

# 3.4 Test

print('3.4.1')
def aircrafts_csv_to_json(csvin: str, jsonout: str):
    titles = ['name', 'seating', 'range']
    aircrafts = []
    with open(csvin) as infile:
        reader = csv.DictReader(infile, titles)
        next(reader)  # skip header
        for line in reader:
            aircrafts.append({'name': line['name'], 'seating': line['seating'], 'range': line['range']})
    with open(jsonout, 'w') as outfile:
        outfile.write(json.dumps(aircrafts))


print('3.4.2')
def test_aircrafts_csv_to_json():
    jsontest = 'tp3_conversion-test.json'
    aircrafts_csv_to_json(csvin='tp3_airbus_family.csv', jsonout=jsontest)
    expected_list = [
        {'name': 'A220-100', 'seating': '100-120', 'range': '3450'},
        {'name': 'A220-300', 'seating': '120-150', 'range': '3400'},
        {'name': 'A319neo', 'seating': '120-150', 'range': '3650'},
        {'name': 'A320neo', 'seating': '150-180', 'range': '3450'},
        {'name': 'A321neo', 'seating': '180-220', 'range': '4000'},
        {'name': 'A321XLR', 'seating': '180-220', 'range': '4700'},
        {'name': 'A330-800', 'seating': '220-260', 'range': '8150'},
        {'name': 'A330-900', 'seating': '260-300', 'range': '7200'},
        {'name': 'A350-900', 'seating': '300-350', 'range': '8100'},
        {'name': 'A350-1000', 'seating': '350-410', 'range': '8700'},
        {'name': 'A380', 'seating': '400-550', 'range': '8000'}
    ]

    with open(jsontest) as infile:
        read_list = json.load(infile)  # read_list = json.loads(infile.read())
        assert read_list == expected_list

    if os.path.exists(jsontest):
        os.remove(jsontest)


print('3.4.3')
if __name__ == "__main__":
    test_aircrafts_csv_to_json()
    print("test Ok")
