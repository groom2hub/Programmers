# https://school.programmers.co.kr/learn/courses/30/lessons/120814

def solution(n):
    answer = 1 + n // 7 if n % 7 != 0 else n // 7
    return answer