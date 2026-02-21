"""Simple Transportation Management Project.

A beginner-friendly Python project that demonstrates object-oriented
programming, menu-driven interaction, and basic analytics.
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Vehicle:
    vehicle_id: str
    vehicle_type: str
    capacity: int
    route: str
    active: bool = True


@dataclass
class TransportationSystem:
    vehicles: Dict[str, Vehicle] = field(default_factory=dict)

    def add_vehicle(self, vehicle_id: str, vehicle_type: str, capacity: int, route: str) -> str:
        if vehicle_id in self.vehicles:
            return f"Vehicle with ID '{vehicle_id}' already exists."
        self.vehicles[vehicle_id] = Vehicle(vehicle_id, vehicle_type, capacity, route)
        return f"Vehicle '{vehicle_id}' added successfully."

    def remove_vehicle(self, vehicle_id: str) -> str:
        if vehicle_id not in self.vehicles:
            return f"Vehicle with ID '{vehicle_id}' not found."
        del self.vehicles[vehicle_id]
        return f"Vehicle '{vehicle_id}' removed successfully."

    def update_route(self, vehicle_id: str, new_route: str) -> str:
        vehicle = self.vehicles.get(vehicle_id)
        if not vehicle:
            return f"Vehicle with ID '{vehicle_id}' not found."
        vehicle.route = new_route
        return f"Vehicle '{vehicle_id}' route updated to '{new_route}'."

    def mark_status(self, vehicle_id: str, active: bool) -> str:
        vehicle = self.vehicles.get(vehicle_id)
        if not vehicle:
            return f"Vehicle with ID '{vehicle_id}' not found."
        vehicle.active = active
        state = "active" if active else "inactive"
        return f"Vehicle '{vehicle_id}' marked as {state}."

    def list_vehicles(self) -> List[str]:
        if not self.vehicles:
            return ["No vehicles available."]

        rows = ["ID | Type | Capacity | Route | Status"]
        rows.append("-" * 45)
        for v in self.vehicles.values():
            status = "Active" if v.active else "Inactive"
            rows.append(f"{v.vehicle_id} | {v.vehicle_type} | {v.capacity} | {v.route} | {status}")
        return rows

    def total_capacity(self) -> int:
        return sum(v.capacity for v in self.vehicles.values() if v.active)


MENU = """
Transportation Management System
--------------------------------
1. Add vehicle
2. Remove vehicle
3. Update route
4. Mark vehicle active/inactive
5. List vehicles
6. Show active fleet total capacity
7. Exit
"""


def run_cli() -> None:
    system = TransportationSystem()

    while True:
        print(MENU)
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            vehicle_id = input("Vehicle ID: ").strip()
            vehicle_type = input("Vehicle type (Bus/Van/Taxi/etc.): ").strip()
            capacity = int(input("Passenger capacity: ").strip())
            route = input("Assigned route: ").strip()
            print(system.add_vehicle(vehicle_id, vehicle_type, capacity, route))

        elif choice == "2":
            vehicle_id = input("Vehicle ID to remove: ").strip()
            print(system.remove_vehicle(vehicle_id))

        elif choice == "3":
            vehicle_id = input("Vehicle ID to update: ").strip()
            new_route = input("New route: ").strip()
            print(system.update_route(vehicle_id, new_route))

        elif choice == "4":
            vehicle_id = input("Vehicle ID to update status: ").strip()
            status = input("Set status (active/inactive): ").strip().lower()
            print(system.mark_status(vehicle_id, active=(status == "active")))

        elif choice == "5":
            for line in system.list_vehicles():
                print(line)

        elif choice == "6":
            print(f"Active fleet total capacity: {system.total_capacity()} passengers")

        elif choice == "7":
            print("Exiting Transportation Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    run_cli()
