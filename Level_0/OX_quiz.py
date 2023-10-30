# https://school.programmers.co.kr/learn/courses/30/lessons/120907

def solution(quiz):
    answer = []
    
    for i in quiz:
        if i.split()[1] == '+':
            answer.append("O" if int(i.split()[0]) + int(i.split()[2]) == int(i.split()[4]) else "X")
        elif i.split()[1] == '-':
            answer.append("O" if int(i.split()[0]) - int(i.split()[2]) == int(i.split()[4]) else "X")

    return answer