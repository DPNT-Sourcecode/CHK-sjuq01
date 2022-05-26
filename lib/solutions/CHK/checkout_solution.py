

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
        "K": 80,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 30,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 90,
        "Y": 10,
        "Z": 50
    }
    offers = {
        "A": [[5,200],[3,130]],
        "B": [[2,45]],
        "E": [[2,"B"]],
        "F": [[3,20]],
        "H": [[10,80],[5,45]],
        "K": [[2,150]],
        "N": [[3,"M"]],
        "P": [[5,200]],
        "Q": [[3,80]],
        "R": [[3,"Q"]],
        "U": [[4,120]],
        "V": [[3,130],[2,90]]
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
    priority_order = ["E", "N", "R", "A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    for item in priority_order:
        if item in offers.keys():
            for offer in offers[item]:
                # Monetary offer
                if isinstance(offer[1], int):
                    number_offer = sku_freq[item]//offer[0]
                    sku_freq[item] -= number_offer*offer[0] 
                    sum_price += number_offer*offer[1]
                
                #Other item offer
                elif isinstance(offer[1],str):
                    number_offer = sku_freq[item]//offer[0]
                    if sku_freq[offer[1]]>0:
                        sku_freq[offer[1]] -= number_offer
   
            sum_price += sku_freq[item]*prices[item]
        else:
            sum_price += sku_freq[item]*prices[item]
    
    return sum_price
            
# print(checkout("FFABCDECBAABCABBAAAEEAAFF"))  

    
        
