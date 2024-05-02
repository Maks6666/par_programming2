# 2
# Користувач вводить з клавіатури шлях до файлу. Після
# чого запускаються три потоки. Перший потік заповнює файл
# випадковими числами. Два інші потоки очікують на заповнення.
# Коли файл заповнений, обидва потоки стартують.
# Перший потік знаходить усі прості числа, другий потік знаходить факторіал кожного числа у файлі.
# Результати пошуку кожен потік має записати у новий файл.
# Виведіть на екран статистику виконаних операцій.

import threading
import pickle
import random
import math


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

data = []
def create_file(data):
    data = []
    file_name = input("Input file name: ")
    numbers = int(input("Input length of the list: "))
    for i in range(numbers):
        num = random.randint(1, 10)
        data.append(num)
    with open(f"{file_name}.pickle", "wb") as file:
        pickle.dump(data, file)
    print("Data saved.")


def prime_numbers(file_name, new_file_name):
    print("Function 'prime_numbers' starts: ")
    prime_numbers_list = []
    with open(file_name, "rb") as file:
        read_data = pickle.load(file)
        if len(read_data) > 0:
            for num in read_data:
                if is_prime(num):
                    prime_numbers_list.append(num)
            print(prime_numbers_list)
            with open(f"{new_file_name}.pickle", "wb") as file:
                pickle.dump(prime_numbers_list, file)
            print("Data saved.")



def factorials(file_name, new_file_name):
    print("Function 'factorials' starts: ")
    factorials_list = []
    with open(file_name, "rb") as file:
        read_data = pickle.load(file)
        if len(read_data) > 0:
            for num in read_data:
                res = math.factorial(num)
                factorials_list.append(res)
            print(factorials_list)
            with open(f"{new_file_name}.pickle", "wb") as file:
                pickle.dump(factorials_list, file)
            print("Data saved.")


create_file(data)
prime_numbers("data.pickle", "new_data")
factorials("data.pickle", "new_data_2")

t1 = threading.Thread(target=create_file, args=(data, ))
t1.start()
t1.join()

if len(data) > 0:
    t2 = threading.Thread(target=prime_numbers, args=("data.pickle", "new_data", ))
    t2.start()
    t2.join()


    t3 = threading.Thread(target=factorials, args=("data.pickle", "new_data_2", ))
    t3.start()
    t3.join()
else:
    raise Exception("List is empty")
