import smtplib
import datetime as dt
import random

#try:
email = "jane4241778@gmail.com"
password = "ikfglzbqqvlytbyq"
# connection = smtplib.SMTP("smtp.gmail.com",587)
# connection.starttls()
# connection.login(user=email, password=password)
# connection.sendmail(from_addr=email, to_addrs="janeabisha@yahoo.com", msg="Hello")
# connection.close()
# #except Exception as e:
#     #print(f"An error occurred: {e}")


now = dt.datetime.now()
week_of_day = now.weekday()
if week_of_day == 3:
    with open("quotes.txt") as file:
        data = file.readlines()
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="janeabisha@yahoo.com", msg=random.choice(data))
        connection.close()


