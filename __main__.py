import random

def get_length() -> int:
    return random.randrange(14, 32)

def generate_password(length: int) -> str:
    s: list[str] = []

    characters: list[str] = [
        "abcdefghijklmnopqrstuvwxyz",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "0123456789",
        "!@#$%&*[](){}<>£€,.?"
    ]

    for _ in range(length):
        random.shuffle(characters)
        rand_n1: int = random.randrange(0, 4)
        rand_n2: int = random.randrange(len(characters[rand_n1]))

        s.append(characters[rand_n1][rand_n2])
    
    return "".join(s)

def main() -> None:
    password_len: int = get_length()
    password: str = generate_password(password_len)
    print(password)

if __name__ == "__main__":
    main()