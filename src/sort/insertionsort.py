class InsertionSort(object):
    def insertion_sort(self, items):
        for i in range(1, len(items)):
            j = i
            while j > 0 and items[j] < items[j - 1]:
                items[j], items[j - 1] = items[j - 1], items[j]
                j -= 1

        return items
