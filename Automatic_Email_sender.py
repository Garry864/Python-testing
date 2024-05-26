import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
# from pathlib import Path

# from dotenv import load_dotenv # pip install python-dotenv

port = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load the enviorment variables
# current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
# envars = current_dir/ ".env"
# load_dotenv(envars)

# Read the enviorment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

# Authentic_id

# sender_email = "aaravsingh86451@gmail.com"
# password_email = "qfqo qrlp azvw btnt"

def send_email(subject, reciever_mail, name, due_date, invoice_no, amount):
    # Create the base text message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = reciever_mail
    msg["Bcc"] = sender_email

    msg.set_content(
        f"""\
        Dear {name},
        This is a reminder that your invoice {invoice_no} is due on {due_date}. The total amount due is {amount}$.Please ensure that the payment is made by the due date to avoid any late fees.
        Thank you for your prompt attention to this matter.
        Best regards,
        Your Company Name
        """
    )
    # Add the html version that converts the message into a multipart/alternative

    # Set the email content with HTML
    html_content = f"""\
    <!DOCTYPE html>
    <html>
        <body>
            <p>Dear {name},</p>
            <p>This is a reminder that your invoice <strong>{invoice_no}</strong> is due on <strong>{due_date}</strong>. The total amount due is <strong>{amount}rs</strong>.</p>
            <p>Please ensure that the payment is made by the due date to avoid any late fees.</p>
            <p>Thank you for your prompt attention to this matter.</p>
            <p>Best regards,</p>
            <p>Your Company Name</p>
        </body>
    </html>
    """
    msg.add_alternative(html_content, subtype= 'html')

    with smtplib.SMTP(EMAIL_SERVER, port) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, reciever_mail, msg.as_string())

# if __name__ == "__main__":
#     send_email(
#         subject = "Invoice Remainder",
#         name = "John Doe",
#         reciever_mail = "gouravy86451@gmail.com",
#         due_date = "11, Aug 2023",
#         invoice_no = "INV-21-12-009",
#         amount = "5"
#     )