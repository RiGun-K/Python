# 객체지향 프로그래밍( OOP )를 지원함.
# "class 클래스명" 을 사용하여 정의

# Python은 접근 제한자(public, protected, private)를 갖지 않는다. = 기본적으로 public
# 특정 변수명이나 메서드를 private로 만들려면 두개의 밑줄(__)을 이름 앞에 붙이자! 


class MyClass:
    pass    # 빈 클래스


# 클래스 멤버
    # 데이터 표현 ( 속성 )
    # 클래스의 행위를 표현 ( 메서드 ) = 클래스 내의 함수
    # 프로퍼티, 클래스 변수, 인스턴스 변수, 초기자 등등...

# 메서드
    # 인스턴스, 클래스, 정적 메서드
    # 인스턴스 메서드 : 인스턴스 변수에 엑서스 할 수 있도록 
    #                  메서드의 첫번째 파라미터에 항상 객체 자신을 의미하는
    #                   "self"라는 파라미터를 갖는다.
class Rectangle:
    count = 0   # 클래스 변수

    # 초기자
    def __init__(self, width, height):
        # self.* : 인스턴스 변수
        self.width = width
        self.height = height
        Rectangle.count += 1
    
    # 메서드
    def calcArea(self):
        area = self.width * self.height
        return area
    
# 클래스 변수
    # 메서드 밖에 존재하는 변수
    # 클래스 내외부에서 "클래스명.변수명" 으로 엑세스 할 수 있다.
    # 하나의 클래스에 하나만 존재

# 인스턴스 변수
    # 하나의 클래스로부터 여러 객체 인스턴스를 생성하여 사용
    # 메서드 안에서 사용되면서 "self.변수명" 처럼 사용 

def __init__(self, width, height):
    self.width = width
    self.height = height
 
    # private 변수 __area           # private 사용시 이름 앞에 두개의 밑줄(__) 사용
    self.__area = width * height
 
    # private 메서드                # private 사용시 이름 앞에 두개의 밑줄(__) 사용
def __internalRun(self):
    pass


