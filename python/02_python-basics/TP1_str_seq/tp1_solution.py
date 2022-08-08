from datetime import date
from calendar import month_name

# 01 - Days of the week

# 1.1 Days

# 1.1.1
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# 1.1.2 (example for Wednesday)
days[2]

# 1.1.3
for idx, day in enumerate(days):
    print(f"day {idx+1} of the week is {day}")

# 1.1.4
for day in days:
    print(day[:2])

# 1.1.5
new_day = ''
for day in days:
    new_day += day[5]

# 1.1.6
days.append('yasdydy')

# 1.1.7
days.remove('yasdydy')  # or del(days[7]) or days.pop(7)

# 1.2 Days & mood

# 1.2.1
days_moods = {days[0]: "Starting the week slowly", days[1]: "Focus on my studies", days[2]: "Looking for a new TV show",
              days[3]: "Time to have a beer in the city center", days[4]: "Preparing the week-end", days[5]: "Ready for the party!", days[6]: "Studying for tomorrow's  exams"}

# 1.2.2 (example for Wednesday)
days_moods['Wednesday']

# 1.2.3
days_moods['Monday'] = "Starting the week by an exam"

# 1.2.4
days_moods.popitem()  # or days_moods.pop('Sunday') or del(days_moods['Sunday'])

# 1.2.5
days_moods.update({'Sunday': 'Relaxing before holidays'})  # or days_moods['Sunday'] = 'Relaxing before holidays'

# 1.2.6
shortdays_moods = {day[:3]: mood.split()[0] for day, mood in days_moods.items()}

# 1.3 What day is it?

# 1.3.1
# Cf import at the top

# 1.3.2
f"Today we are {days[date.today().isoweekday()-1]} {date.today().day}"

# 1.3.3


def order(arg):
    '''
    Convert integer to ordinal number.  
    Args:
    -  arg: integer (eg: 1)
    Returns:
    - ordinal number (eg: 1st)
    '''
    # Convert to integer (allow string or float arg if value is correct, else raise an error)
    i = int(arg)
    if arg < 1 or arg > 99:
        raise ValueError('Number is expected to be > 0 and < 100')
    # 1 => 1st, 2 => 2nd, 3 => 3rd, except 11th 12th 13th
    if 11 <= i <= 13:
        return str(i)+'th'
    if i % 10 == 1:
        return str(i)+'st'
    if i % 10 == 2:
        return str(i)+'nd'
    if i % 10 == 3:
        return str(i)+'rd'
    else:
        return str(i)+'th'


# 1.3.4
f"Today we are {days[date.today().isoweekday()-1]}, the {order(date.today().day)}"

# 1.3.5
f"Today we are {days[date.today().isoweekday()-1]}, the {order(date.today().day)} of {month_name[date.today().month]}"

# 1.3.6
f"Today we are {date.today().strftime('%A')}, the {order(date.today().day)} of {date.today().strftime('%B')}"
