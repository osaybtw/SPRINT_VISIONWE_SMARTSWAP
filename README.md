# CHARGEGRID - SMARTSWAP

# Equipe - VisionWe
Arthur de Oliveira Carvalho - RM: 573499

Gabriel Henrique S. de Melo Rodrigues - RM: 573093

Fernando Bonfim Hoefle - RM: 569920

Anna Cecília Guimarães M. Lima de Carvalho - RM: 570955

Caio Marques - RM: 573847

# Soluções em Energias Renováveis e Sustentáveis

# Problema

O crescimento da mobilidade elétrica aumenta a demanda por infraestrutura de recarga. Em eletropostos comerciais, o tempo de espera, a gestão do consumo energético e o controle operacional podem comprometer a experiência do usuário e a eficiência do serviço. O projeto busca reduzir esse problema por meio da substituição rápida de baterias, permitindo melhor organização da recarga e maior disponibilidade para os usuários.

# Solução

O ChargeGrid SmartSwap é uma proposta de eletroposto inteligente baseada na troca de baterias. Em vez de aguardar a recarga do veículo, o motorista recebe uma bateria carregada enquanto a bateria descarregada entra em uma fila de recarga. A solução consiste em uma estação de troca de baterias gerenciada por um sistema desenvolvido em Python. O operador registra trocas, acompanha o estoque de baterias, finaliza recargas e consulta relatórios financeiros. A proposta contribui para a eficiência energética ao permitir uma gestão mais organizada da recarga das baterias. Além disso, a arquitetura no futuro visa ser integrada a sistemas fotovoltaicos da GoodWe, possibilitando que parte da energia utilizada seja proveniente de fontes renováveis. A solução também reduz o tempo de permanência dos veículos no posto, aumentando a eficiência operacional da infraestrutura.

# Fluxo simplificado:

Veículo chega -> Troca de bateria -> Cobrança -> Bateria descarregada vai para recarga -> Retorna ao estoque após carregamento

# Viabilidade Técnica

A prova de conceito demonstra que a lógica de troca de baterias pode ser implementada por meio de software, permitindo controlar estoque, registrar operações, gerenciar recargas e gerar relatórios financeiros. Os dados produzidos pelo sistema comprovam a viabilidade inicial da proposta e servem como base para futuras expansões. O ChargeGrid SmartSwap apresenta uma alternativa viável para otimizar a gestão de eletropostos comerciais. A proposta combina mobilidade elétrica, eficiência energética e sustentabilidade em uma solução simples, escalável e alinhada aos objetivos do desafio GoodWe.

# Pensamento Computacional e Automação em Python

# Problema

A expansão da mobilidade elétrica exige soluções mais organizadas para a gestão de eletropostos comerciais. Quando há muitas demandas simultâneas, o posto precisa controlar disponibilidade de baterias, cobrança, fila de recarga e fluxo de operação sem depender apenas de processos manuais. Nesse cenário, torna-se necessário desenvolver sistemas capazes de automatizar tarefas, registrar informações e auxiliar na tomada de decisão, garantindo maior eficiência operacional e melhor experiência para os usuários.

# Solução

O ChargeGrid SmartSwap é uma prova de conceito funcional desenvolvida em Python para simular a operação de uma estação inteligente de troca de baterias. O sistema permite registrar trocas, calcular cobranças, controlar o estoque de baterias disponíveis, acompanhar baterias em recarga e gerar relatórios financeiros. A proposta demonstra como conceitos de automação e pensamento computacional podem ser aplicados ao contexto do desafio GoodWe. O sistema organiza informações operacionais, automatiza cálculos de tarifação e mantém o controle das baterias em diferentes estados de utilização. Além disso, a estrutura foi projetada para possibilitar futuras integrações com sensores, bancos de dados, plataformas de monitoramento e recursos de inteligência artificial voltados à previsão de demanda e otimização da operação.

# Fluxo Simplificado

Veículo chega -> Troca de bateria -> Cálculo da cobrança -> Pagamento confirmado -> Bateria descarregada vai para recarga -> Retorna ao estoque após carregamento -> Geração de relatórios

# Conceitos Aplicados

O projeto evidencia conceitos de gerenciamento inteligente de demanda por meio do controle de disponibilidade das baterias e do monitoramento do estoque da estação. A tarifação e o pagamento são representados pelo cálculo automático do valor cobrado com base na energia consumida. A interoperabilidade é considerada na proposta de integração futura com o ecossistema GoodWe e outras tecnologias de monitoramento e gestão. Já a inteligência artificial pode ser incorporada em versões futuras para prever padrões de utilização, auxiliar na gestão do estoque e otimizar o processo de recarga.

# Viabilidade Técnica

A prova de conceito demonstra que a lógica operacional de um sistema de troca de baterias pode ser implementada por meio de software utilizando Python. O protótipo registra operações, gera dados financeiros, controla o estoque e acompanha o estado das baterias em recarga, comprovando a aplicação prática da solução proposta. Os resultados obtidos durante as simulações demonstram que a solução possui viabilidade técnica inicial e potencial para expansão em futuras versões. O ChargeGrid Intelligence representa uma aplicação direta dos conceitos estudados na disciplina, combinando automação, lógica computacional e gestão operacional em uma solução simples, funcional e alinhada aos objetivos do desafio GoodWe.
