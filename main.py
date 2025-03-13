from workflows.research_workflow import ResearchWorkflow

if __name__ == "__main__":
    """
        DESCONTINUADO!
        Esse arquivo roda o time no terminal! Para isso execute: ```python main.py``` dentro do venv.
    """
    question = input("Digite sua perguntar: ")
    dicionario = {
        "obterFechamentoGerencial" : { "route": "relatorio-financeiro/fechamento/gerencial", "method": "POST" },
        "obterRelatorioNotasFiscais" : { "route": "relatorio-financeiro/notasfiscais", "method": "POST" },
        "obterRelatorioEvolucaoCancelamento" : { "route": "relatorio-financeiro/evolucao/cancelamento", "method": "POST" },
        "obterVendasAtuais" : { "route": "relatorio-financeiro/vendas-anuais", "method": "POST" },
        "obterVendasVsRecebimentos" : { "route": "relatorio-financeiro/vendas-vs-recebimentos", "method": "POST" },
        "getSalesByPaymentType" : { "route": "relatorio-financeiro/vendedor/vendas-por-tipo-pagamento", "method": "POST" },
        "getSalesByPaymentTypeCC" : { "route": "relatorio-financeiro/vendedor/vendas-tipo-pagamento-cc", "method": "POST" },
        "getInvoicesByCompany" : { "route": "relatorio-financeiro/notas-fiscais-por-empresas", "method": "POST" },
        "obterRelatorioCustos" : { "route": "relatorio-financeiro/relatorio-custos", "method": "POST" },
        "obterEstoqueEntradaProdutos" : { "route": "relatorio-financeiro/estoque_entrada_produtos", "method": "POST" },
        "obterOsPendentes" : { "route": "relatorio-financeiro/vendas_pendentes_pagamento", "method": "POST" }
    }
    workflow = ResearchWorkflow(question, dicionario)
    result = workflow.execute()
    # print("Resultado da pesquisa:", result)