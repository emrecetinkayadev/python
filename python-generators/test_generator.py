import sys

# Örnek bir veri kümesi
data = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10, 11, 12, 13]

# Generator kullanımı


def get_items(n):
    i = 0
    while i < n:
        yield i
        i += 1


# Bellek kullanımını ölç
size = sys.getsizeof(data)
print(f"Veri kümesinin bellek kullanımı: {size} bayt")

# "get_items" fonksiyonunun bellek kullanımını ölç
size = sys.getsizeof(get_items(13))
print(f"get_items fonksiyonunun bellek kullanımı: {size} bayt")

# Kullanımı
for item in get_items(13):
    print(item)
