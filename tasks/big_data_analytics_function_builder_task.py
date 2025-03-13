from crewai import Task
from pydantic import PrivateAttr
from agents.big_data_analytics_function_builder import BigDataAnalyticsFunctionBuilder

class BigDataAnalyticsFunctionBuilderTask(Task):
    _question: str = PrivateAttr()
    _data: dict = PrivateAttr()
    
    def __init__(self, question, data, **kwargs):
        big_data_analytics_function_builder = BigDataAnalyticsFunctionBuilder()
        super().__init__(
            description="Criar uma função Python que receba um conjunto de dados completo, processe os dados e gere um relatório em HTML contendo estatísticas, gráficos e insights relevantes. A função deve ser genérica o suficiente para lidar com diferentes formatos de dados estruturados e deve utilizar bibliotecas como Pandas, Seaborn, Matplotlib e Plotly.",
            expected_output="Uma função Python chamada `analisar_dados(dados: pd.DataFrame) -> str`, que recebe um DataFrame, processa os dados e gera um arquivo HTML com os seguintes elementos: estatísticas descritivas, gráficos interativos e análises de padrões nos dados. A saída final deve ser o caminho do arquivo HTML gerado.",
            agent=big_data_analytics_function_builder,
            **kwargs
        )
        self._question = question
        self._data = data

    def run(self):
        prompt = (
            f"Pergunta OPCIONAL: {self._question}\n"
            f"Amostra de Dados: {self._data}, a serem usados para gerar a função em python!\n"
            """Você receberá uma amostra dos dados como referência. Com base nessa amostra, escreva uma função genérica que possa ser aplicada a um dataset maior. A função que você criar deve: 1. Ler e processar os dados (limpeza, formatação e ajustes necessários); 2. Gerar estatísticas principais (médias, medianas, máximos, mínimos, desvio padrão, distribuição); 3. Detectar padrões e tendências (incluindo análise temporal, se aplicável); 4. Criar visualizações gráficas (usando Matplotlib, Seaborn ou Plotly); 5. Exportar os resultados para um arquivo HTML com gráficos interativos e insights formatados.
            """
        )
        
        result = self.agent.llm.call(prompt)
        return result
