fkey = input()
fval = input()
pairs = int(input())
pair_Dict = {}

# split inputs into key/value pairs
for num in range(pairs):
    key, values = input().split(" => ")
    pair_Dict[key] = values.split(";")

# print
for nums in pair_Dict:
    if fkey in nums:
        print(nums + ":")
        for each in pair_Dict[nums]:
            if fval in each:
                print("-" + each)
