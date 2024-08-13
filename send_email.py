import smtplib  # Import the smtplib library to send emails using SMTP
import imghdr  # Import the imghdr library to determine the type of image
from email.message import EmailMessage  # Import the EmailMessage class to create email messages
from dotenv import load_dotenv
import os
# Load environment variables from a .env file
load_dotenv()

password = os.getenv("webpassword")  # Retrieve the sender email account's password from an environment variable
SENDER = "supremedocs19@gmail.com"  # The sender email address

RECEIVER = "da7338629@gmail.com"  # The receiver email address


def send_email(image_path):
    print("Send_email function started")
    email_message = EmailMessage()  # Create an EmailMessage object
    email_message["Subject"] = "New customer showed up!"  # Set the email subject
    email_message.set_content("Hey we saw a new customer!")  # Set the email content

    # Open the image file in binary read mode
    with open(image_path, "rb") as file:
        content = file.read()  # Read the content of the file

    # Add the image as an attachment to the email
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)  # Connect to the Gmail SMTP server
    gmail.ehlo()  # Identify ourselves to the SMTP server
    gmail.starttls()  # Secure the SMTP connection
    gmail.login(SENDER, password)  # Log in to the SMTP server using the sender's credentials
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())  # Send the email
    gmail.quit()  # Terminate the SMTP session
    print("send_email function ended")


if __name__ == "__main__":
    send_email(image_path="images/41.png")  # Test the send_email function with a sample image
