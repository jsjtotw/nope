import random
def generate_ship_name(rheiaxyuwei1, rheiaxyuwei2):
    if rheiaxyuwei1.lower() == "joshua" or rheiaxyuwei2.lower() == "joshua":
        raise ValueError("Joshua is not allowed as a name, as it is against the grand creator.")      
    if " " in rheiaxyuwei1:
        rheiaxyuwei3 = rheiaxyuwei1.split()[0]
    else:
        rheiaxyuwei3 = rheiaxyuwei1[:len(rheiaxyuwei1)//2]       
    if " " in rheiaxyuwei2:
        rheiaxyuwei4 = rheiaxyuwei2.split()[-1]
    else:
        rheiaxyuwei4 = rheiaxyuwei2[len(rheiaxyuwei2)//2:]       
    if rheiaxyuwei2[0].isupper():
        rheiaxyuwei4 = rheiaxyuwei4.lower()       
    rheiaxyuwei = rheiaxyuwei3 + rheiaxyuwei4
    return rheiaxyuwei
while True:
    rheiaxyuwei1 = input("Enter the first name: ")
    rheiaxyuwei2 = input("Enter the second name: ")   
    try:
        rheiaxyuwei = generate_ship_name(rheiaxyuwei1, rheiaxyuwei2)
        print('Ship name:', rheiaxyuwei)
    except ValueError as e:
        print("Error:", str(e))
        break  
    choice = input("Do you want to end? (y/n) ")
    if choice.lower() == "y":
        break
    print('-------------')   
