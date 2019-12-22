def sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr.pop(0) + sum(arr)

if __name__ == "__main__":
    print(sum([2, 4, 5, 7]))