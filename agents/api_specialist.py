from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

class ApiSpecialist(Agent):
    def __init__(self):
        super().__init__(
            role="Especialista em APIs REST",
            goal="Dado uma pergunta e um dicionário de endpoints, identificar e utilizar o(s) endpoint(s) REST apropriado(s) para obter os dados necessários.",
            backstory="Desenvolvedor experiente em integrações REST, capaz de ler documentação de APIs, analisar dicionários de endpoints e realizar chamadas HTTP para fornecer respostas precisas.",
            verbose=True,
            allow_delegation=True,
            llm = LLM(
                model="groq/deepseek-r1-distill-llama-70b",
                temperature=0.7
            )
        )
