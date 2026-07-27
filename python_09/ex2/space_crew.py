#!/usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError
from pydantic import model_validator
from datetime import datetime
from enum import Enum


class CrewRank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with \"M\"")
        has_commander_or_captain = False
        for crew_member in self.crew:
            if crew_member.rank in [CrewRank.CAPTAIN, CrewRank.COMMANDER]:
                has_commander_or_captain = True
                break
        if not has_commander_or_captain:
            raise ValueError("Mission must have at"
                             " least one Commander or Captain")
        if self.duration_days > 365:
            total_crew = len(self.crew)
            experienced_crew = [
                crew_member for crew_member
                in self.crew
                if crew_member.years_experience >= 5
                ]
            if len(experienced_crew) / total_crew < 0.5:
                raise ValueError("Long missions (> 365 days) need 50% "
                                 "experienced crew (5+ years)")
        for crew_member in self.crew:
            if not crew_member.is_active:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=CrewRank.COMMANDER,
                age=45,
                specialization="Mission Command",
                years_experience=20,
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=CrewRank.LIEUTENANT,
                age=34,
                specialization="Navigation",
                years_experience=8,
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=CrewRank.OFFICER,
                age=29,
                specialization="Engineering",
                years_experience=6,
            ),
        ],
    )
    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for crew_member in valid_mission.crew:
        print(
            f"- {crew_member.name} "
            f"({crew_member.rank.value}) - "
            f"{crew_member.specialization}"
        )
    print()
    print("=========================================")
    print("Expected validation error:")

    try:
        SpaceMission(
            mission_id="M2024_BAD",
            mission_name="Invalid Deep Space Mission",
            destination="Europa",
            launch_date=datetime.now(),
            duration_days=120,
            budget_millions=1200.0,
            crew=[
                CrewMember(
                    member_id="CM004",
                    name="Bob Wilson",
                    rank=CrewRank.LIEUTENANT,
                    age=31,
                    specialization="Navigation",
                    years_experience=7,
                ),
                CrewMember(
                    member_id="CM005",
                    name="Carol Davis",
                    rank=CrewRank.OFFICER,
                    age=28,
                    specialization="Engineering",
                    years_experience=5,
                ),
            ],
        )
    except ValidationError as err:
        msg = str(err.errors()[0]["msg"])
        if msg.startswith("Value error, "):
            msg = msg[len("Value error, "):]
        print(msg)


if __name__ == "__main__":
    main()
