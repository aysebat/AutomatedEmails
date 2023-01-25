import datetime
from arxiv_file import PaperFeed
import yagmail
import pandas as pd
import time


def send_email():
    email = email_setting()
    paper_feed = PaperFeed(query=row['interest'], length=10).get_paper()
    email.send(to=row['email'],
               subject=f"Your {row['interest']} paper for today",
               contents=f"Hi {row['name']}, \n \n "
                        f"See what's on about  {row['interest']} paper today. \n \n "
                        f"{paper_feed} \n \n "
                        f"Happy Reading \n "
                        f"Ayşe Bat,"
               )


def email_setting():
    """Email settings for the app"""
    email = yagmail.SMTP(user='',
                         password='')
    return email


while True:
    executing_time = datetime.time(8, 36, 00)
    if executing_time:
        print("Executing...")
        # read the Excel file
        df = pd.read_excel('people.xlsx')
        for index, row in df.iterrows():
            send_email()
    time.sleep(60)
