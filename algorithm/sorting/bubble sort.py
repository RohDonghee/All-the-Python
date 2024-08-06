# 버블 정렬 알고리즘 구현

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None: #a를 인수로 전달받음 
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j],a[j-1]


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
