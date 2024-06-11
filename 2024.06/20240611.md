# Python data structure
- 스택과 큐 (Stack & queue)
- 튜플과 집합 (Tuple & set)
- **사전(Dictionary)**
- Collection 모듈

# Dictionary
데이터를 저장할 때는 구분 지을 수 있는 값과 같이 저장<br>
값마다 이름을 붙여서 저장하는 방식<br>
```python
lux = {'health' : 500, 'mana' : 340, 'melee' : 660}
# 딕셔너리 = {키1(key):값1(value), 키2:값2}
# 딕셔너리 = {}
# 딕셔너리 = dict()
```
- **key** : 자료를 꺼낼 수 있는 도구
- **value** : 데이터 값

### ■ Dictionary 정보
- 키가 중복되면 가장 뒤에 있는 값만 사용
- 모든 자료형을 사용할 수 있음

### ■ Dictionary 키 접근 및 할당
- '딕셔너리[키]'를 통해 접근 가능
- 딕셔너리에 키를 지정하지 않으면 해당 딕셔너리 전체를 뜻함
- ```items()``` : 딕셔너리 데이터 출력
- ```keys()``` : 딕셔너리 key만 출력
- ```values()``` : 딕셔너리 value만 출력

### ■ Dictionary 조작
-```setdefault(키, 값)``` : **키-값 쌍 추가**<br>
-```update(키 = 값)``` : **키의 값 수정**, 키가 없으면 키-값 쌍 추가 (키가 문자열일 때만 사용 가능)<br>
-```pop(키)``` : **특정 키-값 쌍을 삭제**한 뒤 반환<br>
-```popitem()``` : **임의의 키-값 쌍을 삭제**한 뒤 튜플(tuple)로 반환 <br>
-```clear()``` : **모든 키-값 쌍 삭제**<br>
-```get(키)``` : **딕셔너리에서 특정 키의 값을 가져옴**

### ■ list와 tuple로 Dictionary 만들기
- 리스트, 튜플에 ```dict.fromkeys()```에 키가 들어있는 리스트를 넣으면 딕셔너리 생성
```python
keys = ['a','b','c']
x = dict.fromkeys(keys)
print(x)
>>> ['a': None, 'b': None, 'c': None]

y = dict.fromkeys(key, 100)
print(y)
>>>['a': 100, 'b': 100, 'c': 100]
```
**※defaultdict 사용**
- Dict type의 기본 값을 지정, 신규값 생성시에 사용하는 방법
- 처음 키를 지정할 대, 값을 주지 않으면 해당 키에 대한 값을 디폴트로 지정
```python
from collections import defaultdict 
y = defaultdict(int)
y['z'] # 0이 출력됨. 기본값을 0으로 출력됨 
```

```

