# Example Input

# 3
# 4 3 5 7 13
# 4 2 4 8 16
# 4 5 3 1 7
# Output

# 2
# 4
# 1
# Explanation:

# Case 1: we have powers: 3: 011, 5: 101, 7: 111, 13: 1101. Combining 13 and 7 will give us 15 : 1111, which is the same as the bitwise OR of entire batteries. Thus answer is 2 - only 2 batteries needed

# Case 2: we need all 4 numbers to reach combined powers of  11110

# Case 3: we only need 7 ( 111) to reach the same combined power as the entire batteries


for i in range(int(input())):
    arr=list(map(int,input().split()))[1:]
    res=0
    for i in arr:
        res=res|i
    arr.sort()
    arr.reverse()
    i=0
    check=0
    count=0
    prev=0
    while(i<len(arr)):
        check=prev|arr[i]
        if prev!=check:
            count+=1
            prev=check
        i+=1
    print(count)
    
        



