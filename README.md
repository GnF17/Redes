**Redes - Blockchain**

 Repositório utilizado para a matérias de Redes de Computadores
Este trabalho trata sobre o desenvolvimento de uma aplicação presta e consome serviços através da Interface de Programação de Aplicação (API) disponibilizada pelos sistemas operacionais: Sockets.

Utilitário blockchain
– O utilitário é simultaneamente cliente e servidor (peer-to-peer)
– Diferentes clientes devem ser capazes de se descobrir em uma rede local
– O usuário deve ser capaz de adicionar um bloco à sua cadeia de blocos local (inclusão)
– O utilitário deve trocar sua cadeia de blocos local com os seus pares remotos, que mantém uma lista das cadeias transmitidas por cada um dos pares (divulgação)
– Assim que todos os pares receberem o bloco, eles devem checar a integridade da cadeia (mineração)
– Se a cadeia não for íntegra, o par deve divulgar para todos os seus pares que este é o caso (mineração)
– Deve ser executada periodicamente a votação entre os pares da rede para determinar qual cadeia entre eles é a cadeia válida real (consenso)
– Caso um dos pares tenha uma cadeia inválida, deverá recalcular o conteúdo dos blocos não presentes na cadeia considerada válida, e adicioná-los a esta cadeia (inclusão), reiniciando o processo de divulgação da cadeia entre os pares
– Referência: https://www.bitcoin.com/satoshi-archive/whitepaper
