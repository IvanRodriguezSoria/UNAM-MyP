
class MergeSort():
    """
    Merge sort algorithm.
    Sorts a list of number in assending order without changing
    the original list.
    """

    def __init__(self):
        pass

    def merge(self, left, right):
        """
        Merge 2 list and returns a new ordered one.

        left    First list to merge.
        right   Second list to merge.
        """
        ordered_list = list()
        left_list_size = len(left)
        right_list_size = len(right)
        while(len(left) > 0 and len(right) > 0):
            if left[0] <= right[0]:
                ordered_list.append(left.pop(0) )
            else:
                ordered_list.append(right.pop(0) )
        for element in left:
            ordered_list.append(element)
        for element in right:
            ordered_list.append(element)
        return ordered_list

    def merge_sort(self, unordered_list):
        """
        Merge sort recursive algorith.
        This algorith divides the list in half creating
        left_list and right_list, then merges both
        in a new ordered one.

        unordered_list  An unordered list to be ordered.
        """
        length = len(unordered_list)
        if length <= 1:
            return unordered_list
        left_list = list()
        right_list = list()
        for i in range(length):
            if i < length // 2:
                left_list.append(unordered_list[i] )
            else:
                right_list.append(unordered_list[i] )
        left = self.merge_sort(left_list)
        right = self.merge_sort(right_list)
        return self.merge(left, right)

if __name__ == '__main__':
    aux = [1,9,2,8,3,7,3,7,4,6,5,1,2,4,6,8,9,6,5,4,3,4,5,6,5,4,3,4,5,6,7,66,7,55,4]
    ms = MergeSort()
    print(ms.merge_sort(aux))

