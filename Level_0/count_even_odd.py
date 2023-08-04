# https://school.programmers.co.kr/learn/courses/30/lessons/120824

def solution(num_list):
    answer = [0, 0]
    for n in num_list:
        answer[n%2] += 1
    return answer