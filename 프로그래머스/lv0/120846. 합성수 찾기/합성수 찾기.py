def solution(n):
    answer = 0
    for i in range(1,n+1):
        l = []
        for j in range(1,i+1):
            if i % j == 0:
                l.append(j)
        if len(l) >= 3:
            answer += 1
    return answer