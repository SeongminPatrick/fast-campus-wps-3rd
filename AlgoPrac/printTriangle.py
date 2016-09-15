# -*- coding: utf-8 -*-
"""
printTriangle 메소드는 양의 정수 num을 매개변수로 입력받습니다.
다음을 참고해 *(별)로 높이가 num인 삼각형을 문자열로 리턴하는 printTriangle 메소드를 완성하세요
printTriangle이 return하는 String은 개행문자('\n')로 끝나야 합니다.
"""

def printTriangle(num):
    s = ""
    for i in range(num):
        s += "*" * (i+1) + "\n"
    return s
print( printTriangle(3) )
