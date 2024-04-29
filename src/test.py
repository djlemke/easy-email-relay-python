from smtplib import SMTP

if __name__ == "__main__":
    fromaddr = "dlemke@netsusa.net"
    toaddr = "dlemke@netsusa.net"
    msg = f"From: {fromaddr}\r\nTo: {toaddr}\r\n\r\nTesting out the relay!"
    
    with SMTP("127.0.0.1", 25000) as smtp:
        smtp.set_debuglevel(1)
        smtp.sendmail(fromaddr, toaddr, msg)
        smtp.quit()