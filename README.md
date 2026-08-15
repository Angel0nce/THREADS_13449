# NovaTech Concurrent Order Processing Simulation

This project simulates a concurrent order processing system for NovaTech. It uses Python's `threading` and `queue` modules to process multiple customer orders simultaneously while ensuring data consistency across shared resources like inventory and statistics.

## Project Structure

The project is organized into modular components:

- **`main.py`**: The entry point of the application. It initializes the shared resources (inventory, statistics, order queue), spawns the worker and monitor threads, and waits for them to complete before printing a final summary.
- **`core/`**: Contains the core logic and thread management classes.
  - `inventory_manager.py`: Handles thread-safe inventory operations, ensuring no race conditions occur when multiple workers attempt to process items from the stock.
  - `stats.py`: Manages a thread-safe `StatsManager` to keep track of approved, rejected, and failed orders.
  - `worker.py`: Defines the `OrderWorker` thread class, which consumes orders from the shared queue, processes them through the inventory manager, and updates statistics.
  - `monitor.py`: Defines the `SystemMonitor` thread class, which periodically outputs the current state of the simulation (pending orders, active workers, current stats).
- **`data/`**: Contains the mock data used to run the simulation.
  - `inventory.py`: Defines the initial product stock.
  - `orders_data.py`: Defines the list of test cases (orders) to be processed, covering normal scenarios, high contention, out-of-stock, and malformed orders.

## How It Works

1. **Initialization**: The main script loads the initial inventory and populates a thread-safe FIFO queue with a predefined list of orders.
2. **Execution**: It spawns multiple `OrderWorker` threads (usually 3) and 1 `SystemMonitor` thread.
3. **Processing**: Each worker continuously fetches an order from the queue and tries to process it. Access to shared resources (like the `InventoryManager` and `StatsManager`) is protected by locks to prevent race conditions.
4. **Completion**: Once the queue is empty, the workers finish their execution. The monitor thread is then safely stopped, and the main thread prints a comprehensive summary of the simulation results, validating that all invariants (e.g., no negative stock) held true.

## Running the Simulation

Ensure you have Python 3 installed. You can run the simulation from the command line:

```bash
python main.py
```
