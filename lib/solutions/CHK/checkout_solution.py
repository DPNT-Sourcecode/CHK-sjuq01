# Determine the multioffer discount for a specific offer
def multioffer(sku_freq, number, price, priority):
    # Determine count of involved items
    count = 0
    for item in priority:
        count += sku_freq[item]
    
    # Determine the number of offers and the resulting sku frequencies post application
    number_offer = count//number
    overflow = count%number
    priority_count = len(priority) - 1
    
    while overflow >= 0 and priority_count >= 0:
        if sku_freq[priority[priority_count]] >= overflow:
            sku_freq[priority[priority_count]] = overflow
            overflow = 0
        else:
            overflow -= sku_freq[priority[priority_count]]
        priority_count -= 1

    while priority_count >= 0:
        sku_freq[priority[priority_count]] = 0
        priority_count -= 1
    
    return sku_freq, number_offer*price

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #Price table definitions
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 70,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 20,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 17,
        "Y": 20,
        "Z": 21
    }
    #Offers to include any 3 of STXYZ
    offers = {
        "A": [[5,200],[3,130]],
        "B": [[2,45]],
        "E": [[2,"B"]],
        "F": [[3,20]],
        "H": [[10,80],[5,45]],
        "K": [[2,120]],
        "N": [[3,"M"]],
        "P": [[5,200]],
        "Q": [[3,80]],
        "R": [[3,"Q"]],
        "U": [[4,120]],
        "V": [[3,130],[2,90]],
        "S": [[3,"STXYZ", 45]],
        "T": [[3,"STXYZ", 45]],
        "X": [[3,"STXYZ", 45]],
        "Y": [[3,"STXYZ", 45]],
        "Z": [[3,"STXYZ", 45]],
    }
    
    #Determine frequency of skus
    sku_freq = dict.fromkeys(prices.keys(), 0)
    
    for sku in skus:
        if sku not in prices.keys():
            return -1
        sku_freq[sku] += 1
    
    #Price determination
    sum_price = 0
    #Prioritisation of items
    priority_order = ["S", "T", "X", "Y", "Z", "E", "N", "R", "A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "U", "V", "W"]
    
    for item in priority_order:
        if item in offers.keys():
            for offer in offers[item]:
                # Monetary offer
                if isinstance(offer[1], int):
                    number_offer = sku_freq[item]//offer[0]
                    sku_freq[item] -= number_offer*offer[0] 
                    sum_price += number_offer*offer[1]
                
                #Other item offer
                elif isinstance(offer[1],str) and len(offer[1]) == 1:
                    number_offer = sku_freq[item]//offer[0]
                    if sku_freq[offer[1]]>0:
                        sku_freq[offer[1]] -= number_offer
                
                # Multi item offer
                elif isinstance(offer[1], str) and len(offer[1]) > 1:
                    sku_freq, price_addition = multioffer(sku_freq, offer[0], offer[2], sorted(offer[1], reverse=True, key = lambda x: prices[x]))
                    sum_price += price_addition
   
            sum_price += sku_freq[item]*prices[item]
        else:
            sum_price += sku_freq[item]*prices[item]
    
    return sum_price
            
print(checkout("SSS"))  

    
        


