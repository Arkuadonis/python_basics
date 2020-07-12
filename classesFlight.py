class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

AirIndia = Flight(3)

people = ["arku", "sagar", "harsh", "james"]
for person in people:
    if AirIndia.add_passengers(person):
        print(f"{person} added successfully")
    else:
        print(f"OOPS!! Flight capacity full. failed to add {person}")



