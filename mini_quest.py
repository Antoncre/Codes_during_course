max_p = []
gained = []

questions = open('questions.txt', 'r')
questions_read = [line.strip() for line in questions.readlines()]
questions.close()
for question in questions_read:
    question_only = question.split('=')[0]
    answer_only = question.split('=')[1]
    answer = input(f"{question_only}=")
    if answer == answer_only:
        gained.append("1")
    else:
        pass
    max_p.append("1")   
m = len(max_p)
n = len(gained)

results = open('result.txt', 'w')
your_results = results.write(f"Your final score is {n}/{m}.")
results.close()
print(f"Your final score is {n}/{m}.")