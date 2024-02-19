import unittest
import json
from HotelManager import Hotel, Customer, Reservation


class TestHotel(unittest.TestCase):
    def setUp(self):
        # Initialize test data
        self.hotel = Hotel("Hotel ABC", 4, 100)

    def test_modify_hotel_information(self):
        # Modify hotel information
        self.hotel.modify_hotel_information(5, 120)

        # Read updated hotel data from file
        with open('hotels.json', 'r') as file:
            hotels = json.load(file)

        # Verify that hotel information has been modified
        for hotel in hotels:
            if hotel['hotel_name'] == self.hotel.hotel_name:
                self.assertEqual(hotel['stars'], 5)
                self.assertEqual(hotel['num_rooms'], 120)
                break

    # Write similar tests for other Hotel methods


class TestCustomer(unittest.TestCase):
    def setUp(self):
        # Initialize test data
        self.customer = Customer("user123", "VIP")

    def test_create_customer(self):
        # Create new customer
        self.customer.create_customer()

        # Read customer data from file
        with open('customers.json', 'r') as file:
            customers = json.load(file)

        # Verify that customer has been created
        self.assertTrue(any(customer['usr_name'] == self.customer.usr_name
                            for customer in customers))

    # Write similar tests for other Customer methods


class TestReservation(unittest.TestCase):
    def setUp(self):
        # Initialize test data
        self.reservation = Reservation(101, ["2022-01-01", "2022-01-02"])

    def test_create_reservation(self):
        # Create new reservation
        customer = Customer("user456", "Regular")
        hotel = Hotel("Hotel XYZ", 3, 80)
        self.reservation.create_reservation(customer, hotel)

        # Read reservation data from file
        with open('reservations.json', 'r') as file:
            reservations = json.load(file)

        # Verify that reservation has been created
        self.assertTrue(any(reservation['room_num'] == self.reservation.room_num for reservation in reservations))

    # Write similar tests for other Reservation methods


if __name__ == '__main__':
    unittest.main()
