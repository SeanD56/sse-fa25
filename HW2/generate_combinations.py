import itertools
import string
import hashlib
import glob

def createFile(cracked_passwords):
    with open("cracked_passwords.txt", "w", encoding="utf-8") as f:
        for pwd in cracked_passwords:
            f.write(f"{pwd}\n")

    return f

def generate_combinations(length):
    characters = string.ascii_letters + string.digits + '&@#'
    for l in range(3, length + 1):
        for combination in itertools.product(characters, repeat=l):
            yield ''.join(combination)


def main():
    hashed_passwords = set()
    cracked_passwords = set()
    for filename in glob.glob("md5*"):       # matches any file starting with "md5"
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:                      
                    hashed_passwords.add(line)
    

    length = 5  
    for combo in generate_combinations(length):
        hashed_combo = hashlib.md5(combo.encode()).hexdigest()
        if len(cracked_passwords) >= 60:
            break
        if hashed_combo in hashed_passwords:
            cracked_passwords.add(combo)
            print(f"Match found: {len(cracked_passwords)} {combo} -> {hashed_combo}")

    fh = createFile(cracked_passwords)
    fh.close()

if __name__ == "__main__":
    main()