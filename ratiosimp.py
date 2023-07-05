from fractions import Fraction
def simplify_ratio(ratio):
    parts = ratio.split(':')
    part1 = parts[0].strip()
    part2 = parts[1].strip()
    if ' ' in part2:
        whole, fraction = part2.split(' ')
        fraction = Fraction(fraction)
        mixed_fraction = Fraction(whole) + fraction
        part2 = str(mixed_fraction)
    if '%' in part1:
        part1 = float(part1.strip('%')) * 0.01
    if '.' in part1:
        part1 = Fraction(part1).limit_denominator()
    simplified_ratio = f'{part1}:{part2}'
    return simplified_ratio
mode = int(input("Choose mode: 1 for user input, 2 for pre-defined ratio: "))
if mode == 1:
    while True:
        ratio = input('Enter your ratio (or enter "q" to quit): ')
        if ratio.lower() == 'q':
            break
        simplified_ratio = simplify_ratio(ratio)
        while '/' in simplified_ratio:
            simplified_ratio = simplify_ratio(simplified_ratio)
        multiplier = float(simplified_ratio.split(':')[0]) / float(ratio.split(':')[0])
        print(f"Simplified Ratio: {simplified_ratio}")
        print(f"Multiplier: {multiplier}")
elif mode == 2:
    ratio = '0.75: 3 5/16'
    simplified_ratio = simplify_ratio(ratio)
    while '/' in simplified_ratio:
        simplified_ratio = simplify_ratio(simplified_ratio)
    multiplier = float(simplified_ratio.split(':')[0]) / float(ratio.split(':')[0])
    print(f"Simplified Ratio: {simplified_ratio}")
    print(f"Multiplier: {multiplier}")
else:
    print('Invalid mode selected. Exiting.')
