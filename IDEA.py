def IDEAEncrypt(plaintext, key):
    rounds = 8
    modulus = 0x10001

    for i in range(rounds):
        plaintext[0] = (plaintext[0] * key[i]) % modulus
        plaintext[1] = (plaintext[1] + key[i + 8]) % modulus
        plaintext[2] = (plaintext[2] + key[i + 16]) % modulus
        plaintext[3] = (plaintext[3] * key[i + 24]) % modulus

        tmp1 = plaintext[0] ^ plaintext[2]
        tmp2 = plaintext[1] ^ plaintext[3]

        tmp1 = (tmp1 * key[i + 32]) % modulus
        tmp2 = (tmp2 + tmp1) % modulus
        tmp2 = (tmp2 * key[i + 40]) % modulus
        tmp1 = (tmp1 + tmp2) % modulus

        plaintext[0] ^= tmp2
        plaintext[2] ^= tmp1

        tmp3 = plaintext[1] ^ plaintext[3]
        plaintext[1] = plaintext[2] ^ tmp2
        plaintext[2] = tmp3 ^ tmp1
        plaintext[3] = tmp2 ^ tmp3

        # Print intermediate values
        print("Round", i + 1, "Output: ", end="")
        for j in range(4):
            print(hex(plaintext[j]), end=" ")
        print()

    plaintext[0] = (plaintext[0] * key[48]) % modulus
    plaintext[1] = (plaintext[1] + key[49]) % modulus
    plaintext[2] = (plaintext[2] + key[50]) % modulus
    plaintext[3] = (plaintext[3] * key[51]) % modulus

    # Print final round output
    print("Final Round Output: ", end="")
    for j in range(4):
        print(hex(plaintext[j]), end=" ")
    print()

plaintext = [0x1234, 0x5678, 0x9abc, 0xdef0]
key = [0x0123, 0x4567, 0x89ab, 0xcdef, 0x0123, 0x4567, 0x89ab, 0xcdef,
       0x0123, 0x4567, 0x89ab, 0xcdef, 0x0123, 0x4567, 0x89ab, 0xcdef,
       0x0123, 0x4567, 0x89ab, 0xcdef, 0x0123, 0x4567, 0x89ab, 0xcdef,
       0x0123, 0x4567, 0x89ab, 0xcdef, 0x0123, 0x4567, 0x89ab, 0xcdef,
       0x0123, 0x4567, 0x89ab, 0xcdef, 0x0123, 0x4567, 0x89ab, 0xcdef,
       0x0123, 0x4567, 0x89ab, 0xcdef, 0x0123, 0x4567, 0x89ab, 0xcdef,
       0x0123, 0x4567, 0x89ab, 0xcdef, 0x0123, 0x4567, 0x89ab, 0xcdef,
       0x0123, 0x4567, 0x89ab, 0xcdef, 0x0123, 0x4567, 0x89ab, 0xcdef,
       0x0123, 0x4567, 0x89ab, 0xcdef, 0x0123, 0x4567, 0x89ab, 0xcdef,
       0x0123, 0x4567, 0x89ab, 0xcdef, 0x0123, 0x4567, 0x89ab, 0xcdef,
       0x0123, 0x4567, 0x89ab, 0xcdef, 0x0123, 0x4567, 0x89ab, 0xcdef,
       0x0123, 0x4567, 0x89ab, 0xcdef, 0x0123, 0x4567, 0x89ab, 0xcdef]

IDEAEncrypt(plaintext, key)