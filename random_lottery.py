import random

def random_lottery_assignment():
    """
    Randomly assigns a total lottery amount among a specified number of participants.
    Each participant has a maximum limit for the lottery allocation.
    """
    # Ask for the total lottery amount and number of participants
    total_lottery_amount = int(input("Enter the total lottery amount: "))
    num_participants = int(input("Enter the number of participants: "))

    # Ask for the participants' names
    participants = []
    for i in range(num_participants):
        name = input(f"Enter participant {i+1}'s name: ")
        max_limit = int(input(f"Enter participant {i+1}'s maximum limit: "))
        participants.append({"name": name, "max_limit": max_limit, "allocated": 0})

    # Randomly allocate the lottery amount among the participants
    while total_lottery_amount > 0:
        participant_index = random.randint(0, num_participants - 1)
        participant = participants[participant_index]
        allocation = random.randint(0, min(total_lottery_amount, participant["max_limit"] - participant["allocated"], 100))
        participant["allocated"] += allocation
        total_lottery_amount -= allocation

    # Print the allocated amounts for each participant
    print("Lottery Allocation Results:")
    for participant in participants:
        print(f"{participant['name']} gets {participant['allocated']} units of the lottery amount.")

random_lottery_assignment()
