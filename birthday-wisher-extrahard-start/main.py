##################### Extra Hard Starting Project ######################
import csv
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import pandas
import random

MY_EMAIL = "saurabh1991Tidgam@gmail.com"
MY_PASSWORD = "pfwuzmcfoybatwam"

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
# birthday_dict = {(data_row[month], data_row[day]): data_row for (index, data_row) in data.iterrows()}

now = dt.datetime.now()
day = now.day
month = now.month
today_tuple = (month, day)

print(today_tuple)

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])\

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"subject:Happy Birthday!\n\n{contents}"
        )