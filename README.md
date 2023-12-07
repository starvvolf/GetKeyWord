# GetKeyWord



## 설치
![스크린샷 2023-12-08 004606](https://github.com/starvvolf/GetKeyWord/assets/118524918/63582d9c-df71-4e52-baba-a7d2aca1778d)
getkeyword.py와 projectUI.ui가 같은 폴더에 있어야 합니다.



## 설명


![image](https://github.com/starvvolf/GetKeyWord/assets/118524918/6e398ee0-55c0-4c76-9812-465122e4c42d)

![스크린샷 2023-12-08 001029](https://github.com/starvvolf/GetKeyWord/assets/118524918/4fdad220-1021-444a-9e53-aeb646e3e533)


검색어와 가져올 글의 개수(설정수치x30)를 지정하면 정해진 개수만큼 검색어 관련 네이버 블로그 글 제목의 키워드를 정리합니다.


띄어쓰기로 단어를 구분하며(ex '후쿠오카여행'/'후쿠오카'/'여행'을 각각 구분), 단어의 출현 빈도 순으로 정리해줍니다.


---

딜레이 없이 크롤링을 하게 되면 http에러가 발생해서 설정수치 1(글 30개)당 0.5초의 딜레이를 두었습니다.


답답하면 필요에 따라서 소스코드의
```
 word_counts = {}
        for i in range(0, self.count):
            keywords=self.get_title(self.query, (i*30)+1)
            time.sleep(0.5)
            for word in keywords:
                if word not in word_counts:
                    word_counts[word]=0
                word_counts[word]+=1
```


time.sleep()수치를 조정하면 속도를 올릴 수 있습니다.


## 개발 환경

conda 23.11.0 (python 3.11.5)


bs4


pyqt                      5.15.10


pyqt5-sip                 12.13.0



## Reference


https://jy-tblog.tistory.com/26


google Bard
