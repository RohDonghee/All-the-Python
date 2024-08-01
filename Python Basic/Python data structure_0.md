# Python data structure
- 스택과 큐 (Stack & queue)
- 튜플과 집합 (Tuple & set)
- 사전(Dictionary)
- Collection 모듈

# Stack 
나중에 넣은 데이터를 먼저 반환하도록 설계된 메모리 구조(Last In First Out:LIFO)<br>
**데이터를 임시 저장**할 때 사용하는 자료구조<br>
ex. 깊이 우선 탐색(DFS) , 백트래킹 종류에 유용
- 데이터 입력 : ```push```
- 데이터 출력 : ```pop```
- 스택에서 입출력이 이뤄지는 부분 : ```top```
- 반대쪽 부분 : ```bottom```
- 예외 처리 클래스(스택이 **비어 있으면** 내보내는 예외 처리) : ```Empty```
- 예외 처리 클래스(스택이 **가득 차 있으면** 내보내는 예외 처리) : ```Full```
- 스택 비었는지 검사 : ```is_empty()```
- 스택 가득 차 있는지 검사 : ```is_full()```
- 초기화하는 함수(스택 배열을 생성하는 등의 준비 작업 수행) : ```__init()__```

- 스택 크기(**스택의 최대 크기**를 나타내는 int형 정수) : capacity
- 스택 배열(push한 데이터를 저장하는 **스택 본체인 list 배열**) : stk
- 스택 포인터(스택에 쌓여있는 **데이터의 개수**) : ptr

```python
# 고정 길이 스택 클래스 FixedStack 구현하기

from typing import Any  # 타입 힌트를 위해 typing 모듈로 타입 표시


class FixedStack:
    """고정 길이 스택 클래스"""
    class Empty(Exception):
        """비어 있는 FixedStack에 pop 또는 peek할 때 내보내는 예외처리"""
        pass

    class Full(Exception):
        """가득 찬 FixedStack에 push할 때 내보내는 예외 처리"""
        pass

    def __init__(self, capacity: int=256) -> None:
        """스택 초기화"""
        self.stk = [None] * capacity  # 스택의 본체 - 내부의 리스트를 고정된 크기로 초기화
        self.capacity = capacity      # 스택의 최대 크기를 나타냄
        self.ptr = 0                  # 스택 포인터

    def __len__(self) -> int:
        """스택에 쌓여 있는 데이터 개수 반환"""
        return self.ptr

    def is_empty(self) -> bool:
        """스택이 비어있는지 판단"""
        return self.ptr <= 0  # == 연산자가 아닌 것에 유념

    def is_full(self) -> bool:
        """스택이 가득 차 있는지 판단"""
        return self.ptr >= self.capacity  # == 연산자가 아닌 것에 유념

    def push(self, value: Any) -> None:
        """스택에 value를 push"""
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """스택에 value를 pop"""
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        """스택에서 데이터를 피크 (꼭대기에서 데이터를 들여다봄) """
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        """스택을 비움 (모든 데이터 삭제)"""
        self.ptr = 0

    def find(self, value: Any) -> Any:
        """스택에서 value를 찾아 인덱스를 반환 (없으면 -1을 반환)"""
        for i in range(self.ptr-1, -1, -1):
            if self.stk[i] == value:
                return i  # 검색 성공
        return -1  # 검색 실패

    def count(self, value: Any) -> int:
        """스택에 있는 value의 개수를 반환"""
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        """스택에 value가 있는지 판단"""
        return self.count(value) > 0

    def dump(self) -> None:
        """덤프 (스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)"""
        if self.is_empty():
            print('스택이 비어 있습니다')
        else:
            print(self.stk[:self.ptr])
```

**※ 리스트와 사용** 
- push는 ```append()```,pop은 ```pop()```을 사용
```python
a = [1,2,3,4,5]
a.append(6)
a.append(7)
a.pop()
>>>20
a.pop()
>>>10
```

**※글자역순출력(예시)**
```python
#글자 역순 출력
word = input()
word_list = list(word)
for i in range(len(word_list)):
  print(word_list.pop()) #하나씩 빼면서 출력
```
