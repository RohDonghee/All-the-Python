# Variables
프로그래밍에서 변수는 **값을 저장하는 주소**<br>
변수는 메모리 주소를 가지고 있고, **변수에 들어가는 값은 메모리 주소에 할당**<br>

 ### ■ 폰 노이만 구조 (John von Neumann Architecture)
- 프로그램 내장 방식의 컴퓨터
- 내장 메모리 **순차처리** 방식 (프로그램 실행할 때, 그 정보를 먼저 메모리에 저장시키고 CPU가 순차적으로 그 정보를 해석하고 계산)

---

# list
시퀀스 자료형, 여러 데이터들의 집합 <br>
- 인덱싱(indexing)
```python
alphabet = [A,B,C]
print(alphabet[2])
>>> C
```
- 슬라이싱(slicing)
```python
alphabet = [A,B,C]
print(alphabet[0:2])
>>>A,B
```
- 리스트 연산 -> append, extend, insert, remove 
- 추가 삭제
- 메모리 저장 방식
- 패킹(packing) & 언패킹(unpacking) -> 여러개의 객체를 하나의 객체로 묶어주거나(한 변수에 여러 개의 데이터를 넣어줌) 그 반대
- 2차원 리스트

list는 주소(offset)을 가지고 있기 때문에 다양하게 활용 가능

---

# Function 
**어떤 일을 수행하는 코드 덩어리**<br>
반복적인 수행을 위해 1회만 작성<br>
코드를 논리적인 단위로 분리<br>
함수와 함수 선언 사이에는 2줄씩 띄워줌 

### ■ 함수의 수행 순서 
함수 부분을 제외한 메인프로그램부터 실행<br>
함수를 정의한 부분은 메모리에 올라감 

### ■ Parameter vs Argument
- parameter : 함수의 입력 값 인터페이스
- argument : 실제 parameter에 대입되는 값
```python
def f(x):  # x <- parameter 
  return 2 * x

print(f(2)) # 2<- argument
```

### ■ 함수의 형태  
**parameter 유무 , 반환 값(return value) 유무**에 따라 함수의 형태가 다름 
| |parameter 없음|parameter 있음| 
|----|-----|----|
|반환 값 없음|함수 내의 수행문만 수행|parameter 사용, 수행문만 수행|
|반환 값 있음|parameter 없이 수행문 수행 후 결과값 반환|parameter 사용, 수행문 수행 후 결과값 반환| <br>

**※ return이 없다면 ?** 
```python
def f(x):
  print x+10 # return 없음 -> 값을 반환하는 것이 아니라 단순히 출력만 함 (값을 반환하고 싶다면 return은 반드시 필요)

f(10)
>>> 20
c = f(10)
>>> 20
print(c)
>>> None # 메모리에 없기 때문에 
```
