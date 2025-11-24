#Single number. XOR kullanımı.
#a ^ a = 0, a ^ 0 = a
'''print(2^2^1)

def singleNumber(nums: list[int]) -> int:
    sonuc = 0

    for i in nums:
        sonuc = sonuc ^ i

    return sonuc

liste = [2,2,1]

print(singleNumber(liste))'''

#set ve sum ile çözüm
'''def singleNumber(nums: list[int]) -> int:
    return sum(set(nums)) * 2 - sum(nums)

liste = [4,1,2,1,2]
print(singleNumber(liste))'''
