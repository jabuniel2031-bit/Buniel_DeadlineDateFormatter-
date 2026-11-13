from datetime import date

event = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = date(year, month, day)

print()
print("\nFormatted Output: ")
print("Event:", event)
print("Date:", event_date)
print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Weekday:", event_date)