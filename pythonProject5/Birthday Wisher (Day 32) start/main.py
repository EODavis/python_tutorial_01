import smtplib
import datetime as dt
import random

my_email = "immanueldavis1@gmail.com"
password = 'rkqhdrjnstbiumdj'

now = dt.datetime.now()
daily = now.hour
if daily == 8:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=[my_email, "davislamide@gmail.com"],
            msg=f"Subject: Daily Motivation\n\n{quote}"
        )



