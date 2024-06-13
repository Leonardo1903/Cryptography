def mangler_function(right_half, round_key):

    result = [0] * len(right_half)
    for i in range(len(right_half)):
        result[i] = right_half[i] ^ round_key[i]
    return result

# Example usage:
def user_input():
    try:
        right_half = input("Enter the right half (as a list of 0s and 1s, e.g., [1, 0, 1, 0, 0, 1]): ")
        right_half = [int(bit) for bit in right_half.strip('[]').split(',')]
        round_key = input("Enter the round key (as a list of 0s and 1s, e.g., [0, 1, 1, 0, 1, 0]): ")
        round_key = [int(bit) for bit in round_key.strip('[]').split(',')]

        if len(right_half) != len(round_key):
            raise ValueError("Lengths of right half and round key must match.")

        return right_half, round_key
    except ValueError as e:
        print(f"Error: {e}")
        return None, None

right_half, round_key = user_input()

if right_half is not None and round_key is not None:
    result = mangler_function(right_half, round_key)
    print("Mangler function output:", result)