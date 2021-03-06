'''
Given a string paragraph and a string array of the banned words banned,
return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.

금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지 않으며 , 구두점(마친표 , 쉼표 등) 또한 무시한다.

ex 1
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"

ex 2
Input: paragraph = "a.", banned = []
Output: "a"

ex 3:
Input: paragraph = "Bob", banned = []

'''

#Input  = "Bob hit a ball, the hit BALL flew far after it was hit."
#banned = ["hit"]

Input  = "a."
banned = []

#Input  = "Bob"
#banned = []

import re
import collections

def mostCommonWord(paragraph, banned):
    string_list = paragraph.lower()
    string_list = re.sub("[^a-z ]","",string_list)
    if len(banned)==0:
        string_list = string_list.split()
    else:
        for b in banned:
            string_list = string_list.replace(f"{b}","")
    
    string_list = string_list.split()
    string_list = collections.Counter(string_list).most_common(1)
    return string_list[0][0]


print(mostCommonWord(Input , banned))


# 풀이1

import collections
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]
    
    
# 풀이 2

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #1). replace the punctuations with spaces,
        #      and put all letters in lower case
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        #2). split the string into words
        words          = normalized_str.split()

        word_count     = defaultdict(int)
        banned_words   = set(banned)

        #3). count the appearance of each word, excluding the banned words
        for word in words:
            if word not in banned_words:
                word_count[word] += 1

        #4). return the word with the highest frequency
        return max(word_count.items(), key=operator.itemgetter(1))[0]
    
    
    
