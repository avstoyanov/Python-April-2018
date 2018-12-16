num_list = list(map(int, input().split(" ")))
for num in range(0, len(num_list)):
    if num % 2 != 0 and num_list[num] % 2 != 0:
        print(f"Index {num} -> {num_list[num]}")
