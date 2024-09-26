prices = [7,1,5,3,6,4]
# 리스트에서 제일 작은 수를 찾아야하고 만약에 그 뒤에 작은 수보다 큰 숫자가 없으면 0
# 리스트에서
min_price = min(prices)
if prices.index(min(prices)) == len(prices) - 1:
    print(0)
else:
    print(max(prices[prices.index(min(prices)):]) - min_price)