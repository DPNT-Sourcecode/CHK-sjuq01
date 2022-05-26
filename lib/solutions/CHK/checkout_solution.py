

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #Price table definitions
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }
    offers = {
        "A": (3,130),
        "B": (2,45)
    }
    
    #Determine frequency of skus
    sku_freq = {
        "A":0,
        "B":0,
        "C":0,
        "D":0
    }
    
    for sku in skus:
        if sku not in prices.keys():
            return -1
        sku_freq[sku] += 1
    
    #Price determination
    sum_price = 0
    
    for item in sku_freq.keys():
        if item in offers.keys():
            number_offer = sku_freq[item]//offers[item][0]
            sum_price += number_offer*offers[item][1] + (sku_freq[item]-number_offer)*prices[item]
        else:
            sum_price += sku_freq[item]*prices[item]
            
    

    
        

