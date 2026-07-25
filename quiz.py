import random
question_set = [
    ["Who is the first Prime Minister of India?", "Jawaharlal Nehru", "Narendra Modi", "Atal Bihari Vajpayee", "Subhas Chandra Bose", 4],
    ["Who is known as the Iron Man of India?", "A. P. J. Abdul Kalam", "Sardar Vallabhbhai Patel", "Mahatma Gandhi", "S. Jaishankar", 2],
    ["What is the capital of India?", "Mumbai", "Kolkata", "New Delhi", "Chennai", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["Who wrote the Indian National Anthem?", "Bankim Chandra Chattopadhyay", "Rabindranath Tagore", "Sarojini Naidu", "Subhas Chandra Bose", 2],
    ["Which is the largest ocean in the world?", "Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", 3],
    ["How many players are there in a cricket team?", "9", "10", "11", "12", 3],
    ["Who is known as the Father of the Nation in India?", "Bhagat Singh", "Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", 3],
    ["Which is the national animal of India?", "Elephant", "Lion", "Tiger", "Leopard", 3],
    ["What is the currency of Japan?", "Won", "Yuan", "Yen", "Dollar", 3]
]
random.shuffle(question_set)
def kbc():
    print("Redirecting to the Game Kon Banega Crorepati(KBC)")
    name=input("Pleas Enter Your Name : ")
    print(f"Welcome {name} in this Game")
    qNo=0
    global score
    score=0
    for questionSet in question_set:
        qNo+=1
        print(f"{qNo}.",questionSet[0])
        print(f"A. {questionSet[1]}",f"B. {questionSet[2]}",f"C. {questionSet[3]}",f"D. {questionSet[4]}",sep="\n")
        ans=int(input("Enter the correct answer (1 for A/ 2 for B/ 3 for C/ 4 for D) : "))
        if ans==questionSet[5]:
            print("Correct.")
            score+=1
        else:
            print("Wrong Answer.",f"The correct answer is {questionSet[5]}")
kbc()
if sum==10:
    print("Congratulation ! You have become the Crorepati.")
else:
    print(f"Better Luck next time. {score} out of 10 questions are correct")