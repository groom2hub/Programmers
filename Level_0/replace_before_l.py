# https://school.programmers.co.kr/learn/courses/30/lessons/181834

def solution(myString):
    answer = ''.join(i if i > 'l' else 'l' for i in myString)
    return answer