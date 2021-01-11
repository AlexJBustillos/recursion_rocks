# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(ss):
    if len(ss) == 0:
        return ss
    else:
        return reverse(ss[1:]) + ss[0]

print(reverse("")) 
# => ""
print(reverse("a")) 
# => "a"
print(reverse("ab")) 
# => "ba"
print(reverse("computer")) 
# => "retupmoc"
print(reverse(reverse("computer"))) 
# => "computer"

def reverse1(ss, already_reversed = ''):
    # get base case down before moving forward
    if len(ss) == 0:
        return already_reversed
    
    new_already_reversed = ss[0] + already_reversed
    new_ss = ss[1:]

    return reverse1(new_ss, new_already_reversed)

print(reverse1("a"))
print(reverse1("babbling"))