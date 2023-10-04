# https://school.programmers.co.kr/learn/courses/30/lessons/120891

def solution(order):
    answer = str(order).count("3") + str(order).count("6") + str(order).count("9")
    return answer