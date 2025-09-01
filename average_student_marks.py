'''Input (stdin)
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Expected Output
56.00'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    output = sum(student_marks[query_name]) / len(student_marks[name])
    print(f"{output:.2f}")



