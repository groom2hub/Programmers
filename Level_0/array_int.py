# https://school.programmers.co.kr/learn/courses/30/lessons/181835

def solution(arr, k):
    answer = [i * k if k % 2 == 1 else i + k for i in arr]
    return answer