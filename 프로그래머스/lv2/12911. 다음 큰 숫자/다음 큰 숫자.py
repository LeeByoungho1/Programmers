def solution(n):
    answer = n+1
    while bin(n)[2:].count('1') != bin(answer)[2:].count('1'):
        answer += 1
    return answer