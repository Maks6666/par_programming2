# 1
# При старті додатку запускаються три потоки. Перший
# потік заповнює список випадковими числами. Два інші потоки
# очікують на заповнення. Коли перелік заповнений, обидва
# потоки запускаються. Перший потік знаходить суму елементів
# списку, другий потік знаходить середнє арифметичне значення
# у списку. Отриманий список, сума та середнє арифметичне
# виводяться на екран.

import threading

lst = []
def full_list(lenght):
    for i in range(lenght):
        num = int(input(f"Input {i+1}st number: "))
        lst.append(num)
    print(lst)
    return lst


def lst_summ(lst):
    el = 0
    for i in lst:
        el += i
    print(f"Summa is {el}")

def mid(lst):
    el = 0
    for i in lst:
        el += i
    mid_value = el/len(lst)
    print(f"Medium value is {mid_value}")


t1 = threading.Thread(target=full_list, args=(5, ))
t1.start()
t1.join()

if len(lst) > 0:
    t2 = threading.Thread(target=lst_summ, args=(lst,))
    t2.start()
    t2.join()

    t3 = threading.Thread(target=mid, args=(lst,))
    t3.start()
    t3.join()
else:
    raise Exception("List is empty")
