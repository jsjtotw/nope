import re
from datetime import datetime
def change_date_format(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    pattern = r'(\d{1,2})/(\d{1,2})/(\d{2,4})'
    new_content = re.sub(pattern, r'\2/\1/\3', content)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
file_path = "WhatsApp Chat with AHS but it's 1C.txt"
change_date_format(file_path)
print("Finished! Lucas x Alden")
