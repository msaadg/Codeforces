def generate_sequence(a, b, k, n):
    if k <= 0:
        return []
    elif k == 1:
        if a == n:
            return [a]
        else:
            return []
    elif k == 2:
        if b == n:
            return [a, b]
        else:
            return []
    else:
        c = a + b
        if c > n:
            return []
        elif c == n and k == 3:
            return [a, b, c]
        else:
            sequences = []
            new_sequence = generate_sequence(b, c, k - 1, n)
            if new_sequence:
                sequences.extend([a] + new_sequence)
            new_sequence = generate_sequence(b, c, k - 2, n)
            if new_sequence:
                sequences.extend([a, b] + new_sequence)
            return sequences


def count_and_generate_sequences(n, k):
    count = 0
    print(f"Sequences with the {k}th element as {n}:")
    for i in range(1, k + 1):
        sequences = generate_sequence(0, 1, i, n)
        if sequences:
            count += 1
            print(sequences)
    print(f"Total number of sequences: {count}")


# Example usage:
n = 22
k = 4
count_and_generate_sequences(n, k)
