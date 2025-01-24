amount = int(input("please enter your amount:"))

note1 = amount//100
note2 = (amount%100)//50
note3 =  ((amount%100)%50)//10
print(note1,note2,note3)