name = str(input("Enter Your Name : "))
print(f"{name} welcome to Show Kaun Banega Crorepati")

questions = ["1.which country is the most cleaned ?", " 2.Who  is the First Prime Minister of India ? ",
             "3.In india when notebandi happened  ? ",
             "4. on which date and month the gst  rule (Goods and Service Tax) is applied ?"]

Ans = ["Dubai", "Pandit Jawaharlal Nehru", "8 November 2016", "1 july 2017"]
print("\n")

R1 = 10000
R2 = 20000
R3 = 30000
R4 = 40000

Ans1 = input(questions[0])
print(Ans1)
if Ans1 == Ans[0]:
    print("-----------------------------------")
    print(f"{name}  this is the Correct Answer. You Played very well !! you won  ruppess {R1} ")
else:
    print("no This is the wrong Answer ")

print('\n')
Ans2 = input(questions[1])
print(Ans2)

if Ans2 == Ans[1]:
    print("-----------------------------------")
    print(f"\n {name}  this is the Correct Answer. You Played very well !! you won  ruppess {R2} ")
else:
    print("no This is the wrong Answer ")

print('\n')

Ans3 = input(questions[2])
print(Ans3)
if Ans3 == Ans[2]:
    print("-----------------------------------")
    print(f"\n {name}  this is the Correct Answer. You Played very well !! you won  ruppess {R3} ")
else:
    print("no This is the wrong Answer ")

print('\n')

Ans4 = input(questions[3])
print(Ans4)
if Ans4 == Ans[3]:
    print("-----------------------------------")
    print(f"\n {name}  this is the Correct Answer. You Played very well !! you won  ruppess {R4} ")
else:
    print("no This is the wrong Answer ")
