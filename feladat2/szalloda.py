import datetime

# Hozz létre egy Szalloda osztályt, ami ezekből a Szobákból áll, és van saját attributuma is (név pl.)
class Szalloda():
    def __init__(self, nev, szobak):
        self.nev = nev
        self.szobak = szobak


# Hozz létre egy Foglalás osztályt, amelybe a Szálloda szobáinak foglalását tároljuk (elég itt, ha egy foglalás csak egy napra szól)
class Foglalas(Szalloda):
    def __init__(self, nev, szobak):
        super().__init__(nev, szobak)
        self.foglalasok = {key: value for key, value in []}

    # Implementálj egy metódust, ami lehetővé teszi szobák foglalását dátum alapján, visszaadja annak árát.
    # A foglalás létrehozásakor ellenőrizd, hogy a dátum érvényes (jövőbeni) és a szoba elérhető-e akkor.
    # Books a room and returns the price and an empty string, on error returns a non-empty string
    def book_room(self, room_nr, date):
        # A foglalás létrehozásakor ellenőrizd, hogy a dátum érvényes (jövőbeni)
        if date <= datetime.datetime.now().strftime("%Y%m%d"):
            return 0, "Invalid date"
        # a szoba elérhető-e akkor
        if room_nr in self.foglalasok:
            # a szoba elérhető-e akkor
            if self.__is_date_booked(date, room_nr):
                return 0, "Room is already booked."
            else:
                booked_date = self.foglalasok[room_nr]
                booked_date.append(date)
        else:
            self.foglalasok[room_nr] = [date]
        booked_interval = 1
        price = self.__get_room_price(room_nr, booked_interval)
        if price < 0:
            return 0, "Unknown price"
        return price, ""


    def __is_date_booked(self, date, room_nr):
        for booked_date in self.foglalasok[room_nr]:
            if booked_date == date:
                return True
        return False

    def __get_room_price(self, room_nr, booked_interval):
        for room in self.szobak:
            if room.szobaszam == room_nr:
                return room.ar * booked_interval
        return -1

    # Implementálj egy metódust, ami lehetővé teszi a foglalás lemondását.
    # Biztosítsd, hogy a lemondások csak létező foglalásokra lehetségesek.
    # Deletes booking, returns non-empty string on error
    def delete_booking(self, room_nr, date):
        err_msg = "Room not booked"
        if room_nr not in self.foglalasok:
            return err_msg
        if not self.__is_date_booked(date, room_nr):
            return err_msg
        booked_date = self.foglalasok[room_nr]
        booked_date.remove(date)
        return ""

    # Implementálj egy metódust, ami listázza az összes foglalást.
    def get_bookings(self):
        return self.foglalasok

    # Implementálj egy metódust, ami listázza az összes foglalást.
    # Csak a szobak?
    def get_booked_rooms(self):
        booked_rooms = []
        for room_nr in self.foglalasok:
            booked_rooms.append(room_nr)
        return booked_rooms
