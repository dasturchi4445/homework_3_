class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert(prev_node, new_data):
    # listning ixtiyoriy nuqtasiga element qo'shish
    if prev_node is None:
        print("Error")
        # yangi element qo'shamiz
        new_node = Node(new_data)
        # yangi tugunni keyingi elementga bog'laymiz
        new_node.next = prev_node
        # avvalgi tugunni yangi elementga bog'laymiz
        prev_node.next = new_node


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        # listning boshiga element qo'shish
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def check(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            if last.next == new_node:
                return last.next
            last = last.next


l_list = LinkedList()

data = []
for i in range(1, 20):
    data.append(i)

l_list.head = Node(data[0])
for j in data[1:]:
    l_list.append(j)

# l_list.insert(l_list.check(13), 77)
# print(l_list.printList())

l_list = LinkedList()
a = Node(11)
b = Node(44)
c = Node(55)
d = Node(77)

l_list.head = a

a.next = b
b.next = c
c.next = d

# print(f"previous state: {l_list.printList}()")

l_list.push(88), l_list.push(99), l_list.push(66), l_list.push(33), l_list.push(22)

# print(f"the next case: {l_list.printList}()")

l_list.append(111), l_list.append(222), l_list.append(333), l_list.append(444), l_list.append(555)

# print(f"added new information: {l_list.printList()}")

insert(11, 666), insert(55, 777)
insert(77, 888), insert(333, 999)

# print(l_list.printList())

"""
List (Tuzilish):
Oddiy ro'yxat Pythonda massiv (array) kabi tuziladi. Elementlar ketma-ket joylashgan, ya'ni xotirada bir-biriga
yaqin bo'ladi. O'lchami oldindan belgilangan va kerak bo'ladigan dinamik ravishda kengaytiriladi.

LinkedList (Tuzilish):
Bog'langan ro'yxatda har bir element (tugun) o'z qiymat va keyingi elementga ko'rsatkich (pointer) saqlaydi.
Tugunlar xotirada tarqoq joylashishi mumkin, faqat ko'rsatkichlar orqali bog'langan bo'ladi.

"""

"""
List (Kiritish va o'chirish):
Elementni kiritish yoki o'chirish uchun ko'p hollarda indekslar yangilanishi kerak bo'ladi. Boshlang'ich
yoki o'rtadan element kiritish/o'chirish O(n) vaqt talab qiladi, chunki elementlarni siljitish kerak bo'ladi. 

LinkedList (Kiritish va o'chirish):
Boshlang'ich yoki o'rtadan element kiritish/o'chirish O(1) vaqt talab qiladi, faqat ko'rsatkichlarni yangilash kifoya.
Biroq elementni topish uchun O(n) vaqt talab qilishi mumkin, chunki barcha elementlarni ketma-ket ko'rib chiqishi kerak.

"""

"""
List (Indeks bo'yicha kirish): 
Elementga indeks bo'yicha kirish O(1) vaqt talab qiladi, chunki indeks xotira manzilini ko'rsatadi.

LinkedList (Indeks bo'yicha kirish):
Elementga indeks bo'yicha kirish O(n) vaqt talab qiladi, chunki ketma-ket elementlarni ko'rib chiqishi kerak.

"""

"""
List (Xotira samaradorligi):
Oddiy ro'yxatlar xotiradan samarali foydalanadi, chunki ular ketma-ket joylashgan.

LinkedList (Xotira samaradarligi):
Bog'langan ro'yxatlar qo'shimcha xotira talab qiladi, chunki xar bir tugun ko'rsatkichni ham sqlaydi.  

"""

"""
List (Foydalanish xolatlari):
Kichik va o'rta hajimdagi ro'yxatlar uchun yaxshi tanlov, ayniqsa indeks bo'yicha kirish tezligi muhim bo'lsa.
Elementlarni tez-tez kiritish va o'chirish kerak bo'lmasa.

LinkedList (Foydalanish xolatlari):
Katta hajimdagi ro'yxatlar va elementlarni tez-tez kiritish va o'chirish kerak bo'lgan holatlar uchun yaxshi tanlov.
Indeks bo'yicha kirish tezligi muhim bo'lmagan hollarda. 

"""

"""
=> Xulosa:
Oddiy ro'yxatlar (Lists) tez-tez foydalanish uchun qulayroq va samaradorliroq bo'lishi mumkin.
Bog'langan ro'yxatlar (Linked lists) esa muayyan holatlarda (masalan, kiritish/o'chirish tezligi muhim bo'lmagan
hollarda) afzal bo'lishi mumkin.
 
"""