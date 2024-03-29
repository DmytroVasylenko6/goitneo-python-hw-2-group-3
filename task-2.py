from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        if not len(name) >= 1:
            raise ValueError("Name should be at least 1 character long")
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        if not (len(phone) == 10 and phone.isdigit()):
            raise ValueError("Phone should be 10 digits long")
        super().__init__(phone)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        idx_num = self.phones.index(Phone(phone_number))
        self.phones.pop(idx_num)
        return self.phones

    def edit_phone(self, edit_number, new_number):
        for p in self.phones:
            if p.value == edit_number:
                idx_num = self.phones.index(p)

                self.phones[idx_num] = Phone(new_number)

        return self.phones

    def find_phone(self, searh_number):
        find_phone = ""
        for phone in self.phones:
            if str(phone) == str(searh_number):
                find_phone = str(phone)

        if find_phone:
            return find_phone
        else:
            return f"Search phone {searh_number} does not exist in AddressBook"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        del self.data[name]

    def find(self, name):
        for key, record in self.data.items():
            if key == name:
                return record


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)
# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
# Видалення запису Jane
book.delete("Jane")
