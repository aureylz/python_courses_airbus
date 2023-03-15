import json
import csv
import os

# PART 3 - Aircrafts

# 3.1 Files

# 3.1.1

# save dict to file
with open("my_dict.json", "w") as jsonfile:
    json.dump(
        {"plane_1": "A220", "plane_2": "A320", "plane_3": "A330", "plane_4": "A350"},
        jsonfile,
        indent=2,
    )

# function reading key-values and save them into a json file


def save_as_json(**kwargs):
    print(
        """Create a function that accepts an unknown number of key / value parameters and save it as json"""
    )
    try:
        with open("my_dict.json", "wt") as json_file:
            json.dump({k: v for k, v in kwargs.items()}, json_file, indent=2)
    except (PermissionError, IOError) as ex:
        print(ex)


save_as_json(
    {"plane_1": "A220", "plane_2": "A320", "plane_3": "A330", "plane_4": "A350"}
)


# 3.1.2
with open("tp3_airbus_family.csv") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)  # skip header
    for line in reader:
        print(line)

# 3.1.3
titles = ["name", "seating", "range"]
with open("tp3_airbus_family.csv") as f:
    reader = csv.DictReader(f, titles)
    next(reader)  # skip header
    for line in reader:
        print(line)

# 3.1.4
# 3.1.4a Simple solution: build the list, and then record entire object at the end
titles = ["name", "seating", "range"]
aircrafts = []
with open("tp3_airbus_family.csv") as infile:
    reader = csv.DictReader(infile, titles)
    next(reader)  # skip header
    for line in reader:
        aircrafts.append(
            {"name": line["name"], "seating": line["seating"], "range": line["range"]}
        )
with open("tp3_airbus_family.json", "w") as outfile:
    outfile.write(json.dumps(aircrafts))

# 3.1.4b More complex: process and record line by line
titles = ["name", "seating", "range"]
with open("tp3_airbus_family.csv") as infile:
    reader = csv.DictReader(infile, titles)
    next(reader)  # skip header
    with open("tp3_airbus_family.json", "w") as outfile:
        first_line = True
        outfile.write("[\n")
        for line in reader:
            if not first_line:
                outfile.write(",\n")
            outfile.write(
                json.dumps(
                    {
                        "name": line["name"],
                        "seating": line["seating"],
                        "range": line["range"],
                    },
                    indent=4,
                )
            )
            first_line = False
        outfile.write("\n]")

# 3.2 Tests

# 3.2.1


def aircrafts_csv_to_json(csvin: str, jsonout: str):
    titles = ["name", "seating", "range"]
    aircrafts = []
    with open(csvin) as infile:
        reader = csv.DictReader(infile, titles)
        next(reader)  # skip header
        for line in reader:
            aircrafts.append(
                {
                    "name": line["name"],
                    "seating": line["seating"],
                    "range": line["range"],
                }
            )
    with open(jsonout, "w") as outfile:
        outfile.write(json.dumps(aircrafts))


# 3.2.2


def test_aircrafts_csv_to_json():
    jsontest = "tp3_conversion-test.json"
    aircrafts_csv_to_json(csvin="tp3_airbus_family.csv", jsonout=jsontest)
    expected_list = [
        {"name": "A220-100", "seating": "100-120", "range": "3450"},
        {"name": "A220-300", "seating": "120-150", "range": "3400"},
        {"name": "A319neo", "seating": "120-150", "range": "3650"},
        {"name": "A320neo", "seating": "150-180", "range": "3450"},
        {"name": "A321neo", "seating": "180-220", "range": "4000"},
        {"name": "A321XLR", "seating": "180-220", "range": "4700"},
        {"name": "A330-800", "seating": "220-260", "range": "8150"},
        {"name": "A330-900", "seating": "260-300", "range": "7200"},
        {"name": "A350-900", "seating": "300-350", "range": "8100"},
        {"name": "A350-1000", "seating": "350-410", "range": "8700"},
        {"name": "A380", "seating": "400-550", "range": "8000"},
    ]

    with open(jsontest) as infile:
        read_list = json.load(infile)  # read_list = json.loads(infile.read())
        assert read_list == expected_list

    if os.path.exists(jsontest):
        os.remove(jsontest)


# 3.2.3
if __name__ == "__main__":
    test_aircrafts_csv_to_json()
    print("test Ok")
