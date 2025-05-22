def gen_pw(pw_length: int, pw_cap: bool, pw_num: bool, pw_sym: bool) -> str:
    from random import choices, shuffle
    from string import ascii_lowercase, ascii_uppercase, digits

    chars = ascii_lowercase*3
    punctuation = "!§$%&?#-=<>+"
    if pw_cap:
        chars += ascii_uppercase*3
    if pw_num:
        chars += digits*3
    if pw_sym:
        chars += punctuation

    sec = choices(chars, k=pw_length-4)+(choices(ascii_lowercase, k=1)+choices(ascii_uppercase, k=1)+choices(digits, k=1)+choices(punctuation, k=1))
    shuffle(sec)
    return "".join(sec)

if __name__ == "__main__":
    print("Execute main pw_generator.py. This is just a helper file.")