def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    
    return result

def binarySearch(lys, val) :
    first = 0
    last = len(lys) - 1
    row = -1

    while (first <= last) and (row == -1) :
        mid = (first + last) // 2

        if lys[mid] == val:
            row = mid
        else :
            if val < lys[mid] :
                last = mid - 1
            else:
                first = mid + 1
    
    return row

# fungsi untuk mensorting nested list
def sort_nested_dataset(dataset) :
    dataset_sorted = []
    nested_dataset = {} # untuk menyimpan nested list (sebagai value) beserta index nya (sebagai key)

    # memisahkan nilai string dan list
    # nilai string ke dalam dataset_sorted dan nilai list ke dalam nested_dataset
    for i in range(len(dataset)) :
        if type(dataset[i]) == str :
            dataset_sorted.append(dataset[i])
        else :
            nested_dataset[i] = merge_sort(dataset[i])

    # mensorting list yang berisi string
    dataset_sorted = merge_sort(dataset_sorted)

    # lalu memasukan kembali list yang dipisah sesuai dengan indexnya semula
    for i in nested_dataset :
        dataset_sorted.insert(i, nested_dataset[i])

    return dataset_sorted

dataset = ['galda', 'zaki', ['ibnu', 'zaki'], 'kalam', ['zaki', 'ari', 'ibnu'], 'zaki']
dataset_sorted = sort_nested_dataset(dataset)
cari = input('\nSiapa yang ingin dicari?\n> ')

print(f"\nMencari '{cari}' pada\nDataset awal      : {dataset}\nDataset disorting : {dataset_sorted}\n")

for row in range(len(dataset_sorted)) :
    # jika typenya list, maka cari nilainya di dalam list tersebut sebagai column
    if type(dataset_sorted[row]) == list :
        column = binarySearch(dataset_sorted[row], cari)
        if column != -1 : print(f'{cari} berada di array index ke - {row} kolom {column}')
    else :
        if dataset_sorted[row] == cari : print(f'{cari} berada di array index ke - {row}')
