# Teste_Tecnico_Data_Scientist_Pacto
repositório | arquivos | consumo api | power BI | DAX | sql

#Iunstruções de execução passo a passo:
Em uma interface visual de código, abra os arquivos

#Análise do desafio/Visão geral da solução:
O desafio proposto envolvia o consumo e organização de dados da Fake Store Api, de forma que fosse possível trabalhar com essas inofmrações de forma lógica e visual em ambiente de BI.
A solução envolve a limpeza e qualificação dos dados consultados via API com python para a organização de Data Frames que nos possibilitassem exportar esses arquivos em formato útil para BI. Utilizei a ferramenta power BI onde foram importadas e relacionadas as tabelas de fato, produto e usuarios, tendo sido criada uma tabela de medidas intermediarias que representam operações dax feitas com os valores trazidos das tabelas; foram geradas visualizações limnpas e objetivas sobre o que interpretei dos dados, agerando insights relevantes para um tomada teórica de decisões em cima dos dados trabalhados.

#Decisões Tecnicas tomadas:
<img width="318" height="159" alt="image" src="https://github.com/user-attachments/assets/a88d4bb6-4673-4029-a3b6-ad3513ad6624" />


- lib requests para consumir as informações
- pandas para a manipulação das informações, bem como .json_normalize para os dados aninhados
- Utilização de Star Schema para trabalhar com as tabelas de maneira otimizada
- Implementação de uma dimensão de calendário via DAX

#Principais desafios técnicos:
Percebi uma incompatibilidade no tipo de dados das tabelas fato e calendário, uma vez que o formato dos dados na tabela fato não podiam ser correspondidos com os da tabela data. Editei o formato dessa coluna em fato, que veio em *string*, para *data*, o que fez com que a relação entre as duas tabelas fosse estabelecida de maneira correta permitindo a criação das visualizações. 
Resumo: identificar o erro de tipagem para garantir a entrega do dashboard

#Sugestões de melhorias e próximos passos:
Os próximos passos em relação ao produto final do desafio seria implementar a mesma cadeia de decisões para valores reais, conseguindo entregar insights tangíveis por algum cliente real.
Percepção minha de melhoria, seria observar o processo de maneira mais ágil e holística, antecipando algum design genérico que permita apenas a alteração da relação de outras tabelas para um dashboard semelhante - nesse caso fiz tudo do 0 e pode ser prático deixar isso em uma esteira mais bem organizada

