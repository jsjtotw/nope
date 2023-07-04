import re
from datetime import datetime
def change_date_format(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    pattern = r'(\d{1,2})/(\d{1,2})/(\d{2,4})'
    new_content = re.sub(pattern, r'\2/\1/\3', content)
    with open(file_path, 'w') as file:
        file.write(new_content)
file_path = 'your_file_path.txt'
change_date_format(file_path)