
def second_max(lst):
    unique_lst = list(set(lst))  
    if len(unique_lst) >= 2:
        unique_lst.sort(reverse=True)
        return unique_lst[1]
    else:
        return "2-maksimal son mavjud emas."

user_input = input("Sonlarni vergul bilan ajratib kiriting: ")
lst = [int(x) for x in user_input.split(',')]

print("Listdagi 2-maksimal son:", second_max(lst))





def second_min(tpl):
    unique_tpl = tuple(set(tpl))  
    if len(unique_tpl) >= 2:
        return sorted(unique_tpl)[1]
    else:
        return "2-minimal son mavjud emas."

user_input_tuple = input(" sonlarni vergul bilan ajratib kiriting: ")
tpl = tuple(int(x) for x in user_input_tuple.split(','))

print(" 2-minimal son:", second_min(tpl))



def teskari_saralash_royxat(sonlar):
    saralangan_sonlar = sorted(sonlar, reverse=True)
    return saralangan_sonlar


sonlar = [10, 15 ,56, 44, 67]

print(teskari_saralash_royxat(sonlar))




from collections import Counter

def eng_kop_takrorlangan_qiymat(royxat):
    takrorlar = Counter(royxat)
    eng_kop_qiymat, takror_soni = takrorlar.most_common(1)[0]   
    return eng_kop_qiymat

a = int(input("1-Sonni kiriting: "))
b = int(input("2-Sonni kiriting: "))
c = int(input("3-Sonni kiriting: "))
d = int(input("4-Sonni kiriting: "))
boy = a, b, c, d
print("Eng ko'p takrorlangan qiymat:", eng_kop_takrorlangan_qiymat(boy))




from collections import Counter

def eng_kam_takrorlangan_qiymat(boy):
    hisoblagich = Counter(boy)
    eng_kam = min(hisoblagich, key=hisoblagich.get)
    return eng_kam

a = int(input("1-Sonni kiriting: "))
b = int(input("2-Sonni kiriting: "))
c = int(input("3-Sonni kiriting: "))
d = int(input("4-Sonni kiriting: "))
boy = a, b, c, d

natija = eng_kam_takrorlangan_qiymat(boy)
print("Eng kam takrorlangan qiymat:", natija)



def eng_katta_juft_son(boy):
    juft_sonlar = [son for son in boy if son % 2 == 0]
    
    if juft_sonlar:
        return max(juft_sonlar)
    else:
        return -1

a = int(input("1-Sonni kiriting: "))
b = int(input("2-Sonni kiriting: "))
c = int(input("3-Sonni kiriting: "))
d = int(input("4-Sonni kiriting: "))
boy = a, b, c, d


natija = eng_katta_juft_son(boy)
print("Eng katta juft son:", natija)




def largest_even(lst):

    evens = [x for x in lst if x % 2 == 0]
    
    return max(evens) if evens else -1

lst = [1, 3, 5, 7, 8, 10, 12, 15]

result = largest_even(lst)
print("Listdagi eng katta juft son:", result)




def uppercase_strings(lst):

    return [item for item in lst if isinstance(item, str) and item[0].isupper()]


lst = [1, True, "Salom", "nima", "Dunyo", 5, 5.6, "Yana"]

result = uppercase_strings(lst)
print("Katta harfdan boshlangan stringlar:", result)



def replace_with_types(lst):
    return [type(item) for item in lst]

lst = [True, "Salom", 5, 5.6]
print(replace_with_types(lst))


