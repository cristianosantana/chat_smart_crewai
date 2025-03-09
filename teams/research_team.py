from crewai import Crew
from tasks.api_specialist_task import ApiSpecialistTask

class ResearchTeam:
    def __init__(self, question, endpoints_dict):
        self.api_specialist_task = ApiSpecialistTask(question, endpoints_dict)
        self.crew = Crew(
            agents=[self.api_specialist_task.agent],
            tasks=[self.api_specialist_task]
        )

    def run(self):
        return self.api_specialist_task.run()
        
