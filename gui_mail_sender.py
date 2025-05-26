#For the purpose of sending emails with a GUI interface
# Allows you to copy paste the emails and other details then automatically do rest job for all the pasted content
#Input: Just Name and Email
#Output: Email will be sent to the respective person


import smtplib
import ssl
import re
from email.message import EmailMessage
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Email credentials
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""
ATTACHMENT_PATH = r"C:\Users\Aditya\OneDrive\Desktop\AdityaKumar_Cybersecurity_.pdf"
EMAIL_SUBJECT = "Cybersecurity Internship Application – Aditya Kumar"

# Email body template
MESSAGE_TEMPLATE = """
Dear {name},

I am Aditya Kumar, a fourth-year B.Tech IT student at the Institute of Engineering and Management, Kolkata. Along with cybersecurity and malware analysis, I have practical experience working with AWS cloud services, which I believe will help me contribute effectively to your projects.

I am writing to apply for a cybersecurity internship at your organization. My experience spans malware detection, steganalysis, penetration testing, and security automation, with hands-on projects involving session hijacking detection and image-based malware analysis using Python. I’ve also worked with tools like Metasploit, Wireshark, and VirusTotal to build automated detection pipelines.

I am particularly interested in SOC operations, as well as red and blue team methodologies. I enjoy tackling new challenges and am eager to contribute to real-world defensive and offensive security projects while learning from your team.

Please find my resume attached for your review. I would be excited to bring my skills and enthusiasm to your cybersecurity efforts.

Thank you for your time and consideration.

Sincerely,
Aditya Kumar  
Mobile: 
Email:  
LinkedIn: linkedin.com/in/aditya-kumar-3241b6286
"""

def send_email(to_email, name):
    msg = EmailMessage()
    msg["Subject"] = EMAIL_SUBJECT
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg.set_content(MESSAGE_TEMPLATE.format(name=name.strip() or "HR Team"))

    with open(ATTACHMENT_PATH, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="AdityaKumar_Cybersecurity_.pdf")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return f"✅ Sent to {name} <{to_email}>"
    except Exception as e:
        return f"❌ Failed to send to {to_email}: {e}"

def process_emails(input_text, output_box):
    output_box.delete(1.0, tk.END)
    lines = input_text.strip().splitlines()

    if not lines:
        messagebox.showwarning("No Input", "Please enter at least one name-email line.")
        return

    for line in lines:
        parts = re.split(r"\s+", line.strip())
        if len(parts) < 2:
            output_box.insert(tk.END, f"⚠️ Invalid line skipped: {line}\n")
            continue
        name = " ".join(parts[:-1])
        email = parts[-1]
        result = send_email(email, name)
        output_box.insert(tk.END, result + "\n")
        output_box.update()

def main_gui():
    root = tk.Tk()
    root.title("Cybersecurity Internship Mail Sender")
    root.geometry("720x540")

    tk.Label(root, text="Paste names and emails (e.g., John john@example.com)", font=("Arial", 12)).pack(pady=5)

    input_textbox = scrolledtext.ScrolledText(root, width=85, height=12, font=("Courier New", 10))
    input_textbox.pack(padx=10, pady=5)

    send_button = tk.Button(root, text="📧 Send Emails", font=("Arial", 12, "bold"),
                            command=lambda: process_emails(input_textbox.get("1.0", tk.END), output_box))
    send_button.pack(pady=10)

    tk.Label(root, text="Status Log:", font=("Arial", 12, "bold")).pack()
    output_box = scrolledtext.ScrolledText(root, width=85, height=10, font=("Courier New", 10), fg="green")
    output_box.pack(padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main_gui()
