from typing import List

from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms: List[Room] = []

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        return f"Monthly consumption: {sum(room.expenses+room.room_cost for room in self.rooms):.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget >= room.expenses+room.room_cost:
                budget = room.budget
                room.budget -= room.expenses+room.room_cost
                result.append(f"{room.family_name} paid {room.expenses+room.room_cost:.2f}$ and have {budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return '\n'.join(result)

    def status(self):
        total_occupation = sum([room.members_count for room in self.rooms])
        result = [f"Total population: {total_occupation}"]
        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.f2}$")
            if room.children:
                counter = 0
                for child in room.children:
                    counter += 1
                    result.append(f"---Child {counter} monthly cost: {child.get_monthly_expense():.2f}$")

            if hasattr(room, 'appliances'):
                app_expenses = 0
                for a in room.appliances:
                    app_expenses += a.get_monthly_expense()
                result.append(f"--- Appliances monthly cost: {app_expenses:.2f}$")

        return result
