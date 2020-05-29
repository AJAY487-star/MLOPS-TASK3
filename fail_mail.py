import smtplib as sm
msg = "OS is terminated"
server=sm.SMTP_SSL("smtp.gmail.com", 465)
server.login("ajaysoul282@gmail.com"," password")
server.sendmail("ajaysoul282@gmail.com","ajaysoul282@gmail.com", msg)
server.quit()