import smtplib

my_email = "turkemre1966@gmail.com"
apppassword = "oxxulaqhiemnosgo"

connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email, password=apppassword)

connection.sendmail(from_addr=my_email,
                    to_addrs="turkemre5234@gmail.com", msg="Merhaba Emre")

connection.close()