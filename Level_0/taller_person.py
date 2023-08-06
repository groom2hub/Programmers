# https://school.programmers.co.kr/learn/courses/30/lessons/120585

def solution(array, height):
    answer = 0
    array.sort()
    for i in array[::-1]:
        if i > height:
            answer += 1
        else:
            break
    return answer