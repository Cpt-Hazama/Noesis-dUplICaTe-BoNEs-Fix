import re


def remove_bone_prefix(smd_file):
    with open(smd_file, 'r') as f:
        lines = f.readlines()

    bone_lines = [line for line in lines if line.startswith('  ')]

    # Remove the stupid f#cking "boneXXXX_" prefix that Noesis adds
    modified_lines = []
    for line in bone_lines:
        match = re.search(r'bone\d{4}_(\w+)', line)
        if match:
            modified_line = line.replace(match.group(), match.group(1))
            modified_lines.append(modified_line)
        else:
            modified_lines.append(line)

    for i, line in enumerate(lines):
        if line.startswith('  '):
            lines[i] = modified_lines.pop(0)

    output_file = smd_file.split('.')[0] + '_fixed.smd'
    with open(output_file, 'w') as f:
        f.writelines(lines)

    print(f"Modified SMD file saved as: {output_file}")


# Example usage
smd_file = input(
    "Enter the SMD file (just put it in the script directory and type the file name): ")
remove_bone_prefix(smd_file)
