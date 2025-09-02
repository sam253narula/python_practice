'''
input (stdin)
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66
Expected Output
38
'''

# Solution 1:
# Enter your code here. Read input from STDIN. Print output to STDOUT
num_of_elems = int(input())
set_A = set(input().split())
num_of_other_sets = int(input())
ops_tuple = []
for _ in range(num_of_other_sets):
    ops_info = input().split()
    ops_name = ops_info[0]
    ops_elems = set(input().split())
    ops_tuple.append((ops_name, ops_elems))

for i in range(len(ops_tuple)):
    ops_name = ops_tuple[i][0]
    ops_elems = ops_tuple[i][1]
    if (ops_name == "update"):
        set_A.update(ops_elems)
    elif (ops_name == "intersection_update"):
        set_A.intersection_update(ops_elems)
    elif (ops_name == "symmetric_difference_update"):
        set_A.symmetric_difference_update(ops_elems)
    elif (ops_name == "difference_update"):
        set_A.difference_update(ops_elems)
    else:
        print(f"unknown ops: {ops_name}")

print(sum(map(int, set_A)))


# Solution 2:
# Enter your code here. Read input from STDIN. Print output to STDOUT
num_of_elems = int(input())
set_A = set(input().split())
num_of_other_sets = int(input())
ops_tuple = []
for _ in range(num_of_other_sets):
    ops_info = input().split()
    ops_name = ops_info[0]
    ops_elems = set(input().split())
    # getattr(object, methods)(arguments for method to be performed on object)
    getattr(set_A, ops_name)(ops_elems)

print(sum(map(int, set_A)))

