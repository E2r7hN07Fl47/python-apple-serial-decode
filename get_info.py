import requests
from consts import URL, YEARS, WEEKS, LOCATIONS

serial = input("Enter serial nubmer: ")
print()

if len(serial) == 11:
    new_serial = False
elif len(serial) == 12:
    new_serial = True
else:
    input("Not valid serial. Press enter to exit...")
    raise SystemExit

if new_serial:
    serial_loc = serial[:3]
    serial_year = serial[3:4]
    serial_week = serial[4:5]
    serial_line = serial[5:8]
    serial_prod = serial[8:12]
else:
    serial_loc = serial[:2]
    serial_year = serial[2:3]
    serial_week = serial[3:5]
    serial_line = serial[5:8]
    serial_prod = serial[8:11]

response = requests.get(URL+serial_prod).text

print_name = "Unknown"

for line in response.split('\n'):
    if "s.prop17 = '" in line:
        print_name = line.split("'")[1]
        break

print_year, is_second_part = YEARS.get(serial_year[0], ("Unknown", False))
if isinstance(print_year, int) and "201" in print_name:
    try:
        model_year = int(print_name.split('(')[1].split(', ')[1].replace(')', ''))
        if print_year < model_year:
            print_year += 10
    except:
        pass

if new_serial:
    print_week = WEEKS[serial_week]
    if is_second_part:
        print_week += 26
else:
    print_week = int(serial_week)

print_location = LOCATIONS.get(serial_loc, "Unknown")

print("Model:", print_name)
print("Year:", print_year)
print("Week:", print_week)
print("Location:", print_location)
print("Production line:", serial_line)
print()

input("Press enter to exit...")
