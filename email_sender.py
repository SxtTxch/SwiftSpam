import smtplib
import random
import uuid

# -----------------------------------------------------------------------------
# This code is intended for educational purposes only.
# It is prohibited to use, modify, or distribute this code for any malicious,
# illegal, or abusive activities.
# By using this code, you agree to use it responsibly and ethically.
# ---------------------------------------------------------------------------

# CONSTANT VALUES

limit = 99 
#-- Some SMTP Servers have a limit of e-mail sent per SMTP connection. Please adjust accordingly. If you don't know what's the limit, make it big and check the error.
#-- Often it's 100.
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "example@gmail.com"
sender_password = "password"
recipient_email = "example@gmail.com"

# LIST OF EMAIL SUBJECTS PICKED AT RANDOM
subjects = [
    "Count your days!",
    "Your time is up!",
    "Tick-tock!",
    "Beware!",
    "The end is near!",
    "Not a drill!",
    "A little surprise!",
    "Who's there?",
    "Hope you see this!",
    "Read me now!"
]

# LIST OF MESSAGES
messages = [
    "HAHAHAHAHAHAHAHA!",
    "Your clock is ticking!",
    "Beware of the shadows!",
    "It's coming for you!",
    "Run while you can!",
    "This is just the beginning!",
    "Hope you're ready!",
    "Surprise!",
    "Why so serious?",
    "Catch me if you can!"
]

def main():
    print("=== Email Sender ===")
    print("For educational use only. Do not misuse this tool.")

    email_count = 0

    while True:
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            for _ in range(limit):
                unique_id = str(uuid.uuid4())[:8]
                subject = f"{random.choice(subjects)} [ID: {unique_id}]"
                message_body = random.choice(messages)
                email_message = f"From: {sender_email}\nTo: {recipient_email}\nSubject: {subject}\n\n{message_body}"
                server.sendmail(sender_email, recipient_email, email_message)
                email_count += 1
                print(f"Email {email_count} sent successfully with subject: {subject} and message: {message_body}")
            server.quit()

        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()