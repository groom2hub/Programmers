# https://school.programmers.co.kr/learn/courses/30/lessons/120908

def solution(str1, str2):
    answer = 2 if len(str1) == len(str1.replace(str2, '')) else 1
    return answer