from functools import reduce

share_transfers = [
    {
        'turn': 1,
        'company': 2,
        'seller': 2,
        'buyer': 1,
        'quantity': 10,
        'price': 0.05
    },
    {
        'turn': 2,
        'company': 2,
        'seller': 2,
        'buyer': 1,
        'quantity': 15,
        'price': 0.08
    },
    {
        'turn': 3,
        'company': 2,
        'seller': 1,
        'buyer': 2,
        'quantity': 15,
        'price': 0.12
    },
    {
        'turn': 4,
        'company': 2,
        'seller': 2,
        'buyer': 1,
        'quantity': 25,
        'price': 0.09
    },
    {
        'turn': 5,
        'company': 2,
        'seller': 1,
        'buyer': 2,
        'quantity': 20,
        'price': 0.05
    },
    {
        'turn': 1,
        'company': 3,
        'seller': 3,
        'buyer': 1,
        'quantity': 10,
        'price': 0.05
    },
    {
        'turn': 2,
        'company': 3,
        'seller': 3,
        'buyer': 1,
        'quantity': 15,
        'price': 0.08
    },
    {
        'turn': 3,
        'company': 3,
        'seller': 1,
        'buyer': 3,
        'quantity': 15,
        'price': 0.12
    },
    {
        'turn': 4,
        'company': 3,
        'seller': 1,
        'buyer': 3,
        'quantity': 25,
        'price': 0.09
    },
    {
        'turn': 5,
        'company': 3,
        'seller': 3,
        'buyer': 1,
        'quantity': 20,
        'price': 0.05
    }
]

# Returns shares held before number of turns
def get_share_holding_before_turns(player, company, before_turns):
    player_shares = filter(
        lambda x : x['turn'] <= before_turns and x['company'] == company and (x['buyer'] == player or x['seller'] == player),
        share_transfers
    )

    def calculate_holdings(total, transaction):
        return total + transaction['quantity'] if transaction['buyer'] == player else total - transaction['quantity']

    return reduce(calculate_holdings, player_shares, 0)

players = [f'Player {x}' for x in range(1, 6)]
turn = 5
def get_all_share_holding(player):
    holdings = {}
    for company in players:
        share_company = get_share_holding_before_turns(player, int(company[-1]), turn)
        holdings[company] = share_company
    return holdings

print(get_share_holding_before_turns(1, 2, 4))
print(get_all_share_holding(1))