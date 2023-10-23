# https://school.programmers.co.kr/learn/courses/30/lessons/120848

import math

def solution(n):
    answer = 0
    for i in range(10, 0, -1):
        if math.factorial(i) <= n:
            answer = i
            break
    return answer