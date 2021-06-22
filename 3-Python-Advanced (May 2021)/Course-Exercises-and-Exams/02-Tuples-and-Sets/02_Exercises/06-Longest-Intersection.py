# 6.	Longest Intersection
# Write a program that finds the longest intersection. You will be given a number N.
# On the next N lines you will be given two ranges in the format: "{first start},{first end}-{second start},{second end}".
# Find the intersection of these two ranges and save the longest one of all N intersections.
# At the end print the numbers that are included in the longest intersection and its length in the format:
# "Longest intersection is [{longest intersection}] with length {length longest intersection}"
# Note: in each range, there will always be intersection. If there are two equal intersections, print the first one.

N = int(input())

intersections = []

for _ in range(N):
    first_sequence_data, second_sequence_data = input().split('-')

    start, stop = [int(el) for el in first_sequence_data.split(',')]
    first_seq = range(start, stop+1)

    start, stop = [int(el) for el in second_sequence_data.split(',')]
    second_seq = range(start, stop+1)

    intersection = set(first_seq).intersection(second_seq)

    intersections.append(intersection)

longest = sorted(intersections, key=lambda x: -len(x))[0]

print(f"Longest intersection is {list(longest)} with length {len(longest)}")

# N = int(input())
#
# intersections = []
#
# for _ in range(N):
#     first_set_range, second_set_range = input().split('-')
#     first_set_range = first_set_range.split(',')
#     second_set_range = second_set_range.split(',')
#     first_set = set()
#     second_set = set()
#
#     for el in range(int(first_set_range[0]), int(first_set_range[1])+1):
#         first_set.add(el)
#
#     for el in range(int(second_set_range[0]), int(second_set_range[1])+1):
#         second_set.add(el)
#
#     intersection = first_set.intersection(second_set)
#
#     intersections.append(intersection)
#
# intersections_lengths = [len(intersection) for intersection in intersections]
#
# index_of_max_intersection_length = intersections_lengths.index(max(intersections_lengths))
#
# print(f"Longest intersection is {list(intersections[index_of_max_intersection_length])} with length {max(intersections_lengths)}")
