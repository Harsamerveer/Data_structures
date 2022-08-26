
def InsertionSort(elements):

    # index i , j and anchor
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1

        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
            print(elements[j])
            elements[j+1] = anchor

            print(elements[j+1])

   # print(statistics.median(elements))

if __name__ == '__main__':

    elements = [12,56,8,21,82,1,9,23]

    InsertionSort(elements)
    print(elements)

    # Medium of an even numbered list is the average of the two middle numbers in sorted list

