# https://school.programmers.co.kr/learn/courses/30/lessons/120875

def solution(dots):
    answer = 0
    combination = [[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2], [1, 3, 0, 2]]
    
    for c in combination:
        slope_1 = (dots[c[0]][1] - dots[c[1]][1]) / (dots[c[0]][0] - dots[c[1]][0])
        slope_2 = (dots[c[2]][1] - dots[c[3]][1]) / (dots[c[2]][0] - dots[c[3]][0])
        if slope_1 == slope_2:
            answer = 1
            break
    
    return answer