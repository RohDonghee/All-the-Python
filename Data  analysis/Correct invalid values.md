# 잘못된 데이터 수정하기 
- 판다스에서는 누락된 값은 NaN으로 표시한다.
- 

## 데이터프레임 정보 요약 확인
```py
import gdown
gdown.download('https://bit.ly/3GisL6J', 'ns_book4.csv', quiet=False)
```
```py
ns_book4 = pd.read_csv('ns_book4.csv', low_memory=False)
ns_book4.info()
```
- ```info()```를 통해서 데이터프레임의 요약 정보를 확인할 수 있다.

## 누락된 값 처리하기
### ■ isna(), isnull() 메서드
- 해당 메서드를 사용하면 NaN를 직접 카운트할 수 있다.
- 각 행이 비어 있는지를 나타내는 **불리언 배열로 반환**
- sum()을 이어서 호출하면 불리언 배열의 True 개수로 비어 있는 행 개수를 얻을 수 있다.
```py
ns_book4.isna().sum()
```

### ■ None과 np.nan
- 임의로 누락된 값을 만든 후에 NaN으로 표시한다.
- 판다스 데이터프레임은 정수를 저장하는 열에 None이 입력되어 있으면 누락된 값으로 인식한다. 
```py
ns_book4.loc[0,'도서권수'] = None #0번째 행, '도서권수' 열의 값을 None으로 바꿈
ns_book4.head(2)
```
□ **기존 데이터프레임** <br>
![image](https://github.com/user-attachments/assets/16eeac4a-659c-4a05-888d-c7044555bc53)<br>
□ **```ns_book4.loc[0,'도서권수']``` 적용된 데이터프레임**  <br>
![image](https://github.com/user-attachments/assets/5024d806-b9a4-4589-93a9-346fde982bcf)<br>
※ 도서권수는 기존에 int 값에서 float형으로 변한 이유는 판다스가 NaN을 특별한 실수 값으로 저장하기 때문이다. 이를 바꿔주기 위해서는 ```astype({'도서권수':'int32' , '대출건수':'int32'})```를 실행해줘야 한다.<br>

## 누락된 값 바꾸기
### ■ loc,fillna() 메서드

