# api.py
import enum
import logging
from livekit.agents import llm

logger = logging.getLogger("temperature-control")

class Zone(enum.Enum):
    LIVING_ROOM = "living_room"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"

class AssistantFnc(llm.ToolContext):
    def __init__(self):
        super().__init__()
        self._temperature = {
            Zone.LIVING_ROOM: 22,
            Zone.BEDROOM: 20,
            Zone.KITCHEN: 24,
            Zone.BATHROOM: 23,
            Zone.OFFICE: 21,
        }

    @llm.function_tool(description="Get the temperature in a specific room")
    def get_temperature(self, zone: Zone):
        return f"The temperature in the {zone.value} is {self._temperature[zone]}°C"

    @llm.function_tool(description="Set the temperature in a specific room")
    def set_temperature(self, zone: Zone, temp: int):
        self._temperature[zone] = temp
        return f"The temperature in the {zone.value} is now set to {temp}°C"
