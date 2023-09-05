import requests
from datetime import datetime

# Get the current date in mm/dd/yyyy format
current_date = datetime.utcnow().strftime("%m/%d/%Y")

# Get the current time in Zulu format (XXXXZ)
current_time = datetime.utcnow().strftime("%H%MZ")

print("Enter your content. Type 'end' on a new line to finish.")

content_lines = []
while True:
    line = input()
    if line.lower() == 'end':
        break
    content_lines.append(line)

# Ask for a custom sign-off signature and quote
custom_signature = input("Enter your custom sign-off signature (leave empty to skip): ")
quote = input("Enter a quote (leave empty to skip): ")

# Initialize content with the date and time
content = f"START SEQUENCE\nDate: {current_date}\nTime: {current_time}\n\n"

# Add the content lines
content += '\n'.join(content_lines)

# Add the custom sign-off signature if provided
if custom_signature:
    content += f"\n---{custom_signature}---"

# Add the quote if provided
if quote:
    content += f"\n---{quote}---"

# Add "END SEQUENCE" at the very bottom
content += f"\n\nEND SEQUENCE\nDate: {current_date}\nTime: {current_time}"

payload = {
    "content": content
}

webhook_url = "bot webhook url here"
response = requests.post(webhook_url, json=payload)
