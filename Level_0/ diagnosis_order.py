# https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    sorted_list = sorted(emergency, reverse = True)
    emergency_dic = {sorted_list[i]:i+1 for i in range(len(sorted_list))}
    answer = [emergency_dic[i] for i in emergency]
    return answer