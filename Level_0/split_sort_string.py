# https://school.programmers.co.kr/learn/courses/30/lessons/181866

def solution(myString):
    answer = [ i for i in myString.split("x") if i ]
    answer.sort()
    return answer