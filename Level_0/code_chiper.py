# https://school.programmers.co.kr/learn/courses/30/lessons/120892

def solution(cipher, code):
    answer = "".join(cipher[code - 1::code])
    return answer