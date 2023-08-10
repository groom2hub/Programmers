# https://school.programmers.co.kr/learn/courses/30/lessons/120889

def solution(sides):
    sides.sort()
    answer = 1 if sides[2] < sides[0] + sides[1] else 2
    return answer