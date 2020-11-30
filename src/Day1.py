def find_first_repeating_freq(sequence):
    frequencies = set()
    current_freq = 0
    while True:
        for n in sequence:
            current_freq += int(n)
            if current_freq in frequencies:
                return current_freq
            frequencies.add(current_freq)


puzzle = open("../inputs/Day1.txt", "r").readlines()
freq = 0

for num in puzzle:
    freq += int(num)

expected_freq = 442
if freq == expected_freq:
    print(f"✅ Challenge Part 1 -> {freq}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_freq}, got {freq}")

expected_first_repeating_freq = 59908
first_repeating_freq = find_first_repeating_freq(puzzle)
if first_repeating_freq == expected_first_repeating_freq:
    print(f"✅ Challenge Part 2 -> {first_repeating_freq}")
else:
    print(f"❌ Challenge Part 2 -> Expected output {expected_first_repeating_freq}, got {first_repeating_freq}")
