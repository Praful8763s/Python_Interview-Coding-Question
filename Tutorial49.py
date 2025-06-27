def sorting_tuples(tuples):
    tuples = list(tuples)  # Convert tuple to list
    for i in range(len(tuples)):
        for j in range(i + 1, len(tuples)):
            if tuples[i] > tuples[j]:
                tuples[i], tuples[j] = tuples[j], tuples[i]
    return tuples

tuples = (3, 1, 7, 5, 43, 3, 9, 2)
sorting_array = sorting_tuples(tuples)
print(sorting_array)
