# ex23 Strings, bytes and character encoding

import sys
script, encoding, errors = sys.argv

def main(language_file, encoding, error):
    line = language_file.readline()
    if line:
        print_DBES(line, encoding, error)
        return main(language_file, encoding, error)

def print_DBES(line, encoding, error):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, error)
    cooked_string = raw_bytes.decode(encoding, error)
    print(raw_bytes, "<--->", cooked_string)


languages = open("ex23_languages.txt", encoding="utf-8")

main(languages, encoding, errors)
    
    
    
