'''
Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

Example 2:
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


1. 문자 로그는 숫자로그 보다 앞에 있다.
2. 문자 로그는 내용에 따라 사전 순으로 정렬된다.내용이 같으면 식별자를 기준으로 정렬
3. 숫자 로그는 상대적인 순서를 유지한다.
'''
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]


def reorderLogFiles(self, logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 두 개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
