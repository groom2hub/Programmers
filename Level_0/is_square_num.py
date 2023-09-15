# https://school.programmers.co.kr/learn/courses/30/lessons/120909

def solution(n):
    answer = 1 if int(n ** (1/2)) == n ** (1/2) else 2
    return answer