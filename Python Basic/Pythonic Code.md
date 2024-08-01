# Pythonic Code
- 파이썬 특유의 코딩 기법
- 파이썬 특유의 문법을 활용하여 효율적으로 코드를 표현

# Split & Join
**split** : String type의 값을 기준값으로 나눠서 list로 반환 
```python
items = 'zero one two three'
print(items)
>>> ["zero", "one", "two", "three"]
```

**join** : String으로 구성된 list를 합쳐서 하나의 string으로 반환
```python
colors = ['zero' , 'one' , 'two' , 'three']
result = ''.join(colors) #'' 안에 값으로 연결해줌
>>> 'zeroonetwothree'
```

# list comprehension 
- 기존 list를 활용해서 간단히 다른 list로 만드는 기법
- 선언과 할당이 동시에 되기 때문에 for + append보다 속도가 빠름<br>
```[(변수에 활용할 값) for (사용할 변수명) in (순회값)]```

```python
result = [ i for i in range(10) if i % 2 == 0 ]
print(result)
>>> [0,2,4,6,8]
```
