class Flight:
    def __init__(self, flight_number: str, destination: str, capacity: int):
        self.f_n = flight_number
        self.d = destination
        self.c = capacity
        self.passengers = []

    def add_passenger(self, name: str, seat: str):
        tpl = (name, seat)
        self.passengers.append(tpl)
        print(self.passengers)
    
    def remove_passenger(self, name: str):
        self.passengers = [p for p in self.passengers if p[0] != name]
        print(self.passengers)

    def get_passenger_count(self):
        print(len(self.passengers))

    def __str__(self):
        return f"\n{self.f_n}\n{self.d}\n{self.c}\n{self.passengers}"



reys = Flight(flight_number="HY123", destination="London", capacity=150)

reys.add_passenger("Ali Karimov", "12A")
reys.add_passenger("Vali Usmonov", "12B")

reys.get_passenger_count()

reys.remove_passenger("Vali Usmonov")
print(reys)