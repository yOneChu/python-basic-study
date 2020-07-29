prices = '100 달러'

if prices[4:] == '달러':
    print(int(prices[:4]) * 1112, '달러')



exchange = {'달러':1112, '위안':171, '엔':1010}
prices = '100 달러'
for exchange_key in exchange.keys():
    if prices[4:] == exchange_key:
        print( int(prices[:4]) * exchange[exchange_key], '원')


## 구구단 출력
for index in range(2,10):
    for index2 in range(1,10):
        print(index, "x", index2,"=", (index*index2))


dongs = ["101동", "102동","103동"]
hos = ["101호", "102호", "103호"]
for dong in dongs:
    for ho in hos:
        print(dong, ho)
    print("\n")
