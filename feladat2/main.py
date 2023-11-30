import datetime
import random

import szoba
import szalloda


# Töltsd fel az futtatás után a rendszert 1 szállodával,
# 3 szobával és 5 foglalással, mielőtt a felhasználói adatbekérés megjelenik.
def init_data():
    # init rooms
    rooms = []
    # 3 szobával
    for i in range(3):
        if (i % 2) == 0:
            smoking = ((i % 3) == 0)
            rooms.append(szoba.EgyagyasSzoba(ar=70, szobaszam=i, dohanyzo=smoking))
        else:
            balcony = ((i % 3) == 0)
            rooms.append(szoba.KetagyasSzoba(ar=100, szobaszam=i, erkely=balcony))
    # 1 szállodával
    booking = szalloda.Foglalas(nev="ReallyGood Hotel", szobak=rooms)

    # 5 foglalással
    dates = [
        datetime.datetime(2023, 12, 10).strftime("%Y%m%d"),
        datetime.datetime(2023, 12, 11).strftime("%Y%m%d"),
        datetime.datetime(2023, 12, 9).strftime("%Y%m%d"),
        datetime.datetime(2023, 12, 20).strftime("%Y%m%d"),
        datetime.datetime(2023, 12, 21).strftime("%Y%m%d"),
    ]
    for date in dates:
        booking.book_room(random.randrange(1, 4), date)
    return booking


if __name__ == '__main__':
    booking = init_data()

    while True:
        action = input("Actions: Booking, Delete, List, Esc): ")
        if action.lower()  == "booking":
            room_nr = int(input("Room number: "))
            date_input = input("Date: (yyyy-mm-dd): ")
            date = datetime.datetime.strptime(date_input, '%Y-%m-%d').strftime("%Y%m%d")
            price, errMsg = booking.book_room(room_nr, date)
            if errMsg != "":
                print(errMsg)
            else:
                print(f"Booking confirmed for room: {room_nr} for price: {price} Euro")
        elif action.lower() == "delete":
            room_nr = int(input("Room number: "))
            date_input = input("Date: (yyyy-mm-dd): ")
            date = datetime.datetime.strptime(date_input, '%Y-%m-%d').strftime("%Y%m%d")
            msg = booking.delete_booking(room_nr, date)
            if msg != "":
                print(msg)
            else:
                print(f"Booking deleted for room: {room_nr}")
        elif action.lower() == "list":
            bookings = booking.get_bookings()
            for room, dates in bookings.items():
                print(room)
                for date in dates:
                    print(date)
        elif action.lower() == "esc":
            break
        else:
            print("Invalid action")


