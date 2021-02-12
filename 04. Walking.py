goal = 10000
current_steps = 0

command = ""

while current_steps < goal:
    command = input()
    if command == "Going home":
        steps = int(input())
        current_steps += steps
        break
    else:
        steps = int(command)
        current_steps += steps

if current_steps >= goal:
    print("Goal reached! Good job!")
    if current_steps > goal:
        difference_above = current_steps - goal
        print(f"{difference_above} steps over the goal!")
else:
    difference_below = goal - current_steps
    print(f"{difference_below} more steps to reach goal.")
