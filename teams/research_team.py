from crewai import Crew
from tasks.api_specialist_task import ApiSpecialistTask
from tasks.big_data_analytics_function_builder_task import BigDataAnalyticsFunctionBuilderTask

class ResearchTeam:
    def __init__(self, question, endpoints_dict):
        self.api_specialist_task = ApiSpecialistTask(question, endpoints_dict)
        self.big_data_analytics_function_builder_task = BigDataAnalyticsFunctionBuilderTask(question, endpoints_dict)

        self.crew = Crew(
            agents=[self.api_specialist_task.agent, self.big_data_analytics_function_builder_task.agent],
            tasks=[self.api_specialist_task, self.big_data_analytics_function_builder_task]
        )

    def run(self):
        responseApiSpecialist = self.api_specialist_task.run()
        responseBigDataAnalyticsFunctionBuilder = self.big_data_analytics_function_builder_task.run()
        print(responseBigDataAnalyticsFunctionBuilder)
        return responseApiSpecialist
        
