# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

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