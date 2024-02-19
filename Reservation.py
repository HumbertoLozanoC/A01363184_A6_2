import json


class Reservation:
    def __init__(self, room_num, res_days):
        self.room_num = room_num
        self.res_days = res_days

    def create_reservation(self, customer, hotel):
        # Read reservation data from file
        with open('reservations.json', 'r') as file:
            reservations = json.load(file)

        # Add new reservation
        reservations.append({
            'customer': customer.usr_name,
            'hotel': hotel.hotel_name,
            'room_num': self.room_num,
            'res_days': self.res_days
        })

        # Write updated reservation data to file
        with open('reservations.json', 'w') as file:
            json.dump(reservations, file, indent=4)

    def cancel_reservation(self, customer_name, room_num):
        # Read reservation data from file
        with open('reservations.json', 'r') as file:
            reservations = json.load(file)

        # Remove reservation by customer name and room number
        reservations = [reservation for reservation in reservations
                        if reservation['customer'] != customer_name
                        or reservation['room_num'] != room_num]

        # Write updated reservation data to file
        with open('reservations.json', 'w') as file:
            json.dump(reservations, file, indent=4)
