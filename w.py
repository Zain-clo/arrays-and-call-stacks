from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Replace with your email credentials
sender_email = "your_email@gmail.com"
sender_password = "your_password"

@app.route('/submit-score', methods=['POST'])
def submit_score():
  data = request.get_json()
  score = data['score']

  # Send email notification
  receiver_email = "recipient_email@example.com"  # Replace with user's email
  message = MIMEText(f"Your quiz score is: {score}")
  message['Subject'] = "Quiz Results"
  message['From'] = sender_email
  message['To'] = receiver_email

  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, sender_password)
    smtp.send_message(message)

  return jsonify({'message': 'Score received and email sent'})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)