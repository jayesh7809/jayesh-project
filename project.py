class CylinderBookingSystem:
    def __init__(self):
        self.cylinders_available = {'oxygen': 100, 'propane': 50, 'acetylene': 30}
        self.booked_cylinders = {'oxygen': 0, 'propane': 0, 'acetylene': 0}

    def display_menu(self):
        print("1. Check Cylinder Availability")
        print("2. Book Cylinder")
        print("3. View Booked Cylinders")
        print("4. Exit")

    def check_availability(self, gas_type):
        return self.cylinders_available.get(gas_type, 0)

    def book_cylinder(self, gas_type, quantity):
        available_quantity = self.check_availability(gas_type)
        if quantity > available_quantity:
            print(f"Sorry, only {available_quantity} cylinders of {gas_type} are available.")
        else:
            self.cylinders_available[gas_type] -= quantity
            self.booked_cylinders[gas_type] += quantity
            print(f"{quantity} cylinders of {gas_type} booked successfully.")

    def view_booked_cylinders(self):
        print("Booked Cylinders:")
        for gas_type, quantity in self.booked_cylinders.items():
            print(f"{gas_type}: {quantity}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                gas_type = input("Enter the type of gas (oxygen/propane/acetylene): ")
                available_quantity = self.check_availability(gas_type)
                print(f"Available {gas_type} cylinders: {available_quantity}")
            elif choice == '2':
                gas_type = input("Enter the type of gas to book (oxygen/propane/acetylene): ")
                quantity = int(input("Enter the quantity to book: "))
                self.book_cylinder(gas_type, quantity)
            elif choice == '3':
                self.view_booked_cylinders()
            elif choice == '4':
                print("Exiting the program. Thank you!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    booking_system = CylinderBookingSystem()
    booking_system.run()
