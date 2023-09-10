# https://school.programmers.co.kr/learn/courses/30/lessons/181901

def solution(n, k):
    answer = [i * k for i in range(1, n//k + 1)]
    return answer