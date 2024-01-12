questions=[
    ["HTML stands for___________",
     "HyperText Markup Language", "HyperText Markp Language", "HyperText Markup Language", "Hyperext Markup Language",
     1],
    ["CSS stands for____________",
     "Cascading Style Sheet", "HyperText Markup Language", "HyperTet Markup Language", "Cascading stile sheet",
     1],
    ["DBMS stands for____________",
     "Database Management System", "Data Markup Language", "Data Base Management System", "Data Block Management System",
     1],
    ["SQL stands for____________",
     "Structured Query Language", "Sequential Query Language", "Simple Query Language", "Structured Question Language",
     1],
]

levels=[1,2,3,4,5,6]
score=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f'Level {levels[i]}')
    print(question[0])
    print(f'1.{question[1]}              2.{question[2]}')
    print(f'3.{question[3]}              4.{question[4]}')
    Answer=int(input("Enter your answer (1-4):"))
    if Answer==question[-1]:
        print("Correct Answer")
        print(f'your score is {score+1}')
        score+=1
    else:
        print("Wrong Answer")
        print(f'your score is {score}')