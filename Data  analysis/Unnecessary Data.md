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
**※ axis 매개변수의 기본값인 0은 행, 1은 열을 나타냄**
