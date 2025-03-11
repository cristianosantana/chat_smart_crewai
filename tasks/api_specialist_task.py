from crewai import Task
from agents.api_specialist import ApiSpecialist
from pydantic import PrivateAttr
from tools.extract_data_from_text import ExtractDataFromText

class ApiSpecialistTask(Task):
    _question: str = PrivateAttr()
    _endpoints_dict: dict = PrivateAttr()
    _extract_data_from_text = ExtractDataFromText()

    def __init__(self, question, endpoints_dict, **kwargs):
        api_specialist = ApiSpecialist()
        super().__init__(
            description=f"Dada a pergunta: '{question}', analise o dicionário de endpoints e identifique qual(is) endpoint(s) utilizar para obter os dados necessários.",
            agent=api_specialist,
            expected_output="Uma resposta objetiva contendo o(s) endpoint(s) mais relevante!",
            **kwargs
        )
        self._question = question
        self._endpoints_dict = endpoints_dict

    def run(self):
        prompt = (
            f"Pergunta: {self._question}\n"
            f"Endpoints disponíveis: {self._endpoints_dict}\n"
            "A partir desses dados, qual endpoint deve ser usados?"
            "Retorne a route, o method e o payload se houver! Uma coisa muito importante é que esses dados estejam entre os blocos ```route: * ```, ```method: * ``` e ```payload: * ```, converta o payload em json!"
        )
        
        decision = self.agent.llm.call(prompt)

        result = {
            'route': self._extract_data_from_text.extract_data_from_text(decision, r"```ROUTE:\s*\n?(.*?)```"),
            'method': self._extract_data_from_text.extract_data_from_text(decision, r"```METHOD:\s*\n?(.*?)```"),
            'payload': self._extract_data_from_text.extract_data_from_text(decision, r"```PAYLOAD:\s*\n?(.*?)```")
        }
        
        return result
