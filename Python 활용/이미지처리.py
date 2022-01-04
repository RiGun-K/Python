# pillow - 이미징 라이브러리

import os
import cv2

from PIL import Image

# 이미지 열기
# im = Image.open('C:\Users\RiGun\Python\Python 활용\Profile.jpg')
im = Image.open('./Profile.jpg')

im.show()

# 이미지 크기 출력
print(im.size)

# 이미지 PNG로 저장
im.save('Profile.png')
