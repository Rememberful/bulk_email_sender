import smtplib
from email.message import EmailMessage
import time
import os

# ----------------------------- Configuration -----------------------------

EMAIL_ADDRESS = "adii.utsav@gmail.com"
EMAIL_PASSWORD = ""
EMAIL_SUBJECT = "Cybersecurity Internship Application – Aditya Kumar"

ATTACHMENT_PATH = r'D:\Cybersecurity\codebit\Resume_edited_as_pratik\AdityaKumar_Cybersecurity_Resume.pdf'
ATTACHMENT_FILENAME = 'AdityaKumar_Cybersecurity_Resume.pdf'

MESSAGE_TEMPLATE = """
Dear {name},

I’m Aditya Kumar, a final-year B.Tech (IT) student at the Institute of Engineering and Management, Kolkata, with hands-on experience in cybersecurity, cloud security, and secure development practices.

I’m reaching out to explore an internship opportunity at {company}. My key projects include building a Python-based steganalysis tool for malware detection in images—featuring cryptographic hashing, entropy checks, and VirusTotal integration—and developing a session hijacking detection system for web applications using Flask. I’m currently contributing to security operations and compliance through internships at Noida Power Company Ltd. (SOC) and Nirveonx (Cybersecurity & AI/ML), where I’ve worked with SIEM tools, ISO 27001 controls, and vulnerability assessments.

My skill set spans penetration testing, malware analysis, security automation, and cloud services (AWS, Azure). I’m particularly interested in SOC workflows, red/blue team strategies, and scalable detection systems that combine security with automation.

Please find my resume attached. I’d be excited to contribute to your cybersecurity team and would appreciate the opportunity to discuss how my skills align with your current initiatives.

Warm regards,  
Aditya Kumar  
Phone: +91 7079487671  
Email: adii.utsav@gmail.com  
LinkedIn: linkedin.com/in/aditya-kumar-3241b6286  
GitHub: https://github.com/Rememberful

"""

# ----------------------------- Email Sender -----------------------------

def send_email(to_email, name, company):
    msg = EmailMessage()
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    recipient_name = name.strip() if name.strip() else "HR Team"
    body = MESSAGE_TEMPLATE.format(name=recipient_name, company=company)
    msg.set_content(body)

    if not os.path.exists(ATTACHMENT_PATH):
        return f"❌ Attachment file not found at {ATTACHMENT_PATH}"

    with open(ATTACHMENT_PATH, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=ATTACHMENT_FILENAME)

    for attempt in range(2):  # Try up to 2 times
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            return f"✅ Email sent successfully to {recipient_name} <{to_email}>"
        except smtplib.SMTPException as e:
            if attempt == 1:
                return f"❌ Failed to send to {to_email}: {e}"
            time.sleep(2)

# ----------------------------- Main Program -----------------------------

def main():
    print("=== Bulk Email Sender – Cybersecurity Internship Application ===\n")
    while True:
        to_email = input("Enter recipient's email address (leave blank to quit): ").strip()
        if not to_email:
            print("Exiting...")
            break

        name = input("Enter recipient's name (leave blank for HR Team): ").strip()
        company = input("Enter company name: ").strip()

        if not company:
            print("⚠️ Error: Company name is required.\n")
            continue

        result = send_email(to_email, name, company)
        print(result)
        time.sleep(2)  # Delay between emails to avoid Gmail throttling
        print()  # Blank line for readability

if __name__ == "__main__":
    main()
