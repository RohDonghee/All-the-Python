# 불필요한 데이터 삭제하기 
API, 웹 스크래핑, 데이터베이스 등으로 수집한 불완전한 데이터를 삭제하는 방법

## 열 삭제하기
```py
import pandas as pd
df = pd.read_csv('남산도서관 장서 대출목록 (2021년 04월).csv', encoding='EUC-KR')
```
![image](https://github.com/user-attachments/assets/f69df931-25ec-4feb-b2fa-e81ef37d8af3)<br>
- csv 파일 각 라인 끝에 존재하는 콤마로 인해 ***Unnamed:13***이 존재한다.
- 불필요한 데이터 열이기 때문에 삭제해야 한다.

```py
ns_df = pd.read_csv('남산도서관 장서 대출목록 (2021년 04월).csv', low_memory=False)
ns_book = ns_df.loc[:,'번호':'등록일자'] 
ns_book.head()
```

![image](https://github.com/user-attachments/assets/2ede0316-aad0-4a0b-92d6-75046c881c8a)<br>
- '번호'열부터 '등록일자'열까지 출력한다.
- ```loc```는 location의 약어로, 데이터프레임의 행 또는 칼럼의 label**label**이나 **boolean array**를 인덱싱한다.
```py
print(ns_df.columns) #데이터프레임 열 이름이 저장된 모든 Columns 속성 출력
print(ns_df.columns[0]) #columns 속성의 0번째 인덱스 출력
```
- 원소별 비교(element-wise comparison)을 통해 열을 boolean array로 나타낼 수 있다.
```py
ns_df.columns != 'Unnamed: 13' #col 값이 'Unnamed: 13'인 값만 False가 출력
selected_columns = ns_df.columns != 'Unnamed: 13'
ns_book = ns_df.loc[:, selected_columns] #값이 True인 열의 모든 행만 선택
ns_book.head()
```

### drop() 메서드
- 행이나 열을 삭제할 수 있다.
- 실제로 삭제되는 것이 아니라 복사된 객체를 반환한다.
```py
ns_book = ns_df.drop(['부가기호', 'Unnamed: 13'], axis=1)  
#여러 개의 열을 삭제하려면 리스트 형식으로 사용 
ns_book.head()
```
**※ axis 매개변수의 기본값인 0은 행(가로), 1은 열(세로)을 나타냄**

### dropna() 메서드
- pandas는 비어있는 값은 NaN(Not a Number: 정의되지 않은 값 혹은 표현할 수 없는 값)으로 표시한다.
- **NaN이 하나라도 포함된 행이나 열을 삭제**한다.
- 모든 값이 NaN인 열을 삭제하려면 dropna()메서드에 **how**매개변수를 'all'로 지정하면 된다.
```py
ns_book = ns_df.dropna(axis=1)
ns_book.head()
```
![image](https://github.com/user-attachments/assets/2bd4c219-db80-47e9-a706-41cf4def8c45)


## 행 삭제하기
- 행을 삭제할 때는 drop() 메서드 혹은 []연산자, 슬라이싱 등을 사용한다.
  
### drop() 메서드
- axis를 0으로 지정하면 행을 삭제할 수 있다.(그러나 기본값이 0이기 때문에 생략 가능)
```py
ns_book2 = ns_book.drop([0,1])
ns_book2 = ns_book2.drop(['Unnamed: 0'], axis=1)
ns_book2.head()
```

### []연산자와 슬라이싱
- 슬라이싱을 이용해서 범위를 지정해줄 수 있다.
```py
ns_book2 = ns_book[2:]
ns_book2.head()
```
※ drop() 메서드나 슬라이싱 모두 같은 결과 출력. 2번째 인덱스부터 출력됨
![image](https://github.com/user-attachments/assets/7a086f6a-2e0a-45e4-8d3f-e5eeb7399ceb)

### []연산자와 불리언 배열
- 행을 선택할 때 가장 즐겨 사용하는 표현이다.
- 원하는 행은 True로, 제외할 행은 False로 표시한 불리언 배열을 만들어 사용한다.
```py
selected_rows = ns_df['출판사'] == '한빛미디어' #출판사가 '한빛미디어'인 행만 출력
ns_book2 = ns_book[selected_rows]
ns_book2.head()
```
![image](https://github.com/user-attachments/assets/249e11d9-5f86-4287-9e52-09f3b0bc70e7)

```py
ns_book2 = ns_book[ns_book['대출건수'] > 1000] #대출건수가 1,000건이 넘는 행만 출력
ns_book2.head()
```

## 중복된 행 찾기
### duplicated() 메서드
- **중복여부를 불리언 배열**로 반환한다.
- 처음 행을 Fasle, 나머지(중복된) 행을 True로 표시한다.
- 데이터프레임에 있는 모든 열을 기준으로 중복된 행을 표시한다.
- 일부 열을 기준으로 중복된 행을 찾으려면 ```subset 매개변수```를 활용한다.
- subset 사용할 때 주의 : **두 개 이상의 값을 불러 올때는 DataFrame 형태**로 불러와야 합니다.
```py
sum(ns_book.duplicated(subset=['도서명','저자','ISBN']) #도서명, 저자, ISBN으로 한정하여 중복 검사 
```

## 그룹별로 모으기 
### groupby() 메서드
- 데이터를 그룹별로 분할하여 독립된 그룹에 대하여 별도로 데이터를 처리(혹은 적용)하거나 그룹별 통계량을 확인한다.
- ```by 매개변수```로 행을 합칠 때 기준이 되는 열을 지정한다.
- 묶고 싶은 칼럼을 기준으로 groupby()를 하면 된다.
![image](https://github.com/user-attachments/assets/8e8e8079-93b7-40c7-a587-8ea3177a60b9) <br>
출처 : www.w3resource.com <br>
  - **Split 단계**: 위에 이미지에서 Split 단계에서 .groupby()에서 정의한 컬럼 조건에 따라 독립된 그룹으로 나누어 줍니다.
  - **Apply 단계**: 나뉘어진 독립된 그룹별 함수를 적용하는 단계 입니다.
  - **Combine 단계**: 최종 단계이며, 각각의 독립된 그룹별로 함수가 적용된 결과를 종합하여 다시 하나의 테이블로 합칩니다.
```py
count_df = ns_book[['도서명', '저자', 'ISBN', '권', '대출건수']] #그룹으로 묶을 기준 열과 대출건수 열만 선택해서 사용
group_df = count_df.groupby(by = ['도서명','저자','ISBN','권'], dropna=False) #이 4개의 열을 묶어줌 (groupby는 NaN이 있는 행을 삭제하기 대문에 dropna = False 설정)
loan_count = group_df.sum()
loan_count = count_df.groupby(by=['도서명','저자','ISBN','권'], dropna = False).sum() #

loan_count.head()
```
![image](https://github.com/user-attachments/assets/65cd401a-5ca0-4ca2-bacc-b3d96ce1ee57)


