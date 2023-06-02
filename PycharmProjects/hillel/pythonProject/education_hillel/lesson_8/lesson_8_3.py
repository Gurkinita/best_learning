class Record:
    def __init__(self, name, phone, last_name=None, date_of_birth=None):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"Name: {self.name}, Last Name: {self.last_name}, Phone: {self.phone}, DOB: {self.date_of_birth}"


class Notebook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def remove_record(self, record):
        self.records.remove(record)

    def edit_record(self, record, name, last_name, phone, date_of_birth):
        record.name = name
        record.last_name = last_name
        record.phone = phone
        record.date_of_birth = date_of_birth


class Interface:
    def __init__(self):
        self.directory = Notebook()
        self.directory.add_record(Record("Emergency Service 1", "911"))
        self.directory.add_record(Record("Emergency Service 2", "112"))
        self.directory.add_record(Record("Emergency Service 3", "999"))

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_record()
            elif choice == "2":
                self.remove_record()
            elif choice == "3":
                self.edit_record()
            elif choice == "4":
                self.display_records()
            else:
                print("Invalid choice. Please try again.")

    def print_menu(self):
        print("\n--- Phone Directory Menu ---")
        print("1. Add Record")
        print("2. Remove Record")
        print("3. Edit Record")
        print("4. Display Records")

    def add_record(self):
        name = input("Enter name: ")
        last_name = input("Enter last name (optional): ")
        phone = input("Enter phone number: ")
        date_of_birth = input("Enter date of birth (optional): ")
        record = Record(name, phone, last_name, date_of_birth)
        self.directory.add_record(record)
        print("Record added successfully.")

    def remove_record(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        matching_records = [record for record in self.directory.records if record.name == name and record.phone == phone]
        if matching_records:
            if any(record.phone in ["911", "112", "999"] for record in matching_records):
                print("Emergency service numbers cannot be removed.")
            else:
                self.directory.remove_record(matching_records[0])
                print("Record removed successfully.")
        else:
            print("No matching records found.")

    def edit_record(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        matching_records = [record for record in self.directory.records if record.name == name and record.phone == phone]
        if matching_records:
            if any(record.phone in ["911", "112", "999"] for record in matching_records):
                print("Emergency service numbers cannot be modified.")
            else:
                record = matching_records[0]
                new_name = input("Enter new name: ")
                new_last_name = input("Enter new last name (optional): ")
                new_phone = input("Enter new phone number: ")
                new_date_of_birth = input("Enter new date of birth (optional): ")
                self.directory.edit_record(record, new_name, new_last_name, new_phone, new_date_of_birth)
                print("Record edited successfully.")
        else:
            print("No matching records found.")

    def display_records(self):
        if self.directory.records:
            print("--- Records ---")
            for record in self.directory.records:
                print(record)
        else:
            print("No records found in the directory.")


def main():
    interface = Interface()
    interface.run()


if __name__ == "__main__":
    main()

