import heapq

def heap_sort(iterable, descending=False):
    sign = -1 if descending else 1
    h = [sign * el for el in iterable]
    heapq.heapify(h)
    return [sign * heapq.heappop(h) for _ in range(len(h))]

def cumulative_sum(arr):
    result = []
    total = 0
    for i in range(len(arr)):
        if i == 0:
            total = arr[i] 
        else:
            total += arr[i]
            result.append(total)  
    return sum(result)  

# Отримання введення від користувача
arr = list(map(int, input("Введіть довжини відрізків кабеля (через пробіл): ").split()))

# Сортування за зростанням
sorted_arr_asc = heap_sort(arr)
print("Відсортований масив відрізків кабелів (за зростанням):", sorted_arr_asc)
# Сортування за спаданням
sorted_arr_desc = heap_sort(arr, descending=True)
print("Відсортований масив відрізків кабелів (за спаданням):", sorted_arr_desc)


# Обчислення кумулятивної суми та загальної суми
cumulative_result = cumulative_sum(sorted_arr_asc)

cumulative_result_1 = cumulative_sum(sorted_arr_desc)

# Виведення результату
print("Кумулятивна сума для зєднання спочатку коротших відрізків:", cumulative_result)

print("Кумулятивна сума для зєднання спочатку довших відрізків:", cumulative_result_1)


