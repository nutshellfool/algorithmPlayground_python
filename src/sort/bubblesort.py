class BubbleSort(object):
    def bubble_sort(self, items):
        for i in range(len(items)):
            for j in range(len(items) - i - 1):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
        return items
