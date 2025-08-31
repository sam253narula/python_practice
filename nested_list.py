'''Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry'''

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    scores = []
    for record in records:
        scores.append(record[1])

    scores = list(set(scores))
    scores.sort()
    students_with_second_lowest_scores = [record[0] for record in records if record[1] == scores[1]]
    sorted_boys = sorted(students_with_second_lowest_scores)
    for student in sorted_boys:
        print(student)