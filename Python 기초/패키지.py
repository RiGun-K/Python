# 패키지 
# 모듈들을 모은 컬렉션을 가리킨다.
# 패키지는 모듈들의 컨테이너로서 패키지 안에는 또다른 서브 패키지를 포함할 수도있다.
# 각 디렉토리 및 모듈 사이에 점(.)을 사용

    # 모듈 import
    # import 패키지.모듈
#import models.account.bill
#models.account.bill.charge(1,50)

    # 모듈안의 모든 함수 import
    # from 패키지명 import 모듈명
#from models.account import bill
#bill.charge(1, 50)
 
    # 특정 함수만 import
    # from 패키지명.모듈명 import 함수명
#from models.account.bill import charge
#charge(1, 50)

# __init__.py

    # __init__.py 파일의 내용  
__all__ = ['bill']

    # 패지키내 모든 모듈 import
    # from 패키지명 import *
#from models.account import *
#bill.charge(1, 50)