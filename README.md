# AutomatedEmails
This OOP Python Project send a peper from arxiv. 

* arxiv_file  has the PaperFeed class that is responsible for scraping the arxiv and create spesific search query.
  * The query information is gettign from the people.csv file in the manin.py
* main file responsible for sending email.
  * email_setting method set up the gmail for email sender
  * send_email method is the content for the email
  * while loop run for the time that set up for each morning and the sleep
  This project is orijinally from the [udemy course.](https://www.udemy.com/course/the-python-pro-course)
