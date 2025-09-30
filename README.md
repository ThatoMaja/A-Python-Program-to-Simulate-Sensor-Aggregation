Multi-threaded Sensor Aggregation System

A Python application simulating a distributed sensor data aggregation platform. This project focuses on implementing concurrency and ensuring thread safety to efficiently handle and process sensor readings from multiple sources across several aggregator nodes.

---

## Project Goal

To design and implement a concurrent system that distributes sensor readings, manages the processing capacity of aggregators, and prevents data corruption using threading mechanisms.

---

## Key Features Implemented

* **Concurrent Reading Collection:** Uses Python's `threading` module to simulate the collection of sensor readings concurrently.
* **Capacity-Aware Distribution:** Distributes readings among multiple aggregators, each with a defined processing capacity limit.
* **Thread Safety with Locks:** Implements `threading.Lock` to protect shared data structures (like task queues and aggregator state) and prevent race conditions.
* **Safe Reassignment:** Logic to safely reassign sensor readings to other available aggregators if an aggregator reaches its capacity.

---

## Concepts Demonstrated

1.  **Threading:** Utilizing `threading` to achieve concurrent execution and task handling.
2.  **Concurrency Control:** Implementing locks (`threading.Lock`) for mutual exclusion on shared resources.
3.  **Load Balancing:** Strategies for distributing tasks (readings) among workers (aggregators) based on their capacity.
4.  **Optimisation:** Discussion on techniques like task batching, thread pooling and load balancing strategies for handling large scales.

---

## How to Run

1.  Ensure you have Python installed.
2.  Execute the main program file (e.g., `sensor_aggregator.py`).
    ```bash
    python sensor_aggregator.py
    ```
3.  [cite_start]The simulation will run with **50 sensor readings** and **5 aggregators** as required by the simulation scenario[cite: 81].
