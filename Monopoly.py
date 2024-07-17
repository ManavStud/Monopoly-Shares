import openpyxl

# Load the workbook and select the active sheet
workbook = openpyxl.load_workbook('Balance.xlsx')
sheet = workbook.active

# Define the cell locations for each player
cell_locations = {
    'Player 1': {
        'Cash': 'B4',
        'Property Value': 'B5',
        'Share Price': 'B6',
        'Equity Value': 'B7',
        'Number of Shares': 'B8',
        'Foreign Shares': 'B9',
        'Net Worth': 'B10',
        'Turns Played': 'B11',
        'Debt Taken': 'B14',
        'Debt Value to be Repaid': 'B15',
        'Debt Interest': 'B16',
        'Share Manipulation Price': 'B17',
        'Share Up/Down %': 'B18',
        'Player 1 Shares':'B22',
        'Player 2 Shares':'B23',
        'Player 3 Shares':'B24',
        'Player 4 Shares':'B25',
        'Player 5 Shares':'B26',
    },
    
    'Player 2': {
        'Cash': 'C4',
        'Property Value': 'C5',
        'Share Price': 'C6',
        'Equity Value': 'C7',
        'Number of Shares': 'C8',
        'Foreign Shares': 'C9',
        'Net Worth': 'C10',
        'Turns Played': 'C11',
        'Debt Taken': 'C14',
        'Debt Value to be Repaid': 'C15',
        'Debt Interest': 'C16',
        'Share Manipulation Price': 'C17',
        'Share Up/Down %': 'C18',
        'Player 1 Shares':'C22',
        'Player 2 Shares':'C23',
        'Player 3 Shares':'C24',
        'Player 4 Shares':'C25',
        'Player 5 Shares':'C26',
    },
    
    'Player 3': {
        'Cash': 'D4',
        'Property Value': 'D5',
        'Share Price': 'D6',
        'Equity Value': 'D7',
        'Number of Shares': 'D8',
        'Foreign Shares': 'D9',
        'Net Worth': 'D10',
        'Turns Played': 'D11',
        'Debt Taken': 'D14',
        'Debt Value to be Repaid': 'D15',
        'Debt Interest': 'D16',
        'Share Manipulation Price': 'D17',
        'Share Up/Down %': 'D18',
        'Player 1 Shares':'D22',
        'Player 2 Shares':'D23',
        'Player 3 Shares':'D24',
        'Player 4 Shares':'D25',
        'Player 5 Shares':'D26',
    },
    
    'Player 4': {
        'Cash': 'E4',
        'Property Value': 'E5',
        'Share Price': 'E6',
        'Equity Value': 'E7',
        'Number of Shares': 'E8',
        'Foreign Shares': 'E9',
        'Net Worth': 'E10',
        'Turns Played': 'E11',
        'Debt Taken': 'E14',
        'Debt Value to be Repaid': 'E15',
        'Debt Interest': 'E16',
        'Share Manipulation Price': 'E17',
        'Share Up/Down %': 'E18',
        'Player 1 Shares':'E22',
        'Player 2 Shares':'E23',
        'Player 3 Shares':'E24',
        'Player 4 Shares':'E25',
        'Player 5 Shares':'E26',
    },
    
    
    'Player 5': {
        'Cash': 'F4',
        'Property Value': 'F5',
        'Share Price': 'F6',
        'Equity Value': 'F7',
        'Number of Shares': 'F8',
        'Foreign Shares': 'F9',
        'Net Worth': 'F10',
        'Turns Played': 'F11',
        'Debt Taken': 'F14',
        'Debt Value to be Repaid': 'F15',
        'Debt Interest': 'F16',
        'Share Manipulation Price': 'F17',
        'Share Up/Down %': 'F18',
        'Player 1 Shares':'F22',
        'Player 2 Shares':'F23',
        'Player 3 Shares':'F24',
        'Player 4 Shares':'F25',
        'Player 5 Shares':'F26',
    },
}

# Function to get cell value
def get_cell_value(cell):
    return sheet[cell].value

# Function to set cell value and save the workbook
def set_cell_value(cell, value):
    sheet[cell].value = value
    workbook.save('Balance.xlsx')

# Function to print the current state of the game
def print_game_state():
    players = list(cell_locations.keys())
    attributes = list(cell_locations['Player 1'].keys())

    header = ["Attribute"] + players
    print("{:<25} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*header))

    for attr in attributes:
        row = [attr]
        for player in players:
            cell = cell_locations[player][attr]
            row.append(get_cell_value(cell))
        print("{:<25} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*row))


def end_turn_without_increasing_turns(player):
    print(f"{player} has chosen to end their turn without increasing turns played.")

def apply_interest_to_debt(player):
    debt_taken_cell = cell_locations[player]['Debt Taken']
    current_debt = get_cell_value(debt_taken_cell)
    interest_rate = 0.05  # Example interest rate of 5%
    
    if current_debt > 0:
        interest = current_debt * interest_rate
        new_debt = current_debt + interest
        set_cell_value(debt_taken_cell, new_debt)
        print(f"Applied interest to {player}'s debt. New debt value: {new_debt}")
    else:
        print(f"{player} has no outstanding debt to apply interest to.")

# Function to add cash
def add_cash(player):
    amount = float(input("Enter the amount of cash to add: "))
    cash_cell = cell_locations[player]['Cash']
    current_cash = get_cell_value(cash_cell)
    set_cell_value(cash_cell, current_cash + amount)

def buy_shares(player):
    seller = int(input("Enter the seller's no: "))
    company = int(input("Enter the company's shares you want to buy: "))
    quantity = int(input("Enter the quantity of shares to be bought: "))
    share_price_location = cell_locations[f'Player {company}']['Share Price']
    share_price = get_cell_value(share_price_location)
    total_buy_value = share_price * quantity
    buyer_cash = cell_locations[player]['Cash']
    current_cash = get_cell_value(buyer_cash)
    if current_cash < total_buy_value:
        print("Operation cannot be performed due to insufficient cash balance")
    else:
        seller_shares_loc = cell_locations[f'Player {seller}'][f'Player {company} Shares']
        seller_shares = get_cell_value(seller_shares_loc)
        print(f"Seller Shares Qty = {seller_shares}")
        if quantity <= seller_shares:
            own_shares_loc = cell_locations[player][f'Player {company} Shares']
            own_shares = get_cell_value(own_shares_loc)
            print(f"Buyer Shares Qty = {own_shares}")
            seller_cash_loc = cell_locations[f'Player {seller}']['Cash']
            seller_cash = get_cell_value(seller_cash_loc)
            set_cell_value(own_shares_loc, own_shares + quantity)
            set_cell_value(seller_shares_loc, seller_shares - quantity) 
            set_cell_value(buyer_cash, current_cash - total_buy_value)
            set_cell_value(seller_cash_loc, seller_cash + total_buy_value)
        else:
            print("Invalid Quantity")
        
        
    
# Function to withdraw cash
def withdraw_cash(player):
    cash_cell = cell_locations[player]['Cash']
    current_cash = get_cell_value(cash_cell)
    print(f"Current cash balance: {current_cash}")
    amount = float(input("Enter the amount of cash to withdraw: "))
    if amount > current_cash:
        print("Error: Withdrawal amount exceeds cash balance.")
    else:
        set_cell_value(cash_cell, current_cash - amount)

# Function to transfer cash
def transfer_cash(player):
    cash_cell = cell_locations[player]['Cash']
    current_cash = get_cell_value(cash_cell)
    print(f"Current cash balance: {current_cash}")
    amount = float(input("Enter the amount of cash to transfer: "))
    if amount > current_cash:
        print("Error: Transfer amount exceeds cash balance.")
        return
    
    transfer_to = int(input("Enter the player number to transfer to (2-5): "))
    if transfer_to < 1 or transfer_to > 5 or transfer_to == int(player[-1]):
        print("Error: Invalid player number.")
        return

    transfer_to_player = f"Player {transfer_to}"
    transfer_to_cash_cell = cell_locations[transfer_to_player]['Cash']
    transfer_to_current_cash = get_cell_value(transfer_to_cash_cell)

    set_cell_value(cash_cell, current_cash - amount)
    set_cell_value(transfer_to_cash_cell, transfer_to_current_cash + amount)

# Function to buy property
def buy_property(player):
    property_price = float(input("Enter the price of the property: "))
    cash_cell = cell_locations[player]['Cash']
    current_cash = get_cell_value(cash_cell)
    if property_price > current_cash:
        print("Error: Property price exceeds cash balance.")
        return
    
    property_value_cell = cell_locations[player]['Property Value']
    current_property_value = get_cell_value(property_value_cell)
    
    set_cell_value(cash_cell, current_cash - property_price)
    set_cell_value(property_value_cell, current_property_value + property_price)

# Function to sell property
def sell_property(player):
    property_price = float(input("Enter the price at which property is sold: "))
    buyer_player_no = int(input("Enter the player number buying this property (2-5): "))
    
    if buyer_player_no < 1 or buyer_player_no > 5 or buyer_player_no == int(player[-1]):
        print("Error: Invalid player number.")
        return
    
    buyer_player = f"Player {buyer_player_no}"
    buyer_cash_cell = cell_locations[buyer_player]['Cash']
    buyer_current_cash = get_cell_value(buyer_cash_cell)
    
    if property_price > buyer_current_cash:
        print("Error: Buyer does not have enough cash.")
        return
    
    buyer_property_value_cell = cell_locations[buyer_player]['Property Value']
    buyer_current_property_value = get_cell_value(buyer_property_value_cell)
    
    seller_cash_cell = cell_locations[player]['Cash']
    seller_current_cash = get_cell_value(seller_cash_cell)
    
    seller_property_value_cell = cell_locations[player]['Property Value']
    seller_current_property_value = get_cell_value(seller_property_value_cell)
    
    set_cell_value(buyer_cash_cell, buyer_current_cash - property_price)
    set_cell_value(buyer_property_value_cell, buyer_current_property_value + property_price)
    
    set_cell_value(seller_cash_cell, seller_current_cash + property_price)
    set_cell_value(seller_property_value_cell, seller_current_property_value - property_price)

# Function to take debt
def take_debt(player):
    debt_amount = float(input("Enter the amount of debt to take: "))
    debt_taken_cell = cell_locations[player]['Debt Taken']
    current_debt = get_cell_value(debt_taken_cell)
    net_worth_cell = cell_locations[player]['Net Worth']
    net_worth = get_cell_value(net_worth_cell)
    
    if current_debt + debt_amount > net_worth:
        print("Error: Total debt exceeds net worth.")
        return
    
    cash_cell = cell_locations[player]['Cash']
    current_cash = get_cell_value(cash_cell)
    
    set_cell_value(debt_taken_cell, current_debt + debt_amount)
    set_cell_value(cash_cell, current_cash + debt_amount)

# Function to repay debt
def repay_debt(player):
    debt_taken_cell = cell_locations[player]['Debt Taken']
    current_debt = get_cell_value(debt_taken_cell)
    cash_cell = cell_locations[player]['Cash']
    current_cash = get_cell_value(cash_cell)
    
    print(f"Current debt: {current_debt}")
    print(f"Current cash balance: {current_cash}")
    
    repay_amount = float(input("Enter the amount to repay: "))
    
    if repay_amount > current_cash:
        print("Error: Repayment amount exceeds cash balance.")
    elif repay_amount > current_debt:
        print("Error: Repayment amount exceeds outstanding debt.")
    else:
        set_cell_value(debt_taken_cell, current_debt - repay_amount)
        set_cell_value(cash_cell, current_cash - repay_amount)

# Main loop to perform operations
def main_loop():
    players = list(cell_locations.keys())

    while True:
        for player in players:
            while True:
                print(f"\n{player}'s turn")
                print("1. Add cash")
                print("2. Withdraw cash")
                print("3. Transfer cash")
                print("4. Buy property")
                print("5. Sell property")
                print("6. Take debt")
                print("7. Repay debt")
                print("8. Buy Shares")
                print("9. End turn")
                print("10. End turn without increasing number of turns")
                print("11. Apply Debt's interest")
                
                choice = input("Enter the number of the operation you want to perform: ")

                if choice == '1':
                    add_cash(player)
                elif choice == '2':
                    withdraw_cash(player)
                elif choice == '3':
                    transfer_cash(player)
                elif choice == '4':
                    buy_property(player)
                elif choice == '5':
                    sell_property(player)
                elif choice == '6':
                    take_debt(player)
                elif choice == '7':
                    repay_debt(player)
                elif choice == '9':
                    turns_played_cell = cell_locations[player]['Turns Played']
                    current_turns = get_cell_value(turns_played_cell)
                    set_cell_value(turns_played_cell, current_turns + 1)
                    break
                elif choice == '8':
                    buy_shares(player)
                elif choice == '10':
                    end_turn_without_increasing_turns(player)
                elif choice == '11':
                    apply_interest_to_debt(player)
            
                else:
                    print("Invalid choice. Please try again.")

        # Print the updated game state after each full round of turns
        print_game_state()

# Run the main loop
print_game_state()
main_loop()
