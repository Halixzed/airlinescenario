from backend import db
from backend.models import Passenger, PassengerContact, Flight, Booking, Staff, Pilot, Airplane, City, FlightIntermediateCity, CrewAssignment, PilotAssignment

class AirlineFacade:
    def get_all_passengers(self):
        passengers = Passenger.query.all()
        return [passenger.to_dict() for passenger in passengers]

    def add_passenger(self, surname, name):
        new_passenger = Passenger(surname=surname, name=name)
        db.session.add(new_passenger)
        db.session.commit()
        return new_passenger.to_dict()

    def get_all_flights(self):
        flights = Flight.query.all()
        return [flight.to_dict() for flight in flights]

    def add_flight(self, flight_num, origin, destination, flight_date, dep_time, arr_time, airplane_id):
        new_flight = Flight(
            flight_num=flight_num,
            origin=origin,
            destination=destination,
            flight_date=flight_date,
            dep_time=dep_time,
            arr_time=arr_time,
            airplane_id=airplane_id
        )
        db.session.add(new_flight)
        db.session.commit()
        return new_flight.to_dict()

    def get_all_staff(self):
        staff = Staff.query.all()
        return [person.to_dict() for person in staff]

    def add_staff(self, empnum, surname, name, address, phone, salary):
        new_staff = Staff(
            empnum=empnum,
            surname=surname,
            name=name,
            address=address,
            phone=phone,
            salary=salary
        )
        db.session.add(new_staff)
        db.session.commit()
        return new_staff.to_dict()

    def get_all_airplanes(self):
        airplanes = Airplane.query.all()
        return [airplane.to_dict() for airplane in airplanes]

    def add_airplane(self, numser, manufacturer, model):
        new_airplane = Airplane(
            numser=numser,
            manufacturer=manufacturer,
            model=model
        )
        db.session.add(new_airplane)
        db.session.commit()
        return new_airplane.to_dict()

    def get_all_cities(self):
        cities = City.query.all()
        return [city.to_dict() for city in cities]

    def add_city(self, city_name):
        new_city = City(city_name=city_name)
        db.session.add(new_city)
        db.session.commit()
        return new_city.to_dict()

    def get_all_bookings(self):
        bookings = Booking.query.all()
        return [booking.to_dict() for booking in bookings]

    def add_booking(self, passenger_id, flight_id):
        new_booking = Booking(passenger_id=passenger_id, flight_id=flight_id)
        db.session.add(new_booking)
        db.session.commit()
        return new_booking.to_dict()

    def get_all_pilots(self):
        pilots = Pilot.query.all()
        return [pilot.to_dict() for pilot in pilots]

    def add_pilot(self, empnum, type_rating):
        new_pilot = Pilot(empnum=empnum, type_rating=type_rating)
        db.session.add(new_pilot)
        db.session.commit()
        return new_pilot.to_dict()

    def add_flight_intermediate_city(self, flight_id, city_id, sequence_num):
        new_intermediate_city = FlightIntermediateCity(
            flight_id=flight_id,
            city_id=city_id,
            sequence_num=sequence_num
        )
        db.session.add(new_intermediate_city)
        db.session.commit()
        return new_intermediate_city.to_dict()

    def add_crew_assignment(self, flight_id, empnum):
        new_crew_assignment = CrewAssignment(flight_id=flight_id, empnum=empnum)
        db.session.add(new_crew_assignment)
        db.session.commit()
        return new_crew_assignment.to_dict()

    def add_pilot_assignment(self, flight_id, pilot_id):
        new_pilot_assignment = PilotAssignment(flight_id=flight_id, pilot_id=pilot_id)
        db.session.add(new_pilot_assignment)
        db.session.commit()
        return new_pilot_assignment.to_dict()
