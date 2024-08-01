# Python data structure
- 스택과 큐 (Stack & queue)
- 튜플과 집합 (Tuple & set)
- **사전(Dictionary)**
- Collection 모듈

### ■ 리스트와 튜플로 딕셔너리 만들기
```dict.fromkeys()'''는 키 리스트로 딕셔너리를 생성하며 값은 None으로 저장됨.<br>
```dict.fromkeys(키리스트, 값```처럼 값을 지정하면 해당 값이 키의 값으로 저장
```python
keys =['a','b','c']
x = dict.fromkeys(keys,100)
print(x)

>>> {'a': 100, 'b': 100, 'c': 100}
```

### ■ 딕셔너리 표현식 사용하기
```{키: 값 for 키, 값 in 딕셔너리}```<br>
```dict({키: 값 for 키, 값 in 딕셔너리})```
- for in 다음에 딕셔너리를 지정하고 items를 사용
``` x = {key: value for key, value in dict.fromkeys(keys).items()}```<br>
※items가 아니라 keys, values로 특정 값만 가져올 수 있음

### ■ 딕셔너리 표현식에서 if조건문 사용
```{키: 값 for 키, 값 in 딕셔너리 if 조건식}```<br>
```dict({키: 값 for 키, 값 in 딕셔너리 in 조건식})```<br>


### ■ 딕셔너리 안에서 딕셔너리 사용
```딕셔너리 = {'키1' : {'키A' : 값A}, '키2' : {'키B' : 값B}} ```
- 중첩 딕셔너리는 계층형 데이터를 저장할 때 유용
- 중첩 딕셔너리에 접근하려면 딕셔너리 뒤에 []를 단계만큼 붙임

### ■ 딕셔너리 할당과 복사
```python
#할당
x = {'a':10, 'b':20, 'c':30, 'd':40}
y = x (
x is y 

>>> True
```

```python
#복사
x = {'a':10, 'b':20, 'c':30, 'd':40}
y = x.copy()
x is y 

>>> False 
```
※ 중첩 딕셔너리를 복사하려면 ```copy()```가 아니라 ```deepcopy()```를 사용해야함<br>
