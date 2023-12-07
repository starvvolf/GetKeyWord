import sys
import urllib.request
from bs4 import BeautifulSoup
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTextEdit, QSpinBox, QListWidget

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("projectUI.ui")[0]

def extract_keywords(title):
      keywords = []
      for word in title.split():
        if len(word) >= 2:
          keywords.append(word)
      return keywords

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 화면을 보여준다.
        self.show()
        self.textEdit.textChanged.connect(self.update_search_query)
        self.spinBox.valueChanged.connect(self.update_search_count)
        self.pushButton.clicked.connect(self.search)
        
        
        
        self.query=""
        self.count=10
    def search(self):
    # 키워드 추출
      
    
    # 키워드 빈도수 계산
        word_counts = {}
        for i in range(0, self.count):
            keywords=self.get_title(self.query, (i*30)+1)
            for word in keywords:
                if word not in word_counts:
                    word_counts[word]=0
                word_counts[word]+=1
        
        # 정렬
        sorted_keywords = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        
        # 출력
        self.listWidget.clear()
        for keyword, count in sorted_keywords:
          self.listWidget.addItem(f"{keyword}: {count}")

    def update_search_query(self):
         self.query = self.textEdit.toPlainText()

    def update_search_count(self, value):
        self.count = value
        
    

    def get_title(self, query, count):
        url = f"https://search.naver.com/search.naver?query={urllib.request.quote(query)}&nso=&where=blog&sm=tab_opt&start={max(1, count)}"
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        titles = soup.find_all(class_="title_area")
        keywords = []
        for title in titles:
            keywords += extract_keywords(title.text.strip())
        return keywords
    
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()