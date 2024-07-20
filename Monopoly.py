import openpyxl
import json
from functools import reduce

# Load the workbook and select the active sheet
workbook = openpyxl.load_workbook('Balance.xlsx')
sheet = workbook.active

# Events to log:
# 1. Cash Transfers [x]
# 2. Share Transfers [x]

#### ---Cash transfers--- ####
cash_transfers = [
    # {
    #     'turn': 1,
    #     'debited_from': 1,
    #     'credited_to': 0, # 0 Implies Bank
    #     'amount': 1000
    # }
]


#### ---Share holding--- ####

share_transfers = [
    # {
    #     'turn': 1,
    #     'buyer': 1,
    #     'company': 2,
    #     'seller': 2,
    #     'quantity': 10,
    #     'price': 0.05
    # }
]

# Returns shares held before number of turns, set turns = turn for all holdings
def get_share_holding_before_turns(player, company, before_turns):
    player_shares = filter(
        lambda x : x['turn'] <= before_turns and x['company'] == company and (x['buyer'] == player or x['seller'] == player),
        share_transfers
    )

    def calculate_holdings(total, transaction):
        return total + transaction['quantity'] if transaction['buyer'] == player else total - transaction['quantity']

    return reduce(calculate_holdings, player_shares, 0)

def get_all_share_holding(player, players, before_turns):
    holdings = {}
    for company in players:
        share_company = get_share_holding_before_turns(player, int(company[-1]), before_turns)
        holdings[company] = share_company
    player_id = f'Player {player}'
    holdings[player_id] = get_cell_value(cell_locations[player_id][f'{player_id} Shares'])
    return holdings

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
        'Dividend Payout Ratio': 'B12',
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
        'Dividend Payout Ratio': 'C12',
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
        'Dividend Payout Ratio': 'D12',
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
        'Dividend Payout Ratio': 'E12',
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
        'Dividend Payout Ratio': 'F12',
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


def update_networth(player):
    nw_cell = cell_locations[player]['Net Worth']
    
    s1cell = cell_locations[player]['Player 1 Shares']
    s1qty = get_cell_value(s1cell)
    s1price_cell = cell_locations['Player 1']['Share Price'] 
    s1price = get_cell_value(s1price_cell)
    
    s2cell = cell_locations[player]['Player 2 Shares']
    s2qty = get_cell_value(s2cell)
    s2price_cell = cell_locations['Player 2']['Share Price'] 
    s2price = get_cell_value(s2price_cell)
    
    s3cell = cell_locations[player]['Player 3 Shares']
    s3qty = get_cell_value(s3cell)
    s3price_cell = cell_locations['Player 3']['Share Price'] 
    s3price = get_cell_value(s3price_cell)
    
    s4cell = cell_locations[player]['Player 4 Shares']
    s4qty = get_cell_value(s4cell)
    s4price_cell = cell_locations['Player 4']['Share Price'] 
    s4price = get_cell_value(s4price_cell)
    
    s5cell = cell_locations[player]['Player 1 Shares']
    s5qty = get_cell_value(s5cell)
    s5price_cell = cell_locations['Player 1']['Share Price'] 
    s5price = get_cell_value(s5price_cell)   
    
    cash_cell = cell_locations[player]['Cash']
    cash = get_cell_value(cash_cell)
    
    apply_interest_to_property(player)
    property_value_cell = cell_locations[player]['Property Value']
    property_value = get_cell_value(property_value_cell)
    
    
    apply_interest_to_debt(player)
    debt_cell = cell_locations[player]['Debt Value to be Repaid']
    debt = get_cell_value(debt_cell)
    
    equity_value = (s1qty * s1price) + (s2qty * s2price) + (s3qty * s3price) + (s4qty * s4price) + (s5qty * s5price)
    net_worth = equity_value + cash + property_value
    
    eq_cell = cell_locations[player]['Equity Value']
    set_cell_value(eq_cell,equity_value)

    
    set_cell_value(nw_cell,net_worth)    
    
    print("Net Worth Updated")

def end_turn_without_increasing_turns(player):
    print(f"{player} has chosen to end their turn without increasing turns played.")
    update_networth(player)

def apply_interest_to_debt(player):
    debt_taken_cell = cell_locations[player]['Debt Value to be Repaid']
    current_debt = get_cell_value(debt_taken_cell)
    interest_rate = 0.05  # Example interest rate of 5%
    
    if current_debt > 0:
        interest = current_debt * interest_rate
        new_debt = current_debt + interest
        set_cell_value(debt_taken_cell, new_debt)
        print(f"Applied interest to {player}'s debt. New debt value: {new_debt}")
    else:
        print(f"{player} has no outstanding debt to apply interest to.")
        

def apply_interest_to_property(player):
    property_cell = cell_locations[player]['Property Value']
    property_value = get_cell_value(property_cell)
    interest_rate = 0.025  # Example interest rate of 5%
    
    if property_value > 0:
        interest = property_value * interest_rate
        property_value_updated = property_value + interest
        set_cell_value(property_cell, property_value_updated)
        print(f"Applied interest to {player}'s Property Value. New Property value: {property_value_updated}")
    else:
        print(f"{player} has no property value")



def end_turn_without_increasing_turns(player):
    print(f"{player} has chosen to end their turn without increasing turns played.")

# Function to add cash
def add_cash(player):
    amount = float(input("Enter the amount of cash to add: "))
    cash_cell = cell_locations[player]['Cash']
    current_cash = get_cell_value(cash_cell)
    set_cell_value(cash_cell, current_cash + amount)
    cash_transfers.append(
        {
            'turn': turn,
            'credited_to': int(player[-1]),
            'debited_from': 0,
            'amount': amount
        }
    )

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
            share_transfers.append({
                'turn': turn,
                'seller': seller,
                'company': company,
                'quantity': quantity,
                'price': float(share_price),
                'buyer': int(player[-1])
            })
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
        cash_transfers.append(
            {
                'turn': turn,
                'debited_from': int(player[-1]),
                'credited_to': 0,
                'amount': amount
            }
        )

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
    cash_transfers.append(
        {
            'turn': turn,
            'debited_from': int(player[-1]),
            'credited_to': int(transfer_to_player[-1]),
            'amount': amount
        }
    )

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
        

#Function to calculate amount
def calculate_amount(player, percentage):
    equity_value = get_cell_value(cell_locations[player]['Equity Value'])
    debt = get_cell_value(cell_locations[player]['Debt Taken'])
    cash = get_cell_value(cell_locations[player]['Cash'])
    property_value = get_cell_value(cell_locations[player]['Property Value'])
    base_value = equity_value - debt - cash - property_value

    if percentage == 5:
        return 0.04 * base_value, "4/6"
    elif percentage == 10:
        return 0.07 * base_value, "3/6"
    elif percentage == 15:
        return 0.10 * base_value, "2/6"
    elif percentage == 20:
        return 0.13 * base_value, "1/6"

def calculate_circuit_value(player, percentage):
    equity_value = get_cell_value(cell_locations[player]['Equity Value'])
    debt = get_cell_value(cell_locations[player]['Debt Taken'])
    cash = get_cell_value(cell_locations[player]['Cash'])
    property_value = get_cell_value(cell_locations[player]['Property Value'])
    base_value = equity_value - debt - cash - property_value

    if percentage == 10:
        return 0.12 * base_value, "3/6"
    elif percentage == 20:
        return 0.06 * base_value, "4/6"

def print_amount_calculation(player):
    print(f"\nAmount Calculation:")
    for percentage in [5, 10, 15, 20]:
        amount, dice_roll = calculate_amount(player, percentage)
        print(f"For {percentage}%: {amount:.2f} - Dice roll: {dice_roll}")

def print_circuit_value(player):
    print(f"\nCircuit Calculation:")
    for percentage in [10, 20]:
        value, dice_roll = calculate_circuit_value(player, percentage)
        print(f"For {percentage}%: {value:.2f} - Dice roll: {dice_roll}")

def share_manipulation(current_player):
    cash = get_cell_value(cell_locations[current_player]['Cash'])
    print(f"\n{current_player}'s Current Cash: {cash}")
    
    manipulate_player_no = int(input("Enter the player number whose share price you want to manipulate (1-5): "))
    
    if manipulate_player_no < 1 or manipulate_player_no > 5:
        print("Error: Invalid player number.")
        return
    # if manipulate_player_no == int(current_player[-1]):
    #     print("Error: You cannot manipulate your own share price.")
    #     return
    
    manipulate_player = f"Player {manipulate_player_no}"
    
    print_amount_calculation(manipulate_player)
    print_circuit_value(manipulate_player)
    
    while True:
        print("\n1. Manipulate Share Price")
        print("2. Apply Circuit")
        print("3. Do Nothing")
        
        choice = input("\nEnter the number of the operation you want to perform: ")
        
        if choice == '1':
            percentage = int(input(f"\nBy what percentage do you want to manipulate {manipulate_player}'s share price (5, 10, 15, 20)? "))
            
            if percentage not in [5, 10, 15, 20]:
                print("Error: Invalid percentage.")
                return
            
            amount_required, _ = calculate_amount(manipulate_player, percentage)
            
            if cash >= amount_required:
                set_cell_value(cell_locations[current_player]['Cash'], cash - amount_required)
                print(f"{current_player} has successfully manipulated {manipulate_player}'s share price by {percentage}%.")
                print(f"{current_player}'s Updated Cash: {get_cell_value(cell_locations[current_player]['Cash'])}")
            else:
                print(f"Error: Insufficient cash ({cash}) to manipulate {manipulate_player}'s share price by {percentage}%.")
            break
                
        elif choice == '2':
            percentage = int(input(f"By what percentage do you want to apply circuit on {manipulate_player}'s share price (10, 20)? "))
            
            if percentage not in [10, 20]:
                print("Error: Invalid percentage.")
                return
            
            amount_required, _ = calculate_circuit_value(manipulate_player, percentage)
            
            if cash >= amount_required:
                set_cell_value(cell_locations[current_player]['Cash'], cash - amount_required)
                print(f"{current_player} has successfully applied circuit on {manipulate_player}'s share price by {percentage}%.")
                print(f"{current_player}'s Updated Cash: {get_cell_value(cell_locations[current_player]['Cash'])}")
            else:
                print(f"Error: Insufficient cash ({cash}) to apply circuit on {manipulate_player}'s share price by {percentage}%.")
                
            break
                
        elif choice == '3':
            break
        
        else:
            print("Invalid choice. Please try again.")

turn = 0
# Main loop to perform operations
def main_loop():
    players = list(cell_locations.keys())

    # Add value after each turn
    # Get average value after 8 rounds
    # Calculate dividend value for each company
    # Decide payout for each player

    average_property_value = { player: 0.0 for player in players }
    average_debt = { player: 0.0 for player in players }
    global turn
    while True:
        turn += 1
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
                print("11. Share Manipulation")
                
                choice = input("Enter the number of the operation you want to perform: ")

                if choice == '1':
                    add_cash(player)
                    update_networth(player)
                elif choice == '2':
                    withdraw_cash(player)
                    update_networth(player)

                elif choice == '3':
                    transfer_cash(player)
                    update_networth(player)

                elif choice == '4':
                    buy_property(player)
                    update_networth(player)

                elif choice == '5':
                    sell_property(player)
                    update_networth(player)

                elif choice == '6':
                    take_debt(player)
                    update_networth(player)

                elif choice == '7':
                    repay_debt(player)
                    update_networth(player)

                elif choice == '9':
                    turns_played_cell = cell_locations[player]['Turns Played']
                    current_turns = get_cell_value(turns_played_cell)
                    set_cell_value(turns_played_cell, current_turns + 1)
                    update_networth(player)
                    break

                elif choice == '8':
                    buy_shares(player)
                    update_networth(player)
                    
                elif choice == '10':
                    end_turn_without_increasing_turns(player)

                elif choice == '11':
                    share_manipulation(player)
                    update_networth(player)
            
                else:
                    print("Invalid choice. Please try again.")
            print("Share transfers")
            print(json.dumps(share_transfers, sort_keys=True, indent=2))
            print("Cash transfers")
            print(json.dumps(cash_transfers, sort_keys=True, indent=2))

        # Print the updated game state after each full round of turns
        print_game_state()

        for player in players:
            average_property_value[player] += float(get_cell_value(cell_locations[player]['Property Value']))
            average_debt[player] += float(get_cell_value(cell_locations[player]['Debt Taken']))

        print(json.dumps(average_property_value, sort_keys=True, indent=2))
        print(json.dumps(average_debt, sort_keys=True, indent=2))

        if turn % 8 == 0:
            for player in players:
                average_property_value[player] /= 8
                average_debt[player] /= 8
            
            # Calculate divided payout for each company
            def formula(avg_property_value, avg_debt):
                return max(0, 0.5 * (avg_property_value - avg_debt))

            dividend_payout = {}
            for company in players:
                dividend_payout_ratio = float(get_cell_value(cell_locations[company]['Dividend Payout Ratio']))
                dividend_payout[company] = dividend_payout_ratio * formula(average_property_value[company], average_debt[company])

            # Calculate actual amount for each player
            dividend_entitled = {}
            for player in players:
                dividend_entitled[player] = {}
                share_holding = get_all_share_holding(int(player[-1]), players, turn - 8)
                for company in players:
                    dividend_entitled[player][company] = share_holding[company] * dividend_payout[company]
            
            print("Dividend Entitled")
            print(json.dumps(dividend_entitled, sort_keys=True, indent=2))

            average_property_value = { player: 0.0 for player in players }
            average_debt = { player: 0.0 for player in players }


# Run the main loop
print_game_state()
main_loop()
