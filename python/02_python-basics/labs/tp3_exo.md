# Python basics - Hands on

## PART 3 - Aircrafts

### 3.1 Files

- 3.1.1 
  - Write a dictionary (eg: {'plane_1': 'A220', 'plane_2': 'A320', 'plane_3': 'A330', 'plane_4': 'A350'}) into a json file (eg: my_dict.json)
  -  💪 Create a function that accepts an unknown number of key / value parameters and save it as json
- 3.1.2 - Read csv file 'tp3_airbus_family.csv', print lines describing Airbus aircrafts.  
  eg: ```['A220-100', '100-120', '3450']```
- 3.1.3 Read again csv file 'tp3_airbus_family.csv', print each line as a json.  
  eg: ```{'name':'A220-100', 'seating':'100-120', 'range':'3450' }```
- 3.1.4 Save read data from csv file to a new json file.  Expected file content:
  ```json
  [  {"name": "A220-100", "seating": "100-120", "range": "3450"}, ... ]
  ```

### 3.2 Unit tests

- 3.2.1 Write the code above into a function: 'aircrafts_csv_to_json(csvin, jsonout)'.  
- 3.2.2 Write a unit test that will:
  - execute the function to create a json file
  - check the content of the file: read json file and check it contains the expected list 
  - delete the json file.
- 3.2.3 Execute the unit test from a main function.  
  `python3 tp3_script.py`
- 3.2.4 Execute test with pytest:
  - remove the previous __main__ test
  - `pip install pytest` if not done
  - `pytest tp3_script.py`
- 3.2.5 Change expected result from unit test (eg: rename A220-100 to A220-400)  
  Re-run pytest
