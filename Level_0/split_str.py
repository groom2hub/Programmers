# https://school.programmers.co.kr/learn/courses/30/lessons/181862

def solution(myStr):
    splitStr = ['a', 'b', 'c']
    for i in splitStr:
        myStr = myStr.replace(i, ' ')

    answer = [i for i in myStr.split()] 
    if len(answer) == 0:
        answer.append("EMPTY")
    
    return answer