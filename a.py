#Allows you to copy paste the emails and other details thenautomatically do rest job for all the pasted content 

import smtplib
from email.message import EmailMessage
import ssl
import re

# Your email credentials
EMAIL_ADDRESS = "adii.utsav@gmail.com"
EMAIL_PASSWORD = "johfxayebkbrcgxd"

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
Mobile: +91 7079487671
Email: adii.utsav@gmail.com
LinkedIn: linkedin.com/in/aditya-kumar-3241b6286
"""

ATTACHMENT_PATH = r'C:\Users\Aditya\OneDrive\Desktop\AdityaKumar_Cybersecurity_.pdf'

def send_email(to_email, name, company):
    msg = EmailMessage()
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    body = MESSAGE_TEMPLATE.format(name=name, company=company)
    msg.set_content(body)

    with open(ATTACHMENT_PATH, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename='AdityaKumar_Cybersecurity_.pdf')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"✅ Sent to {name} <{to_email}>")
    except Exception as e:
        print(f"❌ Error sending to {to_email}: {e}")

def main():
    print("Paste all person details below, each on a new line, in this format:")
    print("1\tAditya Kumar\triya.sharma@example.com\tHR Manager\tGlobussoft")
    print("2\tUtsav\tamit.patel@example.com\tTalent Acquisition\tTech Mahindra")
    print("3\tSneha Roy\tsneha.roy@example.com\tRecruitment Lead\tWipro")
    print("Paste a blank line to finish input.\n")

    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line.strip())

    for line in lines:
        # Split by tabs or multiple spaces
        parts = line.split('\t')
        if len(parts) < 5:
            parts = re.split(r'\s{2,}', line)
        if len(parts) < 5:
            print(f"⚠️ Invalid line skipped: {line}")
            continue

        _, name, email, _, company = parts
        send_email(email, name, company)

if __name__ == "__main__":
    main()
