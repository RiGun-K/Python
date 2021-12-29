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

# 초기자
    # 클래스로부터 새 객체를 생성할 때마다 실행되는 
    # __init__() 이라는 메서드가 있는데, 이를 흔히 클래스 Initializer 라 부른다

# 정적 메서드와 클래스 메서드
    # 정적 메서드
        # 메서드 앞에 @staticmethod 표시
    
    # 클래스 메서드
        # 메서드 앞에 @classmethod 표시

class Rectangle:
    count = 0  # 클래스 변수
 
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1
 
    # 인스턴스 메서드
    def calcArea(self):
        area = self.width * self.height
        return area
 
    # 정적 메서드
    @staticmethod
    def isSquare(rectWidth, rectHeight):
        return rectWidth == rectHeight   
 
    # 클래스 메서드
    @classmethod
    def printCount(cls):
        print(cls.count)   
 
# 테스트
square = Rectangle.isSquare(5, 5)        
print(square)   # True        
 
rect1 = Rectangle(5, 5)
rect2 = Rectangle(2, 5)
rect1.printCount()  # 2

# Special Method(Magic Method)
    # 객체가 소멸될때 (__del__) 메서드
    # 두 개의 객체를 더하는 + (__add__) 메서드
    # 두 개의 객체를 빼는 - (__sub__) 메서드
    # 두 개의 객체를 비교 (__cmp__) 메서드
    # 문자열로 객체를 표현 (__str__) 메서드

def __add__(self, other):
    obj = Rectangle(self.width + other.width, self.height + other.height)
    return obj
 
# 사용 예
r1 = Rectangle(10, 5)
r2 = Rectangle(20, 15)
r3 = r1 + r2  # __add__()가 호출됨


# 클래스 인스턴스 생성과 사용
    # 클래스 생성전 인스턴스(객체)를 생성해야 함
    # "객체변수명 = 클래스명()"과 같이 클래스명을 함수 호출처럼 사용

# 인스턴스 생성
r = Rectangle(2, 3)
 
# 메서드 호출
area = r.calcArea()
print("area = ", area)
 
# 인스턴스 변수 엑세스
r.width = 10
print("width = ", r.width)
 
# 클래스 변수 엑세스
print(Rectangle.count)
print(r.count)

r = Rectangle(2, 3)
 
Rectangle.count = 50
r.count = 10   # count 인스턴스 변수가 새로 생성됨
 
print(r.count, Rectangle.count)  # 10  50 출력

# 클래스 상속과 다형성
    # 상속
        # 자식클래스에서 클래스명 뒤에 부모클래스 이름을 괄호와 함께 넣어주면 된다.

class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("move")
    def speak(self):
        pass
 
class Dog (Animal):
    def speak(self):
        print("bark")
 
class Duck (Animal):
    def speak(self):
        print("quack")

# 자식클래스는 부모클래스의 멤버들을 호출하거나 사용, 자신의 멤버들을 사용가능
dog = Dog("doggy") # 부모클래스의 생성자
n = dog.name # 부모클래스의 인스턴스변수
dog.move()   # 부모클래스의 메서드
dog.speak()  # 파생클래스의 멤버   

    # 다형성
        # animals 리스트에 Dog, Duck 객체를 넣고 이들의 speak() 메서드 호출
        # 객체의 타입에 따라 서로 다른 speak() 메서드가 호출됨 
animals = [Dog('doggy'), Duck('duck')]
 
for a in animals:
    a.speak()