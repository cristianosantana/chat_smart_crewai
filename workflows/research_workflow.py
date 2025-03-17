from teams.research_team import ResearchTeam

class ResearchWorkflow:
    def __init__(self, question, endpoints_dict):
        self.team = ResearchTeam(question, endpoints_dict)

    def execute(self):
        return self.team.run()
