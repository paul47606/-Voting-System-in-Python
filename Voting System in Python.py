candidate1 = input("Enter 1st consistent name: ")
candidate2 = input("Enter 2n consistent name: ")
cand1_votes = 0
cand2_votes = 0
voters_id = [101, 102, 103, 104, 105, 106]
no_of_voters = len(voters_id)
print("number of voters:", no_of_voters)
voted = []

while True:
    if voters_id == []:
        print("Voting is over")
        if cand1_votes > cand2_votes:
            print(f"{candidate1} won the election with {cand1_votes}")
        elif cand2_votes > cand1_votes:
            print(f"{candidate2} won the election with {cand2_votes}")
        elif cand1_votes == cand2_votes:
            print("tied!!")
        break

    else:
        voter = int(input("Enter your id: "))
        if voter in voted:
            print("You already voted")

        else:
            if voter in voters_id:
                print(f"1. {candidate1} \n 2. {candidate2}")
                choice = int(input("Enter your choice"))

                if choice == 1:
                    cand1_votes = cand1_votes + 1
                    print(f"you voted {candidate1}")
                elif choice == 2:
                    cand2_votes = cand2_votes + 1
                    print(f"you voted {candidate2}")

                voters_id.remove(voter)
                voted.append(voter)

            else:
                print("you are not allowed to vote")

