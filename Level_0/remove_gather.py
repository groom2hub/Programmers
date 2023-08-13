# https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        my_string = my_string.replace(i, '')
    
    return my_string