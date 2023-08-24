# https://school.programmers.co.kr/learn/courses/30/lessons/181915

def solution(my_string, index_list):
    answer = ''.join(my_string[i] for i in index_list)
    return answer