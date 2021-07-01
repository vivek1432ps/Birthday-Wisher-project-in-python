##################### Normal Starting Project ######################
import random
from datetime import datetime
import pandas

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.


today = datetime.now()
today_tuple = (today.month, today.day)

# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")


# Dictionary comprehension template for pandas DataFrame looks like this:
birthdays_dict = {(data.row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


# HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
                from_addr=my_email,
                to_addrs="vivekkurubaspvg99@gmail.com",
                msg=f"Subject:Monday Motivation\n\n {quote}"
            )


