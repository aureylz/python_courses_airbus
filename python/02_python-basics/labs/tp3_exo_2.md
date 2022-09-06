# Python basics - Hands on

## 03 - Airbus commercial family

### 3.1 Files (csv, json)
3.1.1 Read csv file 'tp3_airbus_family.csv', print lines describing Airbus aircrafts.  
eg: ['A220-100', '100-120', '3450']

3.1.2 Read again csv file 'tp3_airbus_family.csv', print each line as a json.  
eg: { 'name':'A220-100', 'seating':'100-120', 'range':'3450' } 

3.1.3 Save read data from csv file to a new json file.  File content:  
```json
[  {"name": "A220-100", "seating": "100-120", "range": "3450"}, ... ]
```

### 3.2 Unit tests

3.2.1 Write the code above into a function: 'aircrafts_csv_to_json(csvin, jsonout)'.  

3.2.2 Write a unit test that will:
- execute the function to create a json file
- check the content of the file: read json file and check it contains the expected list 
- delete the json file.

3.2.3 Execute the unit test from a main function.  
`python3 tp3_script.py`

3.2.4 Execute test with pytest:
- remove the previous __main__ test
- `pip install pytest` if not done
- `pytest tp3_script.py`

3.2.5 Change expected result from unit test (eg: rename A220-100 to A220-400)  
Re -run pytest
