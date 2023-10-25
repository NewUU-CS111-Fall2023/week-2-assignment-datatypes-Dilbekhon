"""
 Author: Dilbekkhon
 Date: 25-10-2023
 Name: Spawn prediction
"""


def is_dangerous(x, y):
    danger_zones = [(5, 5), (10, 10), (15, 15)]  # Example danger coordinates
    return (x, y) in danger_zones

def main():
    N = int(input("Enter the number of times to input coordinates: "))

    for _ in range(N):
        try:
            x = float(input("Enter X coordinate: "))
            y = float(input("Enter Y coordinate: "))
        except ValueError:
            print("Invalid input. Please enter numerical coordinates.")
            continue

        if is_dangerous(x, y):
            print("Character died!")
        else:
            print("Character survived!")

if __name__ == "__main__":
    main()
