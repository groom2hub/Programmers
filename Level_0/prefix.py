# https://school.programmers.co.kr/learn/courses/30/lessons/181906

def solution(my_string, is_prefix):
    answer = 1 if my_string[:len(is_prefix)] == is_prefix else 0
    return answer