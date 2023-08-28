# https://school.programmers.co.kr/learn/courses/30/lessons/181929

def solution(num_list):
    mul_nums = 1
    for i in num_list:
        mul_nums *= i
    answer = 1 if sum(num_list) ** 2 > mul_nums else 0
    
    return answer