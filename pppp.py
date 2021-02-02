import smtplib
server = smtplib.SMTP('smtp.csus.com', 587)
server.starttls()
#enter email username
USER = raw_input("Enter your username: \n")

#enter email password
PASSWORD = raw_input("Enter your password: \n")

server.login(USER, PASSWORD)

#compose the subject/body of the email
subject = 'subject of email'
text = 'body of email'
message = "Subject: {}\n\n{}".format(subject, text)

#replace file.txt with the file name that has a list of email addesses
f = open("file.txt", "r")

for x in f:
    recipient = x
    server.sendmail(USER, recipient, message)

f.close()
server.close()
