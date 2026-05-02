class HotelRoom:
    def __init__(self, room_number: int, room_type: str, price_per_night: float):
        self.r_n = room_number
        self.r_t = room_type
        self.p_p_n = price_per_night
        self.is_available = True

    def book(self):
        if self.is_available:
            self.is_available = False
            print("Xona band qilindi.")

    def checkout(self):
        if not(self.is_available):
            self.is_available = True
            print("Xona bo'shatildi")

    def get_info(self):
        print(f"Xona {self.r_n} | Turi: {self.r_t} | Narx: {self.p_p_n} so'm | Holat: {self.is_available}")



xona = HotelRoom(room_number=101, room_type="Deluxe", price_per_night=250000)
xona.book()
xona.get_info()
xona.checkout()