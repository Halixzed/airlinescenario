-- Insert dummy passengers
INSERT INTO passenger (surname, name) VALUES ('Doe', 'John');
INSERT INTO passenger (surname, name) VALUES ('Smith', 'Jane');

-- Insert dummy passenger contacts
INSERT INTO passenger_contact (passenger_id, address, phone) VALUES (1, '123 Elm St', '555-1234');
INSERT INTO passenger_contact (passenger_id, address, phone) VALUES (2, '456 Maple Ave', '555-5678');

-- Insert dummy airplanes
INSERT INTO airplane (numser, manufacturer, model) VALUES (1, 'Boeing', '737');
INSERT INTO airplane (numser, manufacturer, model) VALUES (2, 'Airbus', 'A320');

-- Insert dummy cities
INSERT INTO city (city_name) VALUES ('New York');
INSERT INTO city (city_name) VALUES ('London');

-- Insert dummy flights
INSERT INTO flight (flight_num, origin, destination, flight_date, dep_time, arr_time, airplane_id) VALUES ('AB123', 'New York', 'London', '2024-05-20', '10:00:00', '20:00:00', 1);
INSERT INTO flight (flight_num, origin, destination, flight_date, dep_time, arr_time, airplane_id) VALUES ('CD456', 'London', 'New York', '2024-05-21', '11:00:00', '21:00:00', 2);

-- Insert dummy bookings
INSERT INTO booking (passenger_id, flight_id) VALUES (1, 1);
INSERT INTO booking (passenger_id, flight_id) VALUES (2, 2);

-- Insert dummy staff
INSERT INTO staff (empnum, surname, name, address, phone, salary) VALUES (1, 'Adams', 'Alice', '789 Birch St', '555-9012', 60000);
INSERT INTO staff (empnum, surname, name, address, phone, salary) VALUES (2, 'Brown', 'Bob', '101 Pine St', '555-3456', 65000);

-- Insert dummy pilots
INSERT INTO pilot (pilot_id, empnum, type_rating) VALUES (1, 1, '737');
INSERT INTO pilot (pilot_id, empnum, type_rating) VALUES (2, 2, 'A320');

-- Insert dummy crew assignments
INSERT INTO crew_assignment (flight_id, empnum) VALUES (1, 1);
INSERT INTO crew_assignment (flight_id, empnum) VALUES (2, 2);

-- Insert dummy pilot assignments
INSERT INTO pilot_assignment (flight_id, pilot_id) VALUES (1, 1);
INSERT INTO pilot_assignment (flight_id, pilot_id) VALUES (2, 2);
