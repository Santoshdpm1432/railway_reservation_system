
trains = {
    "12345": {"name": "Express 12345", "seats": 50, "reserved_seats": []},
    "67890": {"name": "Superfast 67890", "seats": 100, "reserved_seats": []},
    "67891": {"name": "santosh express", "seats": 150, "reserved_seats": []},
    "518501": {"name": "ashoka express", "seats": 160, "reserved_seats": []},
    "518502": {"name": "nagaprasad 12345", "seats": 170, "reserved_seats": []},
    "518503": {"name": "raju express", "seats": 180, "reserved_seats": []},
}

def display_trains():
    print("Available Trains:")
    for train_id, details in trains.items():
        print(f"Train ID: {train_id}, Name: {details['name']}, Available Seats: {details['seats'] - len(details['reserved_seats'])}")

def reserve_seat(train_id, passenger_name):
    if train_id in trains:
        train = trains[train_id]
        if len(train["reserved_seats"]) < train["seats"]:
            train["reserved_seats"].append(passenger_name)
            print(f"Seat reserved for {passenger_name} on {train['name']}.")
        else:
            print("Sorry, no seats available on this train.")
    else:
        print("Invalid Train ID.")

def cancel_reservation(train_id, passenger_name):
    if train_id in trains:
        train = trains[train_id]
        if passenger_name in train["reserved_seats"]:
            train["reserved_seats"].remove(passenger_name)
            print(f"Reservation canceled for {passenger_name} on {train['name']}.")
        else:
            print(f"No reservation found for {passenger_name} on {train['name']}.")
    else:
        print("Invalid Train ID.")

def show_reserved_seats(train_id):
    if train_id in trains:
        train = trains[train_id]
        print(f"Reserved seats for {train['name']}: {', '.join(train['reserved_seats']) or 'None'}")
    else:
        print("Invalid Train ID.")

def main():
    while True:
        print("\nRailway Ticket Reservation System")
        print("1. Display Available Trains")
        print("2. Reserve a Seat")
        print("3. Cancel Reservation")
        print("4. Show Reserved Seats")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_trains()
        elif choice == "2":
            train_id = input("Enter Train ID: ")
            passenger_name = input("Enter Passenger Name: ")
            reserve_seat(train_id, passenger_name)
        elif choice == "3":
            train_id = input("Enter Train ID: ")
            passenger_name = input("Enter Passenger Name: ")
            cancel_reservation(train_id, passenger_name)
        elif choice == "4":
            train_id = input("Enter Train ID: ")
            show_reserved_seats(train_id)
        elif choice == "5":
            print("Thank you for using the Railway Ticket Reservation System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()