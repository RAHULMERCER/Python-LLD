import threading
import time

class AirTrafficController:
    _instance = None  # Stores the single instance
    _lock = threading.Lock()  # Ensures thread safety

    def __new__(cls):
        with cls._lock:  # handle race conditions
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.landing_queue = []  # landing queue for incoming flights
                cls._instance.departure_queue = []  # Take off queue for outgoing flights
        return cls._instance

    def request_landing(self, flight_id):
        self.landing_queue.append(flight_id)
        print(f"Flight {flight_id} requested landing.")

    def request_takeoff(self, flight_id):
        self.departure_queue.append(flight_id)
        print(f"Flight {flight_id} requested takeoff.")

    def authorize_landing(self):
        if self.landing_queue:
            flight_id = self.landing_queue.pop(0)
            print(f"Flight {flight_id} is cleared for landing.")
        else:
            print("No flights waiting to land.")

    def authorize_takeoff(self):
        if self.departure_queue:
            flight_id = self.departure_queue.pop(0)
            print(f"Flight {flight_id} is cleared for takeoff.")
        else:
            print("No flights waiting for takeoff.")

atc1 = AirTrafficController()
atc2 = AirTrafficController()

# Ensure both instances are the same
print(atc1 is atc2)  # True

# Simulating flights requesting landing and takeoff
atc1.request_landing("AI101")
atc2.request_landing("BA202")
atc1.request_takeoff("LH303")

# Authorizing landings and takeoffs
time.sleep(1)
atc2.authorize_landing()
time.sleep(1)
atc1.authorize_landing()
time.sleep(1)
atc2.authorize_takeoff()
