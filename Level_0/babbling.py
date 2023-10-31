# https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling):
    answer = 0
    possible_babbling = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for j in possible_babbling:
            if i.count(j) < 2:
                # 단어 사이에 공백을 추가하여 기존에 없던 발음이 가능한 단어 생성 배제
                # ex) wyeoo -> w oo
                i = i.replace(j, ' ')
            else:
                # 네 가지 발음이 두 번 이상일 경우
                break
                
        # 공백을 제외한 모든 단어가 발음이 가능할 경우 
        if len(i.strip()) == 0:
            answer += 1
        
    return answer