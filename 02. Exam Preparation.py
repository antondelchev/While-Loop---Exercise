unsuccessful_tries_limit = int(input())

command = ""
total_problems_solved = 0
total_score = 0
current_problem = ""
unsuccessful_tries_counter = 0

while command != "Enough":
    if command == "":
        problem_name = input()
    else:
        problem_name = command
    score = int(input())
    current_problem = problem_name
    total_score += score
    if score <= 4:
        unsuccessful_tries_counter += 1
        if unsuccessful_tries_counter == unsuccessful_tries_limit:
            break
    total_problems_solved += 1
    command = input()

average_score = total_score / total_problems_solved

if unsuccessful_tries_counter == unsuccessful_tries_limit:
    print(f"You need a break, {unsuccessful_tries_limit} poor grades.")
else:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {total_problems_solved}")
    print(f"Last problem: {current_problem}")
