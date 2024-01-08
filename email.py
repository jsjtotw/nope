import mechanize
import time

br = mechanize.Browser()

to = input("Enter the recipient address: ")
subject = input("Enter the subject: ")
print("Message: ")
message = input(">")

url = "http://anonymouse.org/anonemail.html"

# Set a user-agent
headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
br.addheaders = [('User-agent', headers)]

# Open the URL
br.open(url)

# Print the available forms for debugging
for i, form in enumerate(br.forms()):
    print(f"Form {i}:\n{form}")

# Select the form by its index
br.select_form(nr=0)  # Use the appropriate index based on your observation

# Fill in the form fields
br.form['to'] = to
br.form['subject'] = subject
br.form['text'] = message

# Add a delay before submitting the form
time.sleep(5)  # Adjust the delay as needed

# Submit the form
result = br.submit()

# Read and decode the response
response = br.response().read().decode('utf-8')

# Check the response for success or failure
if "The e-mail has been sent anonymously!" in response:
    print("The email has been sent successfully!! \n The recipient will get it in 12 hours!!")
else:
    print("Failed to send email!")

# Print the response for debugging
print(response)
