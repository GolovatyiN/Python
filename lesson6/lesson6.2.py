seconds_input = int(input("Enter number of seconds (from 0 to 8640000): "))

seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60

days = seconds_input // seconds_in_day
remaining = seconds_input % seconds_in_day

hours = remaining // seconds_in_hour
remaining = remaining % seconds_in_hour

minutes = remaining // seconds_in_minute
seconds = remaining % seconds_in_minute

if days % 10 == 1 and days % 100 != 11:
    day_label = "day"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_label = "days"
else:
    day_label = "days"

time_str = f"{str(hours).rjust(2, '0')}:{str(minutes).rjust(2, '0')}:{str(seconds).rjust(2, '0')}"

print(f"{days} {day_label}, {time_str}")