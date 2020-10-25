def sort(arr, n):
    length = len(arr)
    start = 0
    while True:
        end = start + n
        if end >= length:
            break
        if arr[end] < arr[start]:
            index = start
            value = arr[end]
            while index >= 0 and value < arr[index]:
                arr[index + n] = arr[index]
                if index-n >= 0:
                    index -= n
                else:
                    index -= n
                    break
            arr[index+n] = value
        start += 1


def sortt(arr):
    length = len(arr)
    start = 0
    while length > 1:
        end = start + 1
        if arr[end] < arr[start]:
            index = start
            value = arr[end]
            while index >= 0 and value < arr[index]:
                arr[index + 1] = arr[index]
                index -= 1
            arr[index+1] = value
        length -= 1
        start += 1


if __name__ == '__main__':
    arr1 = [1,3,5,78,9,6,4,2,4,789,87,54,2,1,23,6,9,0,7,34,4,6]
    print(arr1)
    sortt(arr1)
    print(arr1)
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1024, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1025, 9, 0, 0]
    print(arr)
    sort(arr, 4)
    print(arr)
