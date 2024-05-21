# Experimentando do Try/Except

try:
    with open('nonexistentfile.txt', 'r') as file:
        for _ in range(3):
            print(file.readline())
except FileNotFoundError as e:
    print(f"File not found: {e}")
except IOError as e:
    print(f"I/O error: {e}")