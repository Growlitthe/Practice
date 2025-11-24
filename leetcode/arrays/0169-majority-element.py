#Majority Element - Dictionary ile çözüm
'''def majorityElement(nums: list[int]) -> int:
    sozluk = {}

    for i in nums:
        if i in sozluk.keys():
            sozluk[i] +=1
        else:
            sozluk[i] = 1

    enBuyuk = 0

    for key, value in sozluk.items():
        if value > enBuyuk:
            enBuyuk = value
            sonuc = key
    return sonuc

liste = [3,2,3,2,2,3,3,3,2,2,2,2,2,2,2,2,2]
print(majorityElement(liste))'''


#Majority Element - Boyer-Moore Voting ile çözüm
'''def majorityElement(nums: list[int]) -> int:
    aday = 0
    sayac = 0

    for i in nums:

        if sayac == 0:
            aday = i

        if aday == i:
            sayac += 1
        else:
            sayac -= 1
    return aday

liste = [3,2,3,2,2]
print(majorityElement(liste))'''










