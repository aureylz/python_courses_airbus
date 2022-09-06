# Python basics - Hands on

## 02 - Days of the week

### 2.1 Days (list and loop)

- 2.1.1 Write a ```list``` containing days of the week: Monday, Tuesday, ...
- 2.1.2 Display the day corresponding to today
- 2.1.3 Loop on days list to display for each day its position in the week. _Tip_: use ```enumerate``` and ```f-string```
  ```
  day 1 of the week is Monday
  day 2 of the week is Tuesday
  ...
  ```
- 2.1.4 Print the 2 first letters of each day. Expected result:  
  ```
  Mo
  Tu
  ...
  ```
- 2.1.5 Create a word with the 6th letter of each day.  
  ```
  new_day == 'yasdydy'
  ```
- 2.1.6 Add this new day in the ```list``` of days.  
- 2.1.7 Remove the day from the ```list```.  

### 2.2 Days & mood (dict and comprehension)

- 2.2.1 Write a ```dictionary``` with days of the week, and a mood / action for each day. Use previous ```list``` to get days. Example:  
  | Key | Value |
  | --- | --- |
  | "Monday" | "Starting the week slowly" |
  | "Tuesday" | "Focus on my studies" |
  | ... | ... |
- 2.2.2 Display mood of today
- 2.2.3 Change action for Monday to ```"Starting the week by an exam"```
- 2.2.4 Remove last item from moods ```dictionnary```
- 2.2.5 Add item to ```dictionnary```:  
  | Key | Value |
  | --- | --- |
  | "Sunday" | "Relaxing before holidays" |  
- 2.2.6 Use previous ```dictionnary``` to build a new one, having short day as key and first word of mood / description. _Tip_: ```split``` string. Example:  
  | Key | Value |
  | --- | --- |
  | "Mon" | "Starting" |
  | "Tue" | "Focus" |
  | ... | ... |

### 2.3 What day is it? (module and function)

- 2.3.1 Let's try ```datetime``` module.  
  ```python
  python3
  >>> from datetime import date

  >>> datetime.date(2022, 8, 5)
  >>> str(date.today())
  >>> date.today().year
  >>> date.today().month
  >>> date.today().day
  >>> date.today().weekday()
  >>> date.today().isoweekday()
  ```
- 2.3.2 Use ```datetime``` and previous days list to display the current day following this pattern: ```'Today we are Wednesday 7'```. _Tip_: Use ```f-string```
- 2.3.3 Write a ```function``` that takes a number as parameter and returns an ordinal number
  Only manage numbers < 100. Example of usage:  
  ```
  >>> order(1)
  1rst
  ```
  To test your ```function```: write it directly in the ```REPL``` or write it in a file and import your file:
  ```
  python -i my_tp_file.py
  ```
- 2.3.4 Use the ```function``` to now write date with following pattern: ```'Today we are Wednesday, the 7th'```
- 2.3.5 Add current month and date to previous string to get: ```'Today we are Wednesday, the 7th of Sptember'```.  _Tip_: Use ```calendar.month_name```
  ```
  import calendar
  calendar.month_name[1]
  ``` 
- 2.3.6 If not done previously write your order function in a file. 
Use a main to call it.  
```
python my_tp_file.py 3
```
_=> return "3rd"_
- 2.3.7  Bonus: use only date module, with strftime to display date with previous pattern ('Today we are Wednesday, the 7th of Sptember'). Cf. https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
```
date.today().strftime('%B')
date.today().strftime('%A')
``` 