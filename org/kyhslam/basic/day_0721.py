

dic = {'한국' : 'KR', '일본' : 'JP'}

#print(dic)
#print(dic['한국'])

## 추가
dic['미국'] = 'EN'
print(dic)

## 키만 출력
print(dic.keys())


for key in dic.keys():
    print(key)

## 값만 출력
print(dic.values())

for val in dic.values():
    print(val)

## 전체를 List로 가져오기
print(dic.items())