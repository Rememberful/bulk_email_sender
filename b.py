import smtplib
from email.message import EmailMessage
import ssl

# Your email credentials
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""

EMAIL_SUBJECT = "Cybersecurity Internship Application – Aditya Kumar"

MESSAGE_TEMPLATE = """
Dear {name},

I am Aditya Kumar, a third-year B.Tech IT student at the Institute of Engineering and Management, Kolkata. Along with cybersecurity and malware analysis, I have practical experience working with AWS cloud services, which I believe will help me contribute effectively to your projects.

I am writing to apply for a cybersecurity internship at {company}. My experience spans malware detection, steganalysis, penetration testing, and security automation, with hands-on projects involving session hijacking detection and image-based malware analysis using Python. I’ve also worked with tools like Metasploit, Wireshark, and VirusTotal to build automated detection pipelines.

I am particularly interested in SOC operations, as well as red and blue team methodologies. I enjoy tackling new challenges and am eager to contribute to real-world defensive and offensive security projects while learning from your team.

Please find my resume attached for your review. I would be excited to bring my skills and enthusiasm to your cybersecurity efforts.

Thank you for your time and consideration.

Sincerely,
Aditya Kumar
Mobile: 
Email: 
LinkedIn: linkedin.com/in/aditya-kumar-3241b6286
"""

ATTACHMENT_PATH = r'C:\Users\Aditya\OneDrive\Desktop\AdityaKumar_Cybersecurity_.pdf'

def send_email(to_email, name, company):
    msg = EmailMessage()
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    recipient_name = name.strip() if name.strip() else "HR Team"
    body = MESSAGE_TEMPLATE.format(name=recipient_name, company=company)
    msg.set_content(body)

    with open(ATTACHMENT_PATH, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename='AdityaKumar_Cybersecurity_.pdf')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"✅ Email sent successfully to {recipient_name} <{to_email}>")
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")

def main():
    while True:
        to_email = input("Enter recipient's email address (leave blank to quit): ").strip()
        if not to_email:
            print("Exiting...")
            break
        name = input("Enter recipient's name (leave blank for HR Team): ").strip()
        company = input("Enter company name: ").strip()

        if not company:
            print("Error: Company name is required!")
            continue

        send_email(to_email, name, company)
        print()  # Blank line for readability

if __name__ == "__main__":
    main()
