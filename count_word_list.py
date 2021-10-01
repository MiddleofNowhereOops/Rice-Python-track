def count_letters(word_list):
    """ See question description """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0
        
    # enter code here  
    for word in word_list:
        letters = list(word)
        for letter in letters:
            if letter in ALPHABET:
                letter_count[letter] += 1
    
    max_count = 0
    max_letter = ""
    
    for key, value in letter_count.items():
        if letter_count[key] > max_count:
            max_count = value
            max_letter = key
            
    return max_letter
            

#print(count_letters(["hello", "world"]))
    
   
monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"
monty_words = monty_quote.split(" ")

print(count_letters(monty_words))
