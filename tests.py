import re
from fe10_script_parser import Fe10ScriptParser
import os
import codecs

import yaml
#REQUIRED FOR TESTING: Input folder (taken from RD's Mess file) with list of .m files
#Then convert to YML using Lumina

file_directory = os.getcwd()+"/input"

def clean_sample(sample):
    for i in range(0, 12):
        sample = sample.replace(f"\\x0{i}", f"$({i})")

    escape_sequence_fixes = [
        (r"\a", 7),
        (r"\b", 8),
        (r"\f", 12),
        (r"\n", 10),
        (r"\t", 9),
        (r"\v", 11),
        (r"\r", 13)
    ]

    for sequence in escape_sequence_fixes:
        sample = sample.replace(sequence[0], f"$({sequence[1]})")
    sample = sample.replace("$(10)", "\\n")
    return sample

def compare_text(filename, dialogue_name, sample):
    sample = clean_sample(sample)


    converted = Fe10ScriptParser().convert_raw_message_to_pretty(sample)
    reconstructed = Fe10ScriptParser().convert_pretty_to_raw_message(converted)
    print(f"{filename} {dialogue_name} is reconstructed correctly: {sample == reconstructed}")
    return sample == reconstructed

def compare_text_verbose(sample):
    sample = clean_sample(sample)

    converted = Fe10ScriptParser().convert_raw_message_to_pretty(sample)

    print(converted)

    reconstructed = Fe10ScriptParser().convert_pretty_to_raw_message(converted)
    print("---")
    print("SAMPLE:")
    print(sample)
    print("=")
    print("RECONSTRUCTED:")
    print(reconstructed)
    print(f"Is reconstructed correctly: {sample == reconstructed}")




#message = open(file_directory + "/" + "c0000.yml", "r", encoding="shift_jis", errors="replace").read()

break_outer = False
for file in os.listdir(file_directory):
    if break_outer:
        break
    
    if file[-3:] != "yml":
        continue
    message = open(file_directory + "/" + file, "r", encoding="shift_jis", errors="replace").read()
    messages = re.findall(f'(\w+): "(.*?)"', message)

    for m in messages:
        result = compare_text(file, m[0], m[1])
        if result == False:
            compare_text_verbose(m[1])
            break_outer = True
            break

