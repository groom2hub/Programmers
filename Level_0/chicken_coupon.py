# https://school.programmers.co.kr/learn/courses/30/lessons/120884

def solution(chicken):
    answer = 0
    while chicken > 9:
        answer += chicken // 10
        chicken = chicken % 10 + chicken // 10
    return answer