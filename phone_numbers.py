PHONE_NUMBERS = {
    "2" : "abc",
    "3" : "def",
    "4" : "ghi",
    "5" : "jkl",
    "6" : "mno",
    "7" : "pqrs",
    "8" : "tuv",
    "9" : "wxyz"
}

def phone_numbers(numberstr):
    if (len(numberstr) == 1):
        lookedup = PHONE_NUMBERS[numberstr]        
        return [c for c in lookedup]
    otherperms = phone_numbers(numberstr[1:])
    curr = numberstr[0]
    lookedup = PHONE_NUMBERS[curr]
    res = []
    for l in lookedup:       
        for num in otherperms:
            res.append(l + num)
    return res

def phone_numbers_counts(numberstr):
    table = [0 for i in range(len(numberstr))]
    table[0] = len(PHONE_NUMBERS[numberstr[0]])
    for i in range(1, len(numberstr)):
        table[i] = len(PHONE_NUMBERS[numberstr[i]]) * table[i-1]
    return table[len(numberstr) - 1]
    
    
        
print(len(phone_numbers("2234")))
print(phone_numbers_counts("2234"))
