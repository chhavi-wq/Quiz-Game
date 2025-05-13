print("----------------------------------------------------------------------------")
print("                    Welcome to the quiz :--                                 ")
print("                                                                            ")

questions=("What is the primary function of a computer's processing unit (CPU)?: ",
           "Which of the following is the example of secondary storage device?: ",
           "What does the acronym LAN stands for in computer networking?: ",
           "Which programming language is often used for web developement?: ",
           "What is the main purpose of an operating system (OS)?: ",
           "Which of the following is the type of computer virus?: ",
           "Which is the term for the process of using a computer to convert information into an encrypted form?: ",
           "What is the function of a firewall?: ",
           "What is the name of the first widely used computer?: ",
)
options=(("A.Storage of data","B.Processing and executing instructions","C.Connecting to the internet","D.Displaying output"),    
         ("A.RAM","B.ROM","C.Hard disk drive","D.CPU"),        
         ("A.Local Area Network","B.Long Area Network","C.Large Area Network","D.Low Area Network"),
         ("A.C++","B.Java","C.Python","D.Javascript"),
         ("A.To run specific applications","B.To manage hardware and software resources","C.To store data permanently","D.To connect to the internet"),
         ("A.Malware","B.Antivirus","C.Firewall","D.Security patch"),
         ("A.Compression","B.Decryption","C.Encryption","D.Formatting"),
         ("A.To block unauthorized access to a network","B.To compress files","C.To run applications","D.To display output"),
         ("A.ENIAC","B.UNIVAC","C.IBM 360","D.Macintosh"))
answers=("B","C","A","D","B","A","C","A","A")
guesses=[]
score=0
question_number=0

for question in questions:
    print("-------------------------------------------------------------")
    print(question)

    for option in options[question_number]:
        print(option)

    guess=input("Enter the guess(A,B,C,D): ").upper()
    guesses.append(guess)

    if guess==answers[question_number]:
        score+=1
        print("Correct..")

    
    else:
        print("Incorrect..")
        print(f"The correct answer is:  {answers[question_number]}")

    question_number+=1

print("------------------------------------------------------------------")
print("                           RESULTS                                ")
print("------------------------------------------------------------------")
print("answers: ",end=" ")
for answer in answers:
    print(answer,end=" ")
print()
print("guesses: ",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()
score=int(score/len(questions)*100)
print(f"Your score is: {score}%")

