# https://school.programmers.co.kr/learn/courses/30/lessons/181926

def solution(n, control):
    answer = n
    for i in control:
        if i == 'w':
            answer += 1
        elif i == 's':
            answer -= 1
        elif i == 'd':
            answer += 10
        elif i == 'a':
            answer -= 10
    return answer