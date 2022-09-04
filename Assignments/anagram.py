score = int(input("Enter your score"))
if score >=70 and score <=100:
    print("grade is A")
if score >= 60 and score <= 69:
    print("grade is B")
if score >=50 and score <=59:
    print("grade is C")
if score >= 45 and score <= 49:
    print("grade is D")
if score >= 40 and score <=44:
    print("grade is E")
if score < 40 and score >=0:
    print("grade is f")
if score < 0 or score > 100:
    print("invalid score")