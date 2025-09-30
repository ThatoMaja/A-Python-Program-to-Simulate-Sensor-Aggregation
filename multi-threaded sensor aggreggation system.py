import threading
import time
import random

class Aggregator:
    def __init__(self, agg_id):
        self.agg_id = agg_id

    def process_reading(self, reading_id, processing_time):
        print(f"Aggregator {self.agg_id} assigned Reading {reading_id}")
        time.sleep(processing_time)
        print(f"Aggregator {self.agg_id} completed Reading {reading_id}")


def sensor_simulation(num_sensors, aggregators):
    threads = []
    for i in range(1, num_sensors + 1):
        agg = random.choice(aggregators)
        processing_time = random.uniform(0.2, 1.0)
        t = threading.Thread(target=agg.process_reading, args=(i, processing_time))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    aggregators = [Aggregator(i) for i in range(1, 6)]
    print("Starting sensor aggregation simulation...\n")
    sensor_simulation(10, aggregators)
    print("\nAll readings processed.")