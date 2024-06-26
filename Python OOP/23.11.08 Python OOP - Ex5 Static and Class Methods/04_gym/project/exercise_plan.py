class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int,  duration: int) -> None:
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration  # minutes
        self.id = ExercisePlan.id
        ExercisePlan.id += 1

    @staticmethod
    def get_next_id() -> int:
        return ExercisePlan.id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours*60)

    def __repr__(self) -> str:
        return f"Plan <{self.id}> with duration {self.duration} minutes"
