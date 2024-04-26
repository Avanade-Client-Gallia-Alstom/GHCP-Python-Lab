#Select cancel_reservation() method from the following class.Initiate GHCP and run the /tests command.

class TrainReservationSystem:
    def __init__(self):
        self.reservations = []

    def make_reservation(self, passenger_name, seat_number):
        reservation = {'passenger_name': passenger_name, 'seat_number': seat_number}
        self.reservations.append(reservation)

    def cancel_reservation(self, passenger_name):
        for reservation in self.reservations:
            if reservation['passenger_name'] == passenger_name:
                self.reservations.remove(reservation)
                break

    def get_reservation(self, passenger_name):
        for reservation in self.reservations:
            if reservation['passenger_name'] == passenger_name:
                return reservation

        return None


