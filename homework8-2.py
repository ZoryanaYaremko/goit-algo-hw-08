import heapq

def merge_k_lists(lists):
    # Ініціалізуємо мінімальну купу
    min_heap = []

    # Додаємо перші елементи всіх списків до купи
    for i, lst in enumerate(lists):
        if lst:  # Перевіряємо, чи список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))

    merged_list = []

    # Об'єднуємо списки
    while min_heap:
        # Витягуємо найменший елемент з купи
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)

        # Якщо є наступний елемент у списку, додаємо його до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))

    return merged_list

if __name__ == '__main__':
    # Приклад використання
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
