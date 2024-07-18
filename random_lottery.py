import random

def random_lottery_assignment():
    # Ask for the total lottery amount and number of participants
    total_lottery_amount = int(input("Enter the total lottery amount: "))
    num_participants = int(input("Enter the number of participants: "))

    # Ask for the participants' names
    participants = []
    for i in range(num_participants):
        name = input(f"Enter participant {i+1}'s name: ")
        participants.append(name)

    # Initialize a dictionary to store the allocated amounts for each participant
    allocated_amounts = {name: 0 for name in participants}

    # Randomly allocate the lottery amount among the participants
    while total_lottery_amount > 0:
        participant_index = random.randint(0, num_participants - 1)
        participant_name = participants[participant_index]
        allocation = random.randint(0, min(total_lottery_amount, 100))  # limit allocation to 100 units max
        allocated_amounts[participant_name] += allocation
        total_lottery_amount -= allocation

    # Print the allocated amounts for each participant
    for name, amount in allocated_amounts.items():
        print(f"{name} gets {amount} units of the lottery amount.")

random_lottery_assignment()
