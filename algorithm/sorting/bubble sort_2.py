from typing import MutableSequence

def bubble_sort_verbose(a: MutableSequence) -> None:
    ccnt = 0
    scnt = 0
    n = len(n)
    for i in range(n-1):
        print(f'패스 {i+1}')
        for j in range(n-1, i, -1):
            for m in range(0, n-1):
                print(f'a{[m]:2}' + (' 'if m != j - 1 else
                                     ' +' if a[j-1] > a[j] else ' -'),
                                    end ='')
            print(f'{a[n-1]:2}')
            ccnt += 1
            if a[j-1] > a[j]:
                scnt += 1
                a[j-1], a[j] = a[j], a[j-1]
        for m in range(0, n-1):
            print(f'{a[m]:2}', end=' ')
        print(f'{a[n-1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')
