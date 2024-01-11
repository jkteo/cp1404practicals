from prac_09.silver_service_taxi import SilverServiceTaxi

premium_taxi = SilverServiceTaxi("Premium Taxi", 100, 10)
premium_taxi.start_fare()
premium_taxi.drive(20)
print(premium_taxi.get_fare())
