import pandas as pd
import random
from xpinyin import Pinyin
def generate_random_names(num_names):
    df = pd.read_csv('https://raw.githubusercontent.com/psychbruce/ChineseNames/master/data-csv/givenname.csv')
    names = []
    genders = []
    for _ in range(num_names):
        gender = random.choice([-1, 1])
        filtered_df = df[df['name.gender'] == gender]
        if len(filtered_df) < 2:
            continue
        random_index_1 = random.randint(0, len(filtered_df) - 1)
        random_index_2 = random.randint(0, len(filtered_df) - 1)
        while random_index_2 == random_index_1:
            random_index_2 = random.randint(0, len(filtered_df) - 1)
        character_1 = filtered_df.iloc[random_index_1]['character']
        character_2 = filtered_df.iloc[random_index_2]['character']
        names.append(character_1 + ' ' + character_2)
        genders.append('male' if gender == 1 else 'female')
    return names, genders
def transliterate_to_english(name):
    p = Pinyin()
    transliterated_parts = []
    for part in name.split(' '):
        transliterated_part = p.get_pinyin(part, tone_marks='numbers')
        transliterated_part = transliterated_part.replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5')  , '')
        transliterated_parts.append(transliterated_part.capitalize())
    transliterated_name = ' '.join(transliterated_parts)
    return transliterated_name
num_names = int(input('Enter the number of names to generate: '))
random_names, random_genders = generate_random_names(num_names)
for i in range(len(random_names)):
    name = random_names[i]
    gender = random_genders[i]
    transliterated_name = transliterate_to_english(name)
    print(f"{transliterated_name}, ({gender.capitalize()})")
