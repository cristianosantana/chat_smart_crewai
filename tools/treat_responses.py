class TreatResponses():
    
    def generate_html_table_os_pending(self, dados):
        """
            Trata Resposta do metodo getOsPendentes
        """
        if not dados:
            return "<p>Nenhum dado disponível</p>"

        colunas = dados[0].keys()  # Pegamos as colunas a partir do primeiro item

        # Início da tabela
        html = "<table border='1' style='border-collapse: collapse; width: 100%;'>"
        
        # Cabeçalho da tabela
        html += "<tr>"
        for coluna in colunas:
            html += f"<th>{coluna}</th>"
        html += "</tr>"

        # Linhas da tabela
        for item in dados:
            html += "<tr>"
            for coluna in colunas:
                valor = item[coluna]

                if isinstance(valor, list):  # Se for uma lista (exemplo: veículos, endereços)
                    itens_formatados = []
                    for subitem in valor:
                        if isinstance(subitem, dict):  # Se for um dicionário dentro da lista
                            nome = subitem.get("nome") or subitem.get("descrição") or subitem.get("descricao") or subitem.get("valor") or subitem.get("valor_venda_real")
                            if nome:
                                itens_formatados.append(nome)
                            else:
                                itens_formatados.append("Object")  # Caso não tenha nome ou descrição ou valor ou valor_venda_real
                        else:
                            itens_formatados.append("Object")  # Caso seja uma lista simples
                    valor_formatado = "<br>".join(itens_formatados)

                elif isinstance(valor, dict):  # Se for um dicionário direto
                    valor_formatado = valor.get("nome") or valor.get("descrição") or valor.get("descricao") or subitem.get("valor") or subitem.get("valor_venda_real") or "Object" 
                
                else:
                    valor_formatado = valor  # Valor normal
                
                html += f"<td>{valor_formatado}</td>"
            html += "</tr>"

        html += "</table>"
        return html