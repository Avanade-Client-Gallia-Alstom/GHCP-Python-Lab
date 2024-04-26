def test_cancel_reservation():
    # Create an instance of the class
    airline = Airline()

    # Add some reservations
    airline.add_reservation({'passenger_name': 'John Doe', 'flight_number': 'ABC123'})
    airline.add_reservation({'passenger_name': 'Jane Smith', 'flight_number': 'DEF456'})
    airline.add_reservation({'passenger_name': 'Alice Johnson', 'flight_number': 'GHI789'})

    # Test cancelling a reservation that exists
    airline.cancel_reservation('Jane Smith')
    assert len(airline.reservations) == 2

    # Test cancelling a reservation that doesn't exist
    airline.cancel_reservation('Bob Brown')
    assert len(airline.reservations) == 2

    # Test cancelling the last reservation
    airline.cancel_reservation('Alice Johnson')
    assert len(airline.reservations) == 1

    # Test cancelling the only remaining reservation
    airline.cancel_reservation('John Doe')
    assert len(airline.reservations) == 0

# Run the test
test_cancel_reservation()