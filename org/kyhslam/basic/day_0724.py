## 순서, 중복 없다

data = set()
#print(type(data))

data_set = {'apple', 'dell', 'samsung'}
#print(type(data_set))
#print(data_set)

data_set.add('lg')

print(data_set)
data_set.remove('apple')
print(data_set)


## 읽기
for data in data_set:
    print(data)


## 데이터 체크
#print('dell' in data_set)


data1 = {'apple', 'samsung', 'lg'}
data2 = {'samsung', 'lg', 'xaiomi'}

print(data1 & data2) # // 교집합
print(data1 | data2) # // 합집합
print(data1 - data2) # // 차집합
print(data1 ^ data2)
