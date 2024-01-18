def allocate_seats(num_seats, passengers):
    available_seats = list(range(1, num_seats + 1))
    middle_position = num_seats // 2
    berth_count = num_seats // 3  # Assuming a standard 3-berth configuration (lower, middle, upper)

    # Sort passengers by age in descending order
    passengers.sort(key=lambda x: x['age'], reverse=True)

    for passenger in passengers:
        # Allocate lower berth to passengers aged 60 and above
        if passenger['age'] >= 60:
            if available_seats:
                allocated_seat = available_seats.pop(middle_position)
                berth_count -= 1
                print(f"Allocate Seat {allocated_seat} (Lower) to Passenger {passenger['name']}")

    # Allocate seats to family members
    for passenger in passengers:
        if passenger['age'] < 60:
            if available_seats:
                allocated_seat = available_seats.pop()
                berth_count -= 1
                print(f"Allocate Seat {allocated_seat} to Passenger {passenger['name']}")

    # Continue allocating seats until all passengers are seated or no more berths are available
    # ...

# Example Usage:
passenger_data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 62},
    {'name': 'Charlie', 'age': 30},
    # Add more passengers as needed
]

allocate_seats(6, passenger_data)
