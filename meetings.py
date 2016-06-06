from datetime import datetime

import pytz
import random

timezones = random.sample(set(pytz.all_timezones), 6)
fmt = "%Y-%m-%d %H:%M %Z%z"

while True:
    date_input = input("""
        When is your meeting? Please use MM/DD/YYYY HH:MM format. """)
    try:
        local_date = datetime.strptime(date_input, "%m/%d/%Y %H:%M")
    except ValueError:
        print("{} doesn't seem to be a valid date & time".format(date_input))
    else:
        local_date = pytz.timezone("US/Pacific").localize(local_date)
        utc_date = local_date.astimezone(pytz.timezone("UTC"))

        output = []
        for timezone in timezones:
            output.append(utc_date.astimezone(pytz.timezone(timezone)))
        for appointment in output:
            print(appointment.strftime(fmt))
        break
