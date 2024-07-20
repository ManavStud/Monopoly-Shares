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

# Test logs
share_transfers_list1 = [
    {'turn': 2, 'buyer': 1, 'company': 2, 'seller': 2, 'quantity': 8, 'price': 0.05},
    {'turn': 3, 'buyer': 1, 'company': 2, 'seller': 2, 'quantity': 4, 'price': 0.05},
    {'turn': 7, 'buyer': 2, 'company': 2, 'seller': 1, 'quantity': 3, 'price': 0.05},
    {'turn': 10, 'buyer': 1, 'company': 2, 'seller': 2, 'quantity': 5, 'price': 0.05},
    {'turn': 11, 'buyer': 2, 'company': 2, 'seller': 1, 'quantity': 10, 'price': 0.05}
]
share_transfers_list2 = [
    {'turn': 2, 'buyer': 1, 'company': 2, 'seller': 2, 'quantity': 8, 'price': 0.05},
    {'turn': 3, 'buyer': 1, 'company': 2, 'seller': 2, 'quantity': 4, 'price': 0.05},
    {'turn': 7, 'buyer': 2, 'company': 2, 'seller': 1, 'quantity': 3, 'price': 0.05},
    {'turn': 10, 'buyer': 1, 'company': 2, 'seller': 2, 'quantity': 10, 'price': 0.05},
    {'turn': 11, 'buyer': 2, 'company': 2, 'seller': 1, 'quantity': 5, 'price': 0.05}
]

share_transfers_list3 = [
    {'turn': 1, "buyer": 1, "company": 2, "seller": 2, "quantity": 10, "price": 0.05}
]
# Returns shares held before number of turns

def get_share_holding_before_turns(share_transfers, player, company, before_turns):
    buy_orders_before_ex_date = filter(
        lambda x : x['turn'] <= before_turns and x['company'] == company and x['buyer'] == player,
        share_transfers
    )
    buy_orders_after_ex_date = filter(
        lambda x : x['turn'] > before_turns and x['company'] == company and x['buyer'] == player,
        share_transfers
    )
    sell_orders_before_ex_date = filter(
        lambda x : x['turn'] <= before_turns and x['company'] == company and x['seller'] == player,
        share_transfers
    )
    sell_orders_after_ex_date = filter(
        lambda x : x['turn'] > before_turns and x['company'] == company and x['seller'] == player,
        share_transfers
    )

    def calculate_holdings(total, transaction):
        return total + transaction['quantity']

    shares_held_before_ex_date = reduce(calculate_holdings, buy_orders_before_ex_date, 0)
    shares_held_after_ex_date = reduce(calculate_holdings, buy_orders_after_ex_date, 0)
    shares_sold_before_ex_date = reduce(calculate_holdings, sell_orders_before_ex_date, 0)
    shares_sold_after_ex_date = reduce(calculate_holdings, sell_orders_after_ex_date, 0)

    return shares_held_before_ex_date - shares_sold_before_ex_date + min(shares_held_after_ex_date - shares_sold_after_ex_date, 0)

# print(get_share_holding_before_turns(share_transfers_list1[:3], 1, 2, 3), "round 6 case")
# print(get_share_holding_before_turns(share_transfers_list1[:4], 1, 2, 9), "round 9 case")
# print(get_share_holding_before_turns(share_transfers_list1, 1, 2, 9), "round 12 case (sold more)")
# print(get_share_holding_before_turns(share_transfers_list2, 1, 2, 9), "round 12 case (sold less)")
# assert get_share_holding_before_turns(share_transfers_list1[:2], 1, 2, 3) == 12, "Failed round 6 case"
# assert get_share_holding_before_turns(share_transfers_list1[:3], 1, 2, 9) == 9, "Failed round 9 case"
# assert get_share_holding_before_turns(share_transfers_list1, 1, 2, 9) == 4, "Failed round 12 case (sold more)"
# assert get_share_holding_before_turns(share_transfers_list2, 1, 2, 9) == 9, "Failed round 12 case (sold less)"

# players = [f'Player {x}' for x in range(1, 6)]
# turn = 5
# def get_all_share_holding(player):
#     holdings = {}
#     for company in players:
#         share_company = get_share_holding_before_turns(share_transfers, player, int(company[-1]), turn)
#         holdings[company] = share_company
#     return holdings

# print(get_share_holding_before_turns(1, 2, 4))
# print(get_all_share_holding(1))