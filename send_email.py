# install SSL certificate when SSL-error
# /Applications/Python/3.12/Install/Certificates.command with admin priveleges

import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username= "sergepille70@gmail.com"
password = "wooq cdbp lvkf yzpd"
receiver = "sergepille70@gmail.com"

my_context = ssl.create_default_context()
message = """\
Subject: Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)