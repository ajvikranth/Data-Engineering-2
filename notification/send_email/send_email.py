from email.message import EmailMessage
import ssl
import smtplib
from string import Template
from config.config import config

# Function to send an email
def send_email(to_email:str,track_details:str)->None:
    track_details = str(track_details)
    sub='this track from viral 50 might suit your taste'
    body = """<h1>$track_details</h1> """
    body =Template(body).safe_substitute(track_details = track_details)

    # Get email credentials from the configuration
    from_email = config['from_email']
    email_pwd = config['email_pwd']
   
    em = EmailMessage()
    em["From"] = from_email # Set the sender email address
    em["To"] = to_email # Set the recipient email address
    em["Subject"] = sub # Set the email subject
    em.set_content(body,subtype='html') # Set the email body content

    # Create an SSL context
    context = ssl.create_default_context()

    # Connect to the SMTP server and send the email securely
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context =context) as smtp:
        
        smtp.login(from_email,email_pwd)
        smtp.sendmail(from_email,to_email,em.as_string())
    
if __name__ == "__main__":
    track_detail = {
        'rank':1,
        'album_name': 'Sequēns',
        'release_date': '2022-12-01',
        'track_in_album': 12,
        'artist_name': 'Archer Marsh', 
        'explicit': False,
        'id': '1o9JJeBKlVxQ9O4j5Qd4Vh', 
        'name': 'Give Me Everything - Stripped Down', 
        'popularity': 62
        }
    send_email('antonvikranth@gmail.com',track_detail)
