# Urna eleitoral por Joaquim Rafael Mariano Prieto Pereira
# Graduando de Ciência da Computação da Universidade Presbiteriana Mackenzie

# função para cadastrar os candidatos
def candidatos():
    # cria as listas
    pres = []
    gov = []
    pref = []
    nomes_partidos = []
    lista_partidos = []
    while True:
        # rececebe as informações do candidato
        nome = input('Nome: ').title().strip()
        num = int(input('Número: ').strip())
        partido = input('Partido: ').upper()
        cargo = input('Cargo: ').lower().strip()
        cand = [num, nome, partido, cargo, 0]

        print(cand)
        # posiciona os candidatos referente ao seu cargo
        if cargo == 'presidente':
            pres.append(cand)
        elif cargo == 'governador':
            gov.append(cand)
        elif cargo == 'prefeito':
            pref.append(cand)
        # cria a lista de partidos e seus respectivos candidatos eleitos
        if partido not in nomes_partidos:
            nomes_partidos.append(partido)
            p = partido
            lista_partidos.append([p, 0])

        continuar = input('Deseja continuar? ').strip().upper()

        if continuar == 'NAO' or continuar == 'NÃO':
            break
    return pres, gov, pref, lista_partidos


# função para cadastrar eleitores
def eleitores():
    # cria a lista de eleitores
    eleitor = []
    while True:
        # recebe as informações de cada eleitor e adciona na lista
        nome = input('Digite o nome do eleitor: ').title()
        cpf = int(input('Digite o cpf do eleitor: ').strip())
        lista = [nome, cpf]
        eleitor.append(lista)
        print(lista)

        continuar = input('Deseja continuar? ').strip().upper()

        if continuar == 'NAO' or continuar == 'NÃO':
            break
    return eleitor


# cria variaveis para armazenas os votos brancos e nulos de cada cargo
nulo_pres = 0
branco_pres = 0
nulo_gov = 0
branco_gov = 0
nulo_pref = 0
branco_pref = 0


# função para votar
def votar(eleit, presi, gove, prefe):
    for i in eleit:
        print('Eleitor {}'.format(i))
        # voto para presidente
        for j in range(3):
            if j == 0:
                while True:
                    # contabiliza os votos validos para presidente
                    print('Voto para Presidente')
                    voto_pres = int(input('Digite o seu voto para presidente(Branco -1 Nulo -2): '))
                    x = 0
                    for k in presi:
                        if voto_pres == k[0]:
                            global pres
                            pres[x][4] += 1
                            print(k)
                            confirma = input('Confirma o voto?: ').strip().lower()
                            if confirma == 'sim':
                                break
                            else:
                                pres[x][4] -= 1
                        x += 1
                    # contabiliza votos brancos
                    if voto_pres == -1:
                        print('VOTO BRANCO')
                        global branco_pres
                        branco_pres += 1
                        confirma = input('Confirma o voto?: ').strip().lower()
                        if confirma == 'sim':
                            break
                        else:
                            branco_pres -= 1

                    # contabiliza votos nulos
                    elif voto_pres == -2:
                        print('VOTO NULO')
                        global nulo_pres
                        nulo_pres += 1
                        confirma = input('Confirma o voto?: ').strip().lower()
                        if confirma == 'sim':
                            break
                        else:
                            nulo_pres -= 1
                    if confirma == 'sim':
                        break
            # voto para governador
            elif j == 1:
                while True:
                    print('Voto para Governador')
                    voto_gov = int(input('Digite o seu voto para Governador(Branco -1 Nulo -2): '))
                    y = 0
                    for k in gove:
                        # contabiliza os votos validos para governador
                        if voto_gov == k[0]:
                            global gov
                            gov[y][4] += 1
                            print(k)
                            confirma = input('Confirma o voto?: ').strip().lower()
                            if confirma == 'sim':
                                break
                            else:
                                gov[y][4] -= 1
                        y += 1

                    if voto_gov == -1:
                        # contabiliza votos brancos
                        print('VOTO BRANCO')
                        global branco_gov
                        branco_gov += 1
                        confirma = input('Confirma o voto?: ').strip().lower()
                        if confirma == 'sim':
                            break
                        else:
                            branco_gov -= 1

                    elif voto_gov == -2:
                        # contabiliza votos nulos
                        print('VOTO NULO')
                        global nulo_gov
                        nulo_gov += 1
                        confirma = input('Confirma o voto?: ').strip().lower()
                        if confirma == 'sim':
                            break
                        else:
                            nulo_gov -= 1
                    if confirma == 'sim':
                        break

            # voto para prefeito
            elif j == 2:
                while True:
                    print('Voto para Prefeito')
                    voto_pref = int(input('Digite o seu voto para Prefeito (Branco -1 Nulo -2): '))
                    z = 0
                    for k in prefe:
                        # contabiliza os votos validos para prefeito
                        if voto_pref == k[0]:
                            global pref
                            pref[z][4] += 1
                            print(k)
                            confirma = input('Confirma o voto?: ').strip().lower()
                            if confirma == 'sim':
                                break
                            else:
                                pref[z][4] -= 1
                        z += 1

                    if voto_pref == -1:
                        # contabiliza votos brancos
                        print('VOTO BRANCO!')
                        global branco_pref
                        branco_pref += 1
                        confirma = input('Confirma o voto?: ').strip().lower()
                        if confirma == 'sim':
                            break
                        else:
                            branco_pref -= 1

                    elif voto_pref == -2:
                        # contabiliza votos nulos
                        print('VOTO NULO!')
                        global nulo_pref
                        nulo_pref += 1
                        confirma = input('Confirma o voto?: ').strip().lower()
                        if confirma == 'sim':
                            break
                        else:
                            nulo_pref -= 1
                    if confirma == 'sim':
                        break


# função para apurar resultados
def resultados(parti):
    # apuração presidente
    validos_pres = 0
    pres_ord = sorted(pres, key=lambda x: x[4], reverse=True)
    x = 0
    for n in parti:
        if pres_ord[0][2] == n[0]:
            parti[x][1] += 1
        x += 1
    print('O Candidato vencedor para Presidente foi: {}'.format(pres_ord[0]))
    print('')
    for p in pres_ord:
        validos_pres += p[4]
    print('Ranking de resultados para presidente')
    print('')
    print('Nome -  Partido - Votos - Porcentagem dos votos válidos')
    lugar = 1
    for x in pres_ord:
        print('')
        print(lugar, x[1], x[2], x[4], (x[4] / validos_pres) * 100)
        lugar += 1
    total_pres = branco_pres + nulo_pres + validos_pres
    print('')
    print('Total de votos =', total_pres)
    print('Total de votos válidos e % =  {} votos   {:.2f}%'.format(validos_pres, (validos_pres / total_pres) * 100))
    print('Total de votos brancos e % =  {} votos   {:.2f}%'.format(branco_pres, (branco_pres / total_pres) * 100))
    print('Total de votos nulos e %   =  {} votos   {:.2f}%'.format(nulo_pres, (nulo_pres / total_pres) * 100))
    print()
    # apuração governador
    validos_gov = 0
    gov_ord = sorted(gov, key=lambda x: x[4], reverse=True)
    y = 0
    for m in parti:
        if gov_ord[0][2] == m[0]:
            parti[y][1] += 1
        y += 1
    print('O Candidato vencedor para Governador foi: {}'.format(gov_ord[0]))
    print('')
    for g in gov_ord:
        validos_gov += g[4]
    print('Ranking de resultados para governador')
    print('')
    print('Nome -  Partido - Votos - Porcentagem dos votos válidos')
    lugar1 = 1
    for y in gov_ord:
        print('')
        print(lugar1, y[1], y[2], y[4], (y[4] / validos_gov) * 100)
        lugar1 += 1
    total_gov = branco_gov + nulo_gov + validos_gov
    print('')
    print('Total de votos =', total_gov)
    print('Total de votos válidos e % =  {} votos   {:.2f}%'.format(validos_gov, (validos_gov / total_gov) * 100))
    print('Total de votos brancos e % =  {} votos   {:.2f}%'.format(branco_gov, (branco_gov / total_gov) * 100))
    print('Total de votos nulos e %   =  {} votos   {:.2f}%'.format(nulo_gov, (nulo_gov / total_gov) * 100))
    print()
    # apuração prefeito
    validos_pref = 0
    pref_ord = sorted(pref, key=lambda x: x[4], reverse=True)
    z = 0
    for o in parti:
        if pref_ord[0][2] == o[0]:
            parti[z][1] += 1
        z += 1
    print('O Candidato vencedor para Prefeito foi: {}'.format(pref_ord[0]))
    print('')
    for pf in pref_ord:
        validos_pref += pf[4]
    print('Ranking de resultados para Prefeito')
    print('')
    print('Nome -  Partido - Votos - Porcentagem dos votos válidos')
    lugar2 = 1
    for z in pref_ord:
        print('')
        print(lugar2, z[1], z[2], z[4], (z[4] / validos_pref) * 100)
        lugar2 += 1
    total_pref = branco_pref + nulo_pref + validos_pref
    print('')
    print('Total de votos =', total_pref)
    print('Total de votos válidos e % =  {} votos   {:.2f}%'.format(validos_pref, (validos_pref / total_pref) * 100))
    print('Total de votos brancos e % =  {} votos   {:.2f}%'.format(branco_pref, (branco_pref / total_pref) * 100))
    print('Total de votos nulos e %   =  {} votos   {:.2f}%'.format(nulo_pref, (nulo_pref / total_pref) * 100))
    print()
    return total_pres, parti


# função para Relatório e Estatísticas
def relatorio():
    # Exibie uma lista dos eleitores que votaram, ordenados por nome
    list_eleitores = sorted(eleitor, key=lambda x: x[0])
    print(list_eleitores)
    # Checar se a quantidade de eleitores bate com o total de votos registrados na eleição
    n_eleitores = len(eleitor)
    n_votos = total_votos
    if n_votos == n_eleitores:
        print('A auditoria confirma que o número de votos é igual ao de eleitores')
    else:
        print('O número de eleitores não bate com o número de votos')
    # Mostra qual partido elegeu mais políticos e mostra qual partido elegeu menos políticos
    list_par = sorted(eleitos_part, key=lambda x: x[1], reverse=True)
    print('O Partido que mais elegeu políticos foi {} eleitos'.format(list_par[0]))
    print('O Partido que menos elegeu políticos foi {} eleitos'.format(list_par[-1]))


# menu de opções
while True:
    print('')
    print('+' * 7, 'MENU SIMULADOR DO SISTEMA DE VOTAÇÃO', '+' * 7)
    print('1. Cadastrar Candidatos')
    print('2. Cadastrar Eleitores')
    print('3. Votar')
    print('4. Apurar Resultados')
    print('5. Relatório e Estatísticas')
    print('6. Encerrar')
    op = int(input('Opção Escolhida: ').strip())
    # executa conforme a opção escolhida
    if op == 1:
        pres, gov, pref, partido = candidatos()
    elif op == 2:
        eleitor = eleitores()
    elif op == 3:
        votar(eleitor, pres, gov, pref)
    elif op == 4:
        total_votos, eleitos_part = resultados(partido)
    elif op == 5:
        relatorio()
    elif op == 6:
        break
    else:
        print('Opção Inválida')
