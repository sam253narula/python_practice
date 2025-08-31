'''
For this hackerrank question, create a better solution then this:
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
Input Format
The first line contains . The second line contains an array   of  integers each separated by a space.
Constraints
Output Format
Print the runner-up score.
Sample Input 0
5
2 3 6 6 5

Sample Output 0
5
'''

# Solution 1
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    unique_list = list(set(arr))
    print('unique_list', unique_list)
    unique_list.sort(reverse=True)
    print(unique_list[1])

# Solution 2
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    unique_list = list(set(arr))
    # By using -2 we are fetching the second last element from array
    print(unique_list[-2])