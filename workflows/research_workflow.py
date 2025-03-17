from teams.research_team import ResearchTeam
from tools.smart_services import SmartServices
import os

class ResearchWorkflow:
    def __init__(self, question, endpoints_dict):
        self.team = ResearchTeam(question, endpoints_dict)
        self.smart_services = SmartServices()

    def execute(self):
        response = self.team.run()
        return self.smart_services.run_external_api(os.getenv('BASE_URL'), response['method'], response['route'], response['payload'])
