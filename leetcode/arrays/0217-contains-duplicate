#Sözlük kullanımı ile çözüm
def containsDuplicate(nums: list[int]) -> bool:
    sozluk = {}

    for i in nums:
        if i in sozluk:
            sozluk[i] += 1
        else:
            sozluk[i] = 1

    for key, value in sozluk.items():
        if value >= 2:
            return True

    return False

sayilar = [1, 2, 3, 3, 4]
sonuc = containsDuplicate(sayilar)

print(sonuc)
