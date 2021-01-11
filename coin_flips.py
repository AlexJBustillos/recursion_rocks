# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"
# pure function or functional programming has no side effects on the world around it
def coin_flips(n):
    result = []
    def flips(n, result, present):
        if n == 1:
            result.append(present + 'H')
            result.append(present + 'T')
        else:
            flips(n - 1, result, present + 'H')
            flips(n - 1, result, present + 'T')
        
    flips(n, result, '')
    return result

print(coin_flips(2))

# print(coinFlips(2)) 
# => ["HH", "HT", "TH", "TT"]

def coin(n):
    # base case
    if n == 1:
        return ['H', 'T']
    
    already_flipped = coin(n - 1)

    history_plus_heads = list(map(lambda el: el + 'H', already_flipped))
    history_plus_tails = list(map(lambda el: el + 'T', already_flipped))

    return history_plus_heads + history_plus_tails


print(coin(2))