import threading
import time
import random

# 1.1, 1.2,  1.3 Combined
class Aggregator:       
    #An aggregator that processes sensor readings with a max concurrency limit.
    def __init__(self, agg_id, capacity):
        self.agg_id = agg_id
        self.capacity = capacity
        self.active_tasks = 0
        self.lock = threading.Lock() # Lock for thread safety 

    def process_reading(self, reading_id, processing_time):
        # Try to assign the task. If capacity is full, return False.
        with self.lock:
            if self.active_tasks >= self.capacity:
                return False # Could not assign (1.3)
            self.active_tasks += 1
            print(f"Aggregator {self.agg_id} assigned Reading {reading_id}")

       
        time.sleep(processing_time) #Simulate's the actual processing work

        # Mark task as complete
        with self.lock:
            print(f"Aggregator {self.agg_id} completed Reading {reading_id}")
            self.active_tasks -= 1
        return True # Successfully assigned and processed

def sensor_simulation(num_readings, aggregators):
    readings = list(range(1, num_readings + 1)) # Simulate random arrival of readings
    random.shuffle(readings) # Shuffle readings to simulate random arrival

    for reading_id in readings:
        processing_time = random.uniform(0.2, 1.0)
        assigned = False

        # Keep trying to assign the reading until successful
        while not assigned:
            agg = random.choice(aggregators) # Choose a random aggregator
            assigned = agg.process_reading(reading_id, processing_time) # Try to process the reading on the chosen aggregator
            # If the aggregator was at capacity (returns False), the loop will continue and try another one

if __name__ == "__main__":
    aggregators = [Aggregator(i, capacity=2) for i in range(1, 6)]   # Create 5 aggregators with a capacity of 2 each 
    print("Starting sensor aggregation simulation...")
    sensor_simulation(50, aggregators)
    print("All readings processed.")