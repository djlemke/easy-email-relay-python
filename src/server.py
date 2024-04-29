import asyncio
from aiosmtpd.controller import Controller
from smtplib import SMTP

class CustomHandler():
    async def handle_DATA(self, server, session, envelope):
        print("Data received")
        peer = session.peer
        mail_from = envelope.mail_from
        rcpt_tos = envelope.rcpt_tos
        data = envelope.content

        with SMTP("mail.netsusa.net", 587) as smtp:
            print("Starting TLS")
            smtp.starttls()
            print("Attempting login")
            smtp.login("dlemke@netsusa.net", "Ylap.2005!")
            print("Sending mail")
            smtp.sendmail(mail_from, rcpt_tos, data)

        #if error_occured:
        #    return '500 Could not process your message'
        return '250 OK'

class Server():
    def __init__(self):
        self.handler = CustomHandler()
        self.controller = Controller(self.handler, hostname='127.0.0.1', port=25000)
    
    def start(self):
        print("Starting SMTP server")
        try:
            self.controller.start()
        except RuntimeError:
            self.controller = Controller(self.handler, hostname="127.0.0.1", port=25000)
            self.controller.start()
        except:
            print("shits broke")
    
    def stop(self):
        print("Stopping SMTP server")
        self.controller.stop()