''':cvar
0 을 완료하기 위해서는 1을 끝내야 한다는 것을 [0 , 1] 쌍으로 표현하는 n 개의 코스가 있다.
코스 개수 n 과 이 쌍들을 입력으로 받았을 때 모든 코스가 완료 가능한지 판별하라.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''

def canFinish(numCourses, prerequisites):
    return
