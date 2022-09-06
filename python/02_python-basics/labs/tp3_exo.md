# TP N°3 (Python Basics)

## 3.1 Functions

- 3.1.1 - Use one of the datetime module functions to displays the current time in your zone
- 3.1.2 - Wrap the above code into a new function to display the current time in your zone
- 3.1.3 - Modify the earlier created function to display the current time in UTC
- 3.1.4 - Modify again the function to accept a time formatter to customize the time display format
- 3.1.5 - Now make the parameters optional, if not provided, display time in your current zone

## 3.2 Control Flow

- 3.2.1 - Create a function that displays the current time during 1 mn and refresh every second
- 3.2.2 - Modify the above function so that it beeps every even seconds
- 3.2.3 - Create a countdown time that displays a * each second, but starts displaying the 10 remaining seconds

## 3.3 Files

- 3.3.1 - Create a function that accepts an arbitrary number of key / value parameters and save it as json
- 3.3.2 - Read csv file 'tp3_airbus_family.csv', print lines describing Airbus aircrafts.  
  eg: ```['A220-100', '100-120', '3450']```
- 3.3.3 Read again csv file 'tp3_airbus_family.csv', print each line as a json.  
  eg: ```{'name':'A220-100', 'seating':'100-120', 'range':'3450' }```
- 3.3.4 Save read data from csv file to a new json file.  File content:
  ```json
  [  {"name": "A220-100", "seating": "100-120", "range": "3450"}, ... ]
  ```

## 3.4 Unit tests

- 3.4.1 Write the code above into a function: 'aircrafts_csv_to_json(csvin, jsonout)'.  
- 3.4.2 Write a unit test that will:
  - execute the function to create a json file
  - check the content of the file: read json file and check it contains the expected list 
  - delete the json file.
- 3.4.3 Execute the unit test from a main function.  
  `python3 tp3_script.py`
- 3.4.4 Execute test with pytest:
  - remove the previous __main__ test
  - `pip install pytest` if not done
  - `pytest tp3_script.py`
- 3.4.5 Change expected result from unit test (eg: rename A220-100 to A220-400)  
  Re-run pytest
