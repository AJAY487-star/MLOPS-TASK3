with open("/root/accuracy.txt", "r") as f:
 acc=f.read()
import smtplib as sm
msg = "accuracy of the model is "+str(acc)+" percentage"
server=sm.SMTP_SSL("smtp.gmail.com", 465)
server.login("ajaysoul282@gmail.com","password")
server.sendmail("ajaysoul282@gmail.com","ajaysoul282@gmail.com", msg)
server.quit()