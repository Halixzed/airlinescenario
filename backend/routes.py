from flask import Blueprint, request, jsonify
from backend.facade import AirlineFacade

api_bp = Blueprint('api', __name__)
facade = AirlineFacade()

@api_bp.route('/passengers', methods=['GET'])
def get_passengers():
    passengers = facade.get_all_passengers()
    return jsonify(passengers)

@api_bp.route('/passengers', methods=['POST'])
def add_passenger():
    data = request.get_json()
    new_passenger = facade.add_passenger(data['surname'], data['name'])
    return jsonify(new_passenger), 201

@api_bp.route('/flights', methods=['GET'])
def get_flights():
    flights = facade.get_all_flights()
    return jsonify(flights)

@api_bp.route('/flights', methods=['POST'])
def add_flight():
    data = request.get_json()
    new_flight = facade.add_flight(
        flight_num=data['flight_num'],
        origin=data['origin'],
        destination=data['destination'],
        flight_date=data['flight_date'],
        dep_time=data['dep_time'],
        arr_time=data['arr_time'],
        airplane_id=data['airplane_id']
    )
    return jsonify(new_flight), 201

@api_bp.route('/staff', methods=['GET'])
def get_staff():
    staff = facade.get_all_staff()
    return jsonify(staff)

@api_bp.route('/staff', methods=['POST'])
def add_staff():
    data = request.get_json()
    new_staff = facade.add_staff(
        empnum=data['empnum'],
        surname=data['surname'],
        name=data['name'],
        address=data['address'],
        phone=data['phone'],
        salary=data['salary']
    )
    return jsonify(new_staff), 201

@api_bp.route('/airplanes', methods=['GET'])
def get_airplanes():
    airplanes = facade.get_all_airplanes()
    return jsonify(airplanes)

@api_bp.route('/airplanes', methods=['POST'])
def add_airplane():
    data = request.get_json()
    new_airplane = facade.add_airplane(
        numser=data['numser'],
        manufacturer=data['manufacturer'],
        model=data['model']
    )
    return jsonify(new_airplane), 201

@api_bp.route('/cities', methods=['GET'])
def get_cities():
    cities = facade.get_all_cities()
    return jsonify(cities)

@api_bp.route('/cities', methods=['POST'])
def add_city():
    data = request.get_json()
    new_city = facade.add_city(data['city_name'])
    return jsonify(new_city), 201

@api_bp.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = facade.get_all_bookings()
    return jsonify(bookings)

@api_bp.route('/bookings', methods=['POST'])
def add_booking():
    data = request.get_json()
    new_booking = facade.add_booking(
        passenger_id=data['passenger_id'],
        flight_id=data['flight_id']
    )
    return jsonify(new_booking), 201

@api_bp.route('/pilots', methods=['GET'])
def get_pilots():
    pilots = facade.get_all_pilots()
    return jsonify(pilots)

@api_bp.route('/pilots', methods=['POST'])
def add_pilot():
    data = request.get_json()
    new_pilot = facade.add_pilot(
        empnum=data['empnum'],
        type_rating=data['type_rating']
    )
    return jsonify(new_pilot), 201

@api_bp.route('/flight_intermediate_cities', methods=['POST'])
def add_flight_intermediate_city():
    data = request.get_json()
    new_intermediate_city = facade.add_flight_intermediate_city(
        flight_id=data['flight_id'],
        city_id=data['city_id'],
        sequence_num=data['sequence_num']
    )
    return jsonify(new_intermediate_city), 201

@api_bp.route('/crew_assignments', methods=['POST'])
def add_crew_assignment():
    data = request.get_json()
    new_crew_assignment = facade.add_crew_assignment(
        flight_id=data['flight_id'],
        empnum=data['empnum']
    )
    return jsonify(new_crew_assignment), 201

@api_bp.route('/pilot_assignments', methods=['POST'])
def add_pilot_assignment():
    data = request.get_json()
    new_pilot_assignment = facade.add_pilot_assignment(
        flight_id=data['flight_id'],
        pilot_id=data['pilot_id']
    )
    return jsonify(new_pilot_assignment), 201
