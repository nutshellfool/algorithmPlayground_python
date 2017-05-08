class MergeSort(object):
    def merge_sort(self, items):
        if len(items) <= 1:
            return items

        mid = len(items) / 2
        left = self.merge_sort(items[0:mid])
        right = self.merge_sort(items[mid:])

        # merge the 2 sorted list
        merged = MergeSort.merge_2_sorted(left, right)
        return merged

    @staticmethod
    def merge_2_sorted(l1, l2):
        """Merge sort two sorted lists

        Arguments:
        - `l1`: First sorted list
        - `l2`: Second sorted list
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        result = []
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
        result += l1[i:]
        result += l2[j:]
        return result
