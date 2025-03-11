from flask import Blueprint, render_template, request, jsonify
from workflows.research_workflow import ResearchWorkflow  # Importe sua classe ResearchWorkflow
from tools.treat_responses import TreatResponses

bp = Blueprint('main', __name__)
treat_responses = TreatResponses()
dicionario = {
    "getVendasPorTipoPagamento" : { "route": "admin/relatorio-financeiro/vendedor/vendas-por-tipo-pagamento", "method": "POST", "payload": {} },
    "getOsPendentes" : { "route": "admin/relatorio-financeiro/vendas_pendentes_pagamento", "method": "POST", "payload": { "os_tipo_id": 2, "os_status": "FECHADA" } },
    "comissoesPorConcessionariaPeriodo" : { "route": "chat_ai/relatorio/comissoes_por_concessionaria_periodo", "method": "POST", "payload": {"data_inicio": "Y-mm-d 01:00:00", "data_final": "Y-mm-d 23:59:00"} },
    "vendasServicosPorPeriodo" : { "route": "chat_ai/relatorio/vendas_servicos_por_periodo", "method": "POST", "payload": {"data_inicio": "Y-mm-d 01:00:00", "data_final": "Y-mm-d 23:59:00"} },
    "notasFiscaisEmitidasPorEmpresasMes" : { "route": "chat_ai/relatorio/notas_fiscais_emitidas_por_empresas_mes", "method": "POST", "payload": { "month": "m", "year": "Y"} },
}

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/pergunta', methods=['POST'])
def pergunta():
    resultado_pesquisa = None
    data = request.get_json()
    pergunta = data.get('pergunta')

    if not pergunta:
        return jsonify({"error": "Pergunta não fornecida."}), 400
    
    workflow = ResearchWorkflow(pergunta, dicionario) # Instancia o ResearchWorkflow com a pergunta e o dicionário
    resultado_pesquisa = workflow.execute() # Executa o workflow e armazena o resultado
    print(resultado_pesquisa)
    if 'error' in resultado_pesquisa:
        return jsonify(resultado_pesquisa)
    
    tabela_html = treat_responses.generate_html_table_os_pending(resultado_pesquisa)
    
    return jsonify({"tabela_html": tabela_html})


# quero relatorio de comissoes por concessionarias de janeiro de 2025
# notas fiscais emitidas por empresa de janeiro de 2025
# quero relatório vendas por serviços do junho de 2024
# quero relatorio de vendas por tipo de pagamento