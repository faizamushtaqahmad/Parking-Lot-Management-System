import matplotlib.pyplot as plt
from tabulate import tabulate

class ParkingSlot:
    def __init__(self, slot_id):
        self.slot_id = slot_id
        self.is_free = True
        self.vehicle_number = None
        self.arrival_time = None
        
class ParkingLot:
    def __init__(self, total_slots, rate_per_hour=10):
        self.slots = [ParkingSlot(i + 1) for i in range(total_slots)]
        self.waiting_queue = []
        self.rate_per_hour = rate_per_hour
        self.vehicle_records = []  

    def park_vehicle(self, vehicle_number, arrival_time):
        for slot in self.slots:
            if slot.is_free:
                slot.is_free = False
                slot.vehicle_number = vehicle_number
                slot.arrival_time = arrival_time
                print(f"Vehicle {vehicle_number} parked at Slot {slot.slot_id} at Time {arrival_time}.")
                return
        self.waiting_queue.append((vehicle_number, arrival_time))
        print(f"Parking full! Vehicle {vehicle_number} added to waiting queue at Time {arrival_time}.")

    def remove_vehicle(self, vehicle_number, departure_time):
        found = False
        for slot in self.slots:
            if slot.vehicle_number == vehicle_number:
                found = True
                arrival_time = slot.arrival_time
                parking_duration = departure_time - arrival_time
                if parking_duration <= 0:
                    parking_duration = 1
                bill = parking_duration * self.rate_per_hour

                print(f"\nVehicle {vehicle_number} removed from Slot {slot.slot_id} at Time {departure_time}.")
                print(f"Duration Parked: {parking_duration} hour(s)")
                print(f"Bill: Rs{bill}\n")

                self.vehicle_records.append({
                    "vehicle": vehicle_number,
                    "arrival": arrival_time,
                    "departure": departure_time,
                    "waiting": 0 if arrival_time == slot.arrival_time else arrival_time - slot.arrival_time
                })

                slot.is_free = True
                slot.vehicle_number = None
                slot.arrival_time = None

                if self.waiting_queue:
                    next_vehicle, wait_start = self.waiting_queue.pop(0)
                    wait_time = departure_time - wait_start
                    print(f"Now parking waiting vehicle {next_vehicle} at freed Slot {slot.slot_id}.")
                    slot.is_free = False
                    slot.vehicle_number = next_vehicle
                    slot.arrival_time = departure_time

                    self.vehicle_records.append({
                        "vehicle": next_vehicle,
                        "arrival": wait_start,
                        "departure": None,
                        "waiting": wait_time
                    })

                break

        if not found:
            print(f"Vehicle {vehicle_number} not found in the parking lot.")

    def update_departure(self, vehicle_number, departure_time):
        for record in self.vehicle_records:
            if record["vehicle"] == vehicle_number and record["departure"] is None:
                record["departure"] = departure_time
                break

    def display_status(self):
        print("\nCurrent Parking Lot Status:")
        print("-" * 50)
        print("Slot ID |   Status   | Vehicle Number")
        print("-" * 50)
        for slot in self.slots:
            status = "Free" if slot.is_free else "Occupied"
            vehicle = slot.vehicle_number if slot.vehicle_number else "-"
            print(f"{slot.slot_id:^7} | {status:^10} | {vehicle:^15}")
        print("-" * 50)
        if self.waiting_queue:
            print("\nWaiting Queue:")
            for vehicle, time in self.waiting_queue:
                print(f"Vehicle {vehicle} (waiting since Time {time})")
        else:
            print("\nNo vehicles in waiting queue.\n")

    def calculate_averages(self):
        completed = [v for v in self.vehicle_records if v["departure"] is not None]
        if not completed:
            print("No completed vehicle records yet.")
            return
        total_waiting = sum(v["waiting"] for v in completed)
        total_turnaround = sum(v["departure"] - v["arrival"] for v in completed)
        n = len(completed)
        avg_waiting = total_waiting / n
        avg_turnaround = total_turnaround / n
        print(f"\nAverage Waiting Time: {avg_waiting:.2f} hours")
        print(f"Average Turnaround Time: {avg_turnaround:.2f} hours\n")

    def generate_gantt_and_table(self):
        completed = [v for v in self.vehicle_records if v["departure"] is not None]
        if not completed:
            print("No completed vehicle records to display.")
            return

        print("\nVehicle Parking Details Table:\n")
        table_data = []
        fig, ax = plt.subplots(figsize=(12, 6))
        yticks = []
        ylabels = []

        for i, v in enumerate(completed):
            vehicle = v["vehicle"]
            arrival = v["arrival"]
            departure = v["departure"]
            waiting = v["waiting"]
            turnaround = departure - arrival

            table_data.append([
                vehicle,
                arrival,
                departure,
                waiting,
                turnaround
            ])

            ax.barh(i, waiting, left=arrival, color='red', edgecolor='black', label='Waiting' if i == 0 else "")
            ax.barh(i, turnaround - waiting, left=arrival + waiting, color='green', edgecolor='black', label='Parked' if i == 0 else "")

            yticks.append(i)
            ylabels.append(vehicle)

        print(tabulate(table_data, headers=["Vehicle", "Arrival", "Departure", "Waiting", "Turnaround"], tablefmt="grid"))

        ax.set_yticks(yticks)
        ax.set_yticklabels(ylabels)
        ax.set_xlabel("Time (in hours)")
        ax.set_title("Gantt Chart of Vehicle Parking (FCFS)")
        ax.legend()
        plt.tight_layout()
        plt.show()

# Main program
def main():
    total_slots = int(input("Enter total number of parking slots: "))
    rate = int(input("Enter parking rate per hour (Rs): "))
    parking_lot = ParkingLot(total_slots, rate)

    while True:
        print("\n--- Parking Lot Menu ---")
        print("1. Park a Vehicle")
        print("2. Remove a Vehicle")
        print("3. Display Parking Lot Status")
        print("4. Show Average Waiting & Turnaround Time")
        print("5. Show Gantt Chart and Summary Table")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            vehicle_number = input("Enter vehicle number: ")
            arrival_time = int(input("Enter arrival time (in hours): "))
            parking_lot.park_vehicle(vehicle_number, arrival_time)

        elif choice == '2':
            vehicle_number = input("Enter vehicle number to remove: ")
            departure_time = int(input("Enter departure time (in hours): "))
            parking_lot.remove_vehicle(vehicle_number, departure_time)
            parking_lot.update_departure(vehicle_number, departure_time)

        elif choice == '3':
            parking_lot.display_status()

        elif choice == '4':
            parking_lot.calculate_averages()

        elif choice == '5':
            parking_lot.generate_gantt_and_table()

        elif choice == '6':
            print("Exiting Parking Lot System. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()

