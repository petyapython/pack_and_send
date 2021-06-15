import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email(my_email):
    fromaddr = my_email.fromaddr
    toaddr = my_email.toaddr
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Subject of the Mail"
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))
    filename = my_email.filepath.rpartition('\\')[-1]
    attachment = open(my_email.filepath, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(fromaddr, my_email.password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

def main(my_email):
    send_email(my_email)

if __name__ == '__main__':
    main(my_email)