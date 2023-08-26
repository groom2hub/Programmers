# https://school.programmers.co.kr/learn/courses/30/lessons/181933

def solution(a, b, flag):
    answer = a + b if flag else a - b
    return answer