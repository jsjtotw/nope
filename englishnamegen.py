import pandas as pd
import random
df = pd.read_csv('https://raw.githubusercontent.com/hadley/data-baby-names/master/baby-names.csv')
df['percent'] = df['percent'] / 100
df['percent'] = df['percent'] / df['percent'].sum()
def generate_random_name(names_generated, sex=None):
    remaining_names = df[df['sex'] == sex] if sex else df
    remaining_names = remaining_names[~remaining_names['name'].isin(names_generated)]
    if remaining_names.empty:
        return None
    return random.choices(remaining_names['name'], weights=remaining_names['percent'], k=1)[0]
num_names = int(input("Enter the number of names to generate: "))
sex = ''
generated_names = []
while len(generated_names) < num_names:
    name = generate_random_name(generated_names, sex)
    if name:
        generated_names.append(name)
for name in generated_names:
    person_sex = df.loc[df['name'] == name, 'sex'].values[0]
    print(f"{name} ({person_sex})")
