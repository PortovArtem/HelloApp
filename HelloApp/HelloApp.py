print("Hello Python from Visual Studio!")

summ = 0

for i in range(10):
    summ += i

print(summ)

def check_set(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    if set1 == set2:
        return True
    else:
        return False

list1 = list(input('������� ������ ������\n'))
list2 = list(input('������� ������ ������\n'))

result = check_set(list1, list2)

if result == True:
    print('��������� ��������� ������ ������� ���������')
else:
    print('��������� ��������� ������ ������� �� ���������')

