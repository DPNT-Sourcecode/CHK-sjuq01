

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #Price table definitions
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40
    }
    offers = {
        "A": [[5,200],[3,130]],
        "B": [[2,45]],
        "E": [[2,"B"]]
    }
    
    #Determine frequency of skus
    sku_freq = {
        "A":0,
        "B":0,
        "C":0,
        "D":0,
        "E":0
    }
    
    for sku in skus:
        if sku not in prices.keys():
            return -1
        sku_freq[sku] += 1
    
    #Price determination
    sum_price = 0
    #Prioritisation of items
    priority_order = ["E", "A", "B", "C", "D"]
    
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
                    sku_freq[offer[1]] -= number_offer
   
            sum_price += sku_freq[item]*prices[item]
        else:
            sum_price += sku_freq[item]*prices[item]
    
    return sum_price
            
    

    
        

