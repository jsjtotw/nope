import os
from tqdm import tqdm
def generate_code(txt_path):
    code_lines = []
    with open(txt_path, 'r') as file:
        ascii_art = file.read()
        var_name = os.path.splitext(os.path.basename(txt_path))[0]
        code_lines.append(f"let {var_name} = \"{ascii_art}\"")
    return code_lines
def write_code(code_lines, output_file):
    with open(output_file, 'w') as file:
        for line in code_lines:
            file.write(f"{line}\n")
            var_name = line.split('=')[0].strip().split()[1]
            file.write(f"OLED.writeStringNewLine({var_name})\n")
def main(ascii_dir, output_file):
    code_lines = []
    files = [f for f in os.listdir(ascii_dir) if f.endswith(".txt")]
    with tqdm(total=len(files), desc='Converting ASCII files') as pbar:
        for filename in files:
            txt_path = os.path.join(ascii_dir, filename)
            code_lines.extend(generate_code(txt_path))
            pbar.update(1)
    write_code(code_lines, output_file)
if __name__ == "__main__":
    main("ascii_output", "ascii_code.txt")
