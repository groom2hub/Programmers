# https://school.programmers.co.kr/learn/courses/30/lessons/181903

def solution(q, r, code):
    answer = ''.join([code[i] for i in range(len(code)) if i % q == r])
    return answer