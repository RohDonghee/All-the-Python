### 불필요한 데이터 삭제하기 
API, 웹 스크래핑, 데이터베이스 등으로 수집한 불완전한 데이터를 삭제하는 방법

```python
import pandas as pd
df = pd.read_csv('남산도서관 장서 대출목록 (2021년 04월).csv', encoding='EUC-KR')
```
![image](https://github.com/user-attachments/assets/f69df931-25ec-4feb-b2fa-e81ef37d8af3)<br>
- csv 파일 각 라인 끝에 존재하는 콤마로 인해 ***Unnamed:13***이 존재한다.
- 불필요한 데이터 열이기 때문에 삭제해야 한다.

```python
ns_df = pd.read_csv('남산도서관 장서 대출목록 (2021년 04월).csv', low_memory=False)
ns_book = ns_df.loc[:,'번호':'등록일자'] 
ns_book.head()
```
![image](https://github.com/user-attachments/assets/2ede0316-aad0-4a0b-92d6-75046c881c8a)<br>
- ```loc```는 location의 약어로, 데이터프레임의 행 또는 칼럼의 라벨이나 불리언 array를 인덱싱한다.
- '번호'열부터 '등록일자'열까지 출력한다.
