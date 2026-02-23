def gen_pw(pw_length: int, pw_cap: bool, pw_num: bool, pw_sym: bool) -> str:
    from random import choices, shuffle
    from string import ascii_lowercase, ascii_uppercase, digits

    chars = ascii_lowercase*3
    nums = 1
    punctuation = "!§$%&?#-=<>+"

    if pw_cap:
        nums += 1
        chars += ascii_uppercase*3
    if pw_num:
        nums += 1
        chars += digits*3
    if pw_sym:
        nums += 1
        chars += punctuation


    sec = choices(chars, k=pw_length-nums)+(choices(ascii_lowercase, k=1)+(choices(ascii_uppercase, k=1) if pw_cap else [])+(choices(digits, k=1)if pw_num else [])+(choices(punctuation, k=1) if pw_sym else []))
    shuffle(sec)
    return "".join(sec)

if __name__ == "__main__":
    print("Execute main pw_generator.py. This is just a helper file.")