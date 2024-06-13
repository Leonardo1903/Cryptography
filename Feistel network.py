import random
import time

def feistel_function(right_half, sub_key):
    return right_half ^ sub_key

def feistel_encrypt(plaintext, sub_key, rounds):
    block_size = len(plaintext) // 2
    left_half, right_half = 0, 0

    for i in range(rounds):
        left_half = int(plaintext[:block_size])
        right_half = int(plaintext[block_size:])

        new_right_half = left_half ^ feistel_function(right_half, sub_key[i])
        left_half = right_half
        right_half = new_right_half

        plaintext = str(left_half) + str(right_half).zfill(block_size)

    return plaintext

def main():
    random.seed(time.time())
    rounds = int(input("Enter the number of rounds: "))

    sub_key = [random.randint(0, 15) for _ in range(rounds)]

    input("Press Enter to continue...")

    plaintext = input("Enter plaintext: ")

    ciphertext = feistel_encrypt(plaintext, sub_key, rounds)

    print("Ciphertext:", ciphertext)


main()

