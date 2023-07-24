# https://school.programmers.co.kr/learn/courses/30/lessons/120831

def solution(n):
    answer = sum([i for i in range(n + 1) if i % 2 == 0])
    return answer