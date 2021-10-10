###############################################################
# 4. 팩토리얼 구하기
###############################################################

# 4-1
def c4_1(n):
    if n < 1:
        return 0
    return n + c4_1(n - 1)

print(c4_1(6))


# 4-2
def c4_2(numList, count):
    if count <= 1:
        return numList[0]
    else:
        if numList[count - 1] > c4_2(numList, count - 2):
            return numList[count - 1]
        else:
            return c4_2(numList, count - 2)



numArray = [1, 2, 3, 4, 5, 7, 3, 5]
print(c4_2(numArray, len(numArray)))