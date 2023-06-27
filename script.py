from random import choices
from string import ascii_lowercase

AVAILABLE_CHARS = set(ascii_lowercase + ' ')

def str_xor(s1, s2):
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(s1, s2))

def get_binary_repr(s):
    return ''.join(f'{ord(c):08b}' for c in s)

def get_str_from_bin(s):
    return ''.join(chr(int(s[i:i+8], base=2)) for i in range(0, len(s), 8))

def generate_key_for(size):
    return ''.join(choices('01', k=size))

def log(title, value):
    print(f'{title}:\n{value}\n')

def main():
    print('Note: Only lowecase letters and spaces allowed')

    plain1_str = input('Plaintext 1: ')

    plain2_str = input('Plaintext 2: ')

    bad_chars = set(plain1_str + plain2_str) - AVAILABLE_CHARS

    if bad_chars:
        c = next(iter(bad_chars))
        print(f'Character not allowed: "{c}"')
        return

    print()

    plain_str_size = max(len(plain1_str), len(plain2_str))

    plain1_str = plain1_str.ljust(plain_str_size)
    plain2_str = plain2_str.ljust(plain_str_size)

    plain1_bin = get_binary_repr(plain1_str)
    log('Plain 1 bin', plain1_bin)

    plain2_bin = get_binary_repr(plain2_str)
    log('Plain 2 bin', plain2_bin)

    plain_bin_size = max(len(plain1_bin), len(plain2_bin))

    key = generate_key_for(plain_bin_size)
    log('Key', key)

    cipher1 = str_xor(plain1_bin, key)
    log('Cipher 1', cipher1)

    cipher2 = str_xor(plain2_bin, key)
    log('Cipher 2', cipher2)

    ciphers_xored = str_xor(cipher1, cipher2)
    log('Ciphers XORed', ciphers_xored)

    while True:
        try:
            guess_str = input('Guess (Ctrl+C to exit): ')
        except KeyboardInterrupt:
            print()
            print('Bye')
            break

        print()

        guess_bin = get_binary_repr(guess_str)
        log('Guess bin', guess_bin)

        guess_bin_size = len(guess_bin)

        if guess_bin_size > plain_bin_size:
            print('Guess is too long')
            continue

        attempts = set()

        for i in range(plain_bin_size - guess_bin_size):
            attempt_bin = str_xor(guess_bin, ciphers_xored[i:i+guess_bin_size])

            if attempt_bin in attempts:
                continue

            attempts.add(attempt_bin)

            attempt_str = get_str_from_bin(attempt_bin)

            if set(attempt_str).issubset(AVAILABLE_CHARS):
                print(f'Possible match found at position {i}:')
                print(f'"{attempt_str}"')
                print()

if __name__ == '__main__':
    main()
