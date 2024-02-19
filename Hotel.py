import json


class Hotel:
    def __init__(self, hotel_name, stars, num_rooms):
        self.hotel_name = hotel_name
        self.stars = stars
        self.num_rooms = num_rooms

    def modify_hotel_information(self, new_stars, new_num_rooms):
        # Read hotel data from file
        with open('hotels.json', 'r') as file:
            hotels = json.load(file)

        # Modify hotel information
        for hotel in hotels:
            if hotel['hotel_name'] == self.hotel_name:
                hotel['stars'] = new_stars
                hotel['num_rooms'] = new_num_rooms
                break

        # Write updated hotel data to file
        with open('hotels.json', 'w') as file:
            json.dump(hotels, file, indent=4)

    def reserve_room(self, room_num, res_days):
        # Implement room reservation logic here
        pass

    def cancel_reservation(self, room_num):
        # Read reservation data from file
        with open('reservations.json', 'r') as file:
            reservations = json.load(file)

        # Remove reservation by room number
        reservations = [reservation for reservation in reservations
                        if reservation['room_num'] != room_num]

        # Write updated reservation data to file
        with open('reservations.json', 'w') as file:
            json.dump(reservations, file, indent=4)
