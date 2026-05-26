# Global-Solution-Python
print("   SISTEMA DE MONITORAMENTO POR SATELITE - NIVEL DE CO2 E GAS METANO")
 
quantidade = 0
while quantidade < 1:
    entrada = input("\nInsira a quantidade de eventos: ")
    if entrada.isdigit():
        quantidade = int(entrada)
        if quantidade < 1:
            print("  ERRO: A quantidade deve ser pelo menos 1.")
    else:
        print("  ERRO: Digite um numero inteiro valido.")
 
tipos_eventos  = []
paises         = []
regioes        = []
cidades        = []
areas_afetadas = []
intensidades   = []
ocorrencias    = []
 
for i in range(quantidade):
    print("\n")
    print("  Evento", i + 1, "de", quantidade)
    print("------------------------------------------------------------")
 
    print("  Tipo de evento:")
    print("    1 - Emissao de CO2")
    print("    2 - Emissao de Gas Metano")
    tipo_valido = False
    while tipo_valido == False:
        entrada_tipo = input("  Escolha 1 ou 2: ").strip()
        if entrada_tipo == "1":
            tipos_eventos.append("Emissao de CO2")
            tipo_valido = True
        else:
            if entrada_tipo == "2":
                tipos_eventos.append("Emissao de Gas Metano")
                tipo_valido = True
            else:
                print("  ERRO: Digite 1 para CO2 ou 2 para Gas Metano.")
 
    pais = ""
    while pais == "":
        pais = input("  Pais: ").strip()
        if pais == "":
            print("  ERRO: Campo obrigatorio.")
    paises.append(pais)
 
 
    regiao = ""
    while regiao == "":
        regiao = input("  Regiao: ").strip()
        if regiao == "":
            print("  ERRO: Campo obrigatorio.")
    regioes.append(regiao)
 
 
    cidade = ""
    while cidade == "":
        cidade = input("  Cidade: ").strip()
        if cidade == "":
            print("  ERRO: Campo obrigatorio.")
    cidades.append(cidade)
 
    area_valida = False
    while area_valida == False:
        entrada_area = input("  Area afetada (km2): ").strip()
        try:
            area = float(entrada_area)
            if area > 0:
                areas_afetadas.append(area)
                area_valida = True
            else:
                print("  ERRO: A area deve ser maior que zero.")
        except:
            print("  ERRO: Digite um numero valido.")
 
    intensidade_valida = False
    while intensidade_valida == False:
        entrada_int = input("  Intensidade (1 a 10): ").strip()
        if entrada_int.isdigit():
            intensidade = int(entrada_int)
            if intensidade >= 1 and intensidade <= 10:
                intensidades.append(intensidade)
                intensidade_valida = True
            else:
                print("  ERRO: Intensidade deve estar entre 1 e 10.")
        else:
            print("  ERRO: Digite um numero inteiro valido.")
 
    ocorrencia_valida = False
    while ocorrencia_valida == False:
        entrada_oc = input("  Numero de ocorrencias: ").strip()
        if entrada_oc.isdigit():
            ocorrencia = int(entrada_oc)
            if ocorrencia >= 1:
                ocorrencias.append(ocorrencia)
                ocorrencia_valida = True
            else:
                print("  ERRO: O numero de ocorrencias deve ser pelo menos 1.")
        else:
            print("  ERRO: Digite um numero inteiro valido.")
 
    print("  >>> Evento", i + 1, "registrado com sucesso!")
 
 
print("\n============================================================")
print("   EVENTOS REGISTRADOS")
print("============================================================")
 
for i in range(quantidade):
    print("\n  [Evento", str(i + 1) + "]")
    print("  Tipo        :", tipos_eventos[i])
    print("  Pais        :", paises[i])
    print("  Regiao      :", regioes[i])
    print("  Cidade      :", cidades[i])
    print("  Area (km2)  :", areas_afetadas[i])
    print("  Intensidade :", intensidades[i])
    print("  Ocorrencias :", ocorrencias[i])
 
total_eventos = quantidade
 
 
soma_areas = 0.0
for i in range(quantidade):
    soma_areas = soma_areas + areas_afetadas[i]
 
 
soma_intensidades = 0
for i in range(quantidade):
    soma_intensidades = soma_intensidades + intensidades[i]
 
media_intensidade = soma_intensidades / quantidade
 
maior_area        = max(areas_afetadas)
indice_maior_area = areas_afetadas.index(maior_area)
 
 
regioes_unicas    = []
ocorr_por_regiao  = []
 
for i in range(quantidade):
    regiao_atual = regioes[i]
    if regiao_atual in regioes_unicas:
        indice_reg = regioes_unicas.index(regiao_atual)
        ocorr_por_regiao[indice_reg] = ocorr_por_regiao[indice_reg] + ocorrencias[i]
    else:
        regioes_unicas.append(regiao_atual)
        ocorr_por_regiao.append(ocorrencias[i])
 
maior_ocorr_regiao   = max(ocorr_por_regiao)
indice_regiao_top    = ocorr_por_regiao.index(maior_ocorr_regiao)
regiao_mais_ocorrencias = regioes_unicas[indice_regiao_top]
 
 
soma_densidades = 0.0
for i in range(quantidade):
    soma_densidades = soma_densidades + (ocorrencias[i] / areas_afetadas[i])
 
densidade_media = soma_densidades / quantidade
 
eventos_acima_media = 0
for i in range(quantidade):
    if intensidades[i] > media_intensidade:
        eventos_acima_media = eventos_acima_media + 1
 
 
maior_intensidade_geral = max(intensidades)
 
indices_max_int = []
for i in range(quantidade):
    if intensidades[i] == maior_intensidade_geral:
        indices_max_int.append(i)
 
areas_candidatas = []
for i in range(len(indices_max_int)):
    areas_candidatas.append(areas_afetadas[indices_max_int[i]])
 
indice_area_max_entre_candidatos = areas_candidatas.index(max(areas_candidatas))
indice_critico = indices_max_int[indice_area_max_entre_candidatos]
 
print("")
print("        RELATORIO DE ANALISE")
print("")
print("Total de eventos registrados:", total_eventos)
 
print("")
print("Resumo Geral")
print("-----------------------------------------")
print("Area total afetada:", round(soma_areas, 2), "km2")
print("Media de intensidade:", round(media_intensidade, 2))
 
print("")
print("Analises")
print("----------------------------------------")
print("Regiao com maior numero de ocorrencias:", regiao_mais_ocorrencias)
print("Quantidade de eventos acima da media de intensidade:", eventos_acima_media)
print("Densidade media de ocorrencias:", round(densidade_media, 2), "ocorrencias/km2")
 
print("")
print("Evento Mais Critico")
print("----------------------------------------")
print("Tipo:", tipos_eventos[indice_critico])
print("Local:", cidades[indice_critico] + ",", regioes[indice_critico] + ",", paises[indice_critico])
print("Intensidade:", intensidades[indice_critico])
print("Area afetada:", round(areas_afetadas[indice_critico], 2), "km2")
 
print("========================================")
print("Total de desastres registrados:", total_eventos)
