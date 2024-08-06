# 버블 정렬 알고리즘 구현

#MutableSequence: typing 모듈에 있는 제네릭 클래스 중 하나로, 변경 가능한 시퀀스를 나타냄. 리스트와 같은 변경 가능한 자료형에 대해 타입 힌트를 제공할 때 사용.
from typing import MutableSequence 

def bubble_sort(a: MutableSequence) -> None: #None은 함수가 아무것도 반환하지 않는다는 뜻
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j],a[j-1] #a[j-1]이 a[1]보다 크다면 교환해야함.

if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요:'))
    x = [None] * num #x라는 리스트를 num의 개수만큼 초기화

    for i in range(num): 
        x[i] = int(input(f'x[{i}]:'))
    
    bubble_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
