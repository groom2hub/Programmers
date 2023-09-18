# https://school.programmers.co.kr/learn/courses/30/lessons/181939

def solution(a, b):
    answer = int(max(str(a) + str(b), str(b) + str(a)))
    return answer