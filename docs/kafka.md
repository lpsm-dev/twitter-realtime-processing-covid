# Apache Kafka

## Contexto

Atualmente, tratar dados por streaming, ou seja, em tempo real, é uma das demandas mais requisitadas, pois a necessidade de tomar decisões sobre os dados que são muito voláteis ou em sistemas críticos, tem aumentado consideravelmente.

Assim, muitos problemas que antes eram tratados apenas por processamento em batch, agora ganham a necessidade de ter uma camada a mais, a de Streaming.

A imagem a baixo mostra uma arquitetura de Big Data chamada **Kappa**, onde exemplifica a existência do processamento em batch e o streaming. Existe uma camada para tratar dados por batch (Batch Layer), ou seja, processamento de dados pesados, histórico e de forma agendada. E outra camada para processamento de dados de forma rápida e em tempo real, no caso Streaming (Speed Layer), que permite processamento e análise de dados com menor **delay**.

<p align="center">
  <img alt="architecture-batch-streaming" src="https://miro.medium.com/max/1400/1*t2Sz1y-gf969MLAw0wvK5w.png" width="700px" float="center"/>
</p>

## O que é o Apache Kafka?

O Apache Kafka é uma plataforma distribuída de mensagens e streaming.

É uma poderosa ferramente multi-propósito que tem ganhado bastante destaque, pois apresente: desempenho, estabilidade e escalabilidade. 

Muitos especialistas recomendam essa ferramente para processamento de dados por streaming.

O Kafka é mais conhecido por ser uma ferramenta de mensageira, porém conforme a sua documentação e a experiência que adquirimos ao utilizá-lo, descobrimos que ele vai muito além, contendo uma arquitetura robusta para prover streaming de dados com segurança, desempenho, disponibilidade e escalabilidade.

## O que isso significa?

Uma plataforma de streaming possui três recursos principais:

* Publicar e assinar fluxos de registros, semelhante a uma fila de mensagens.
* Armazenar fluxos de registros de maneira durável e tolerante a falhas.
* Processas fluxos de registros conforme eles ocorrem.

## Casos de uso do Apache Kafka

O Kafka é geralmente usado para duas grandes classes de aplicativos:

* Construção de pipelines de dados de streaming em tempo real que obtêm dados entre sistemas ou aplicativos de maneira confiável.

* Construir aplicativos de streaming em tempo real que transformam ou reagem aos fluxos de dados.

## Fluxo básico do Kafka

Basicamente, o fluxo do Kafka pode ser resumido em três ações bem simples:

1. Você produz uma mensagem.
2. Essa mensagem é anexada em um tópico.
3. Você então consome essa mensagem.

<p align="center">
  <img alt="kafka-workflow" src="https://miro.medium.com/max/1400/1*q2jYvDNJMS72HgWsOG1f8g.png" width="700px" float="center"/>
</p>

## Para o que posso usar o Kafka então?

Se você quer mover e transformar um grande volume de dados em tempo real entre diferentes sistemas, então Apache Kafka pode ser exatamente o que você precisa.

## Principais conceitos

* O Kafka é executado como um cluster em um ou mais servidores que podem abranger vários data-centers.
* O cluster Kafka armazena fluxos de registros em categorias chamadas **tópicos**.
* Cada registro consiste em uma chave, um valor e um carimbo de data/hora.

O Kakfa tem cinco API's principais:

1. Producer API: 
  * Permite que um aplicativo publique o fluxo de registros em um ou mais tópicos do Kafka.
2. Consumer API: 
  * Permite que um aplicativo assine um ou mais tópicos e processe o fluxo de registros produzidos.
3. Streams API: 
  * Permite que um aplicativo atue como um processador de fluxo, consumindo um fluxo de entrada de um ou mais tópicos e produzindo um fluxo de saída para um ou mais tópicos de saída, transformando efetivamente os fluxos de entrada em fluxos de saída.
4. Connector API: 
  * Permite criar e executar produtores e consumidores reutilizáveis que conectam tópicos do Kakfa a aplicativos ou sistemas de dados existentes. Por exemplo, um conector para um banco de dados relacional pode capturar todas as alterações em um tabela.
5. Admin API: 
  * Permite gerenciar e inspecionar tópicos, intermediários e outros objetos Kafka.

No Kafka a comunicação entre clientes e os servidores é feita com um protocolo TCP independente da linguagem, simples e de alto desempenho.

### Mensagens - Messages

Trata-se dos dados que serão transmitidos através do Kafka, normalmente são mensagens de textos que podem ser traduzidas em diversos formatos, como JSON e XML...

Mensagem é basicamente o principal recurso do Kafka.

Todos os eventos do Kafka podem ser resumidos em mensagens, sendo consumidos e produzidos através de **tópicos**.

Uma mensagem pode ser desde uma simples String com "Hello World!" ou até mesmo um JSON contendo um objeto do seu domínio.

O Kafka te permite definir Schemas para mensagens. Como num exemplo de um JSON contendo um objeto do seu domínio, o Schema pode auxliar impedindo que mensagens contendo conteúdos inválidos sejam trafegadas no tópico.

Mensagens também podem ser compostas por uma chave (key/value) que é utilizada para sharding e compactação dentro do Kafka. Assim em um ambiente distribuído, é garantido a ordem das mensagens uma vez que mensagens com a mesma chave são direcionadas para uma única partição do Kafka.

### Tópicos - Topics

É o canal por onde é feito a troca dos dados entre os interessados, no caso produtores e consumidores das mensagens.

Um tópico é como categorizamos grupos de mensagens dentro do Kafka.

Todas as mensgens enviadas para o Kafka permanecem em um tópico. Mensagens são imutáveis e ordenadas.

Para manter a ordenação em um ecossistema de Kafka, os tópicos possuem partições e fatores de replicação. 

Um tópico pode possuir N partições, mas ao receber uma nova mensagem o Kafka automaticamente direciona aquela mensagem para uma partição específica dependendo de sua chave (key). Assim, mensagens de uma mesma chave estarão apenas em uma única partição, garantindo a leitura ordenada de todas as mensagens de um tópico.

### Produtores - Producers

Trata-se de quem está produzindo as mensagens em um determinado tópico de interesse.

Responsável por enviar uma mensagem para um tópico específico.

De forma simples, você pode produzir uma mensagem em um tópico.

Uma vez que uma mensagem é produzida em um tópico o próprio Kafka organiza a mensagem em uma partição, garantindo sempre a ordem das mensagens produzidas.

### Consumidores - Consumers

Trata-se de quem está consumindo as mensagens que são publicadas em um determinado tópico.

### Apache Zookeeper

O Zookeeper é um serviço centralizado para, entre outras coisas, coordenação de sistemas distribuídos. 

O Kafka é um sistema distribuído, e consequentemente delega diversas funções de gerenciamento e coordenação para o Zookeeper.

Eles possuem uma dependência muito forte, mas isso não é tão ruim. 

O Kafka pode fazer o que ele intencionalmente tem que saber fazer de melhor, delegando essas demais funcionalidades para quem sabe fazer isso bem, sem precisar reinventar a roda.

### Servidor - Broker

É o próprio Kafka em execução, como ele é distribuído, pode ser uma ou mais instâncias executando em um ou mais servidores.

O Broker é o coração do ecossistema do Kafka. Um Kafka Broker é executado em uma única instância em sua máquina. Um conjunto de Brokers entre diversas máquinas formam um Kafka Cluster.

Uma das principais características do Kafka é a escalabilidade e resiliência que ele oferece. Você pode rodar o Kafka local na sua máquina onde sua própria máquina teria um Kafka Broker formando um Kafka Cluster, como pode subir n instâncias de Kafka Brokers e todas estarem no mesmo Kafka Cluster. Com isso é possível escalar sua aplicação, e replicar os dados entre os Brokers.

<p align="center">
  <img alt="kafka-simple-architecture" src="https://miro.medium.com/max/260/1*kmW0nZSZ_avLJe406rilow.png" width="700px" float="center"/>
</p>

## References

* https://medium.com/@gabrielqueiroz/o-que-%C3%A9-esse-tal-de-apache-kafka-a8f447cac028
* https://medium.com/@cicerojmm/processamento-e-an%C3%A1lise-de-dados-em-tempo-real-com-kafka-e-python-952be439b0fb
* https://kafka.apache.org/intro
* https://kafka.apache.org/uses
* https://www.slideshare.net/CceroMoura1/processamento-e-anlise-de-dados-em-tempo-real-com-python-kafka-e-elasticsearch
* https://pt.slideshare.net/CceroMoura1/processamento-e-anlise-de-dados-em-tempo-real-com-kafka-elasticsearch-e-pyspark