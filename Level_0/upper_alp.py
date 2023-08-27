# https://school.programmers.co.kr/learn/courses/30/lessons/181873

def solution(my_string, alp):
    answer = my_string.replace(alp, alp.upper())
    return answer