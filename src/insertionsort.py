class InsertionSort(object):
    def insertion_sort(self, items):
        for i in range(1, len(items)):
            j = i
            while j > 0 and items[j] < items[j - 1]:
                items[j], items[j-1] = items[j - 1], items[j]
                j -= 1

        return items

if __name__  == '__main__':
    insertionSort = InsertionSort()
    print insertionSort.insertion_sort([5, 4, 3, 2, 1])