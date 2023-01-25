from arxiv_file import PaperFeed
import yagmail
import pandas as pd

# read the excel file
df = pd.read_excel('people.xlsx')

for index, row in df.iterrows():
    email = yagmail.SMTP(user='',
                         password='')

    paper_feed = PaperFeed(query=row['interest'], length=10).get_paper()
    email.send(to=row['email'],
               subject=f"Your {row['interest']} paper for today",
               contents=f"Hi {row['name']}, \n \n "
                        f"See what's on about  {row['interest']} paper today. \n \n "
                        f"{paper_feed} \n \n "
                        f"Happy Reading \n "
                        f"Ayse,"
               )
