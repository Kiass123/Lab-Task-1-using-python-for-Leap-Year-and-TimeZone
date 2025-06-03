#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# In[2]:


from datetime import datetime, timedelta

def convert_to_gmt():
    try:
        local_time_str = input("Enter local time in HH:MM format (24-hour): ")
        timezone_offset = float(input("Enter your timezone offset from GMT (e.g., +6, -4.5): "))

        today = datetime.today().date()
        local_time = datetime.strptime(local_time_str, "%H:%M")
        local_datetime = datetime.combine(today, local_time.time())

        gmt_datetime = local_datetime - timedelta(hours=timezone_offset)

        print("Corresponding GMT time:", gmt_datetime.strftime("%H:%M"))
    except Exception as e:
        print("Error:", e)

convert_to_gmt()


# In[13]:


pip list


# In[ ]:


import pytz
from datetime import datetime

def convert_sydney_to_gmt():
    sydney_tz = pytz.timezone('Australia/Sydney')
    gmt_tz = pytz.timezone('GMT')

    time_input = input("Enter time in Sydney (HH:MM, 24-hour format): ")

    try:
        user_time = datetime.strptime(time_input, "%H:%M")

        now = datetime.now()
        combined_dt = datetime(now.year, now.month, now.day, user_time.hour, user_time.minute)

        sydney_time = sydney_tz.localize(combined_dt)

        gmt_time = sydney_time.astimezone(gmt_tz)

        print(f"\nTime in Sydney: {sydney_time.strftime('%Y-%m-%d %H:%M')} (Australia/Sydney)")
        print(f"Corresponding GMT time: {gmt_time.strftime('%Y-%m-%d %H:%M')} (GMT+0)")

    except ValueError:
        print("Invalid time format. Please enter time in HH:MM format.")

convert_sydney_to_gmt()


# In[ ]:




