from crewai import Crew
from tasks.api_specialist_task import ApiSpecialistTask
from tasks.big_data_analytics_function_builder_task import BigDataAnalyticsFunctionBuilderTask
from tools.smart_services import SmartServices
from tools.treat_responses import TreatResponses
import os

class ResearchTeam:
    def __init__(self, question, endpoints_dict):
        self.api_specialist_task = ApiSpecialistTask(question, endpoints_dict)
        self.big_data_analytics_function_builder_task = BigDataAnalyticsFunctionBuilderTask(question, endpoints_dict)
        self.smart_services = SmartServices()
        self.treat_responses = TreatResponses()

        self.crew = Crew(
            agents=[self.api_specialist_task.agent, self.big_data_analytics_function_builder_task.agent],
            tasks=[self.api_specialist_task, self.big_data_analytics_function_builder_task]
        )

    def run(self):
        responseApiSpecialist = self.api_specialist_task.run()
        data = self.smart_services.run_external_api(os.getenv('BASE_URL'), responseApiSpecialist['method'], responseApiSpecialist['route'], responseApiSpecialist['payload'])
        if len(data) > 0:
            print(self.treat_responses.simple_random_sample(data, 1))
            # responseBigDataAnalyticsFunctionBuilder = self.big_data_analytics_function_builder_task.run()
        else: 
            print(f"DADOS: {data}")
        
        return data