width = int(input())
length = int(input())

total_pieces = width * length

command = input()

while command != "STOP":
    number_of_pieces = int(command)
    total_pieces -= number_of_pieces

    if total_pieces < 0:
        break
    command = input()

difference = abs(total_pieces)

if total_pieces >= 0:
    print(f"{difference} pieces are left.")
else:
    print(f"No more cake left! You need {difference} pieces more.")
