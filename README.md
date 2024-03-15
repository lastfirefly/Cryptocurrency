<h1 align="center"> Cryptocurrency - Projeto Módulo 5 </h1>


<h1 align="center"> :part_alternation_mark: Visão Geral :chart_with_upwards_trend: </h1>

<p align="center">
<img src="https://img.shields.io/static/v1?label=License&message=Apache&color=green&style=for-the-badge"/>
<img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/>
</p>
<h1 align="center"> Criptomoedas utilizadas </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Bitcoin-000?style=for-the-badge&logo=bitcoin&logoColor=white" alt="Bitcoin">
  <img src="https://img.shields.io/badge/Binance-FCD535?style=for-the-badge&logo=binance&logoColor=white" alt="Binance">
  <img src="https://img.shields.io/badge/Cardano-ADA?style=for-the-badge&logo=cardano&logoColor=white" alt="Cardano">
  <img src="https://img.shields.io/badge/Dogecoin-B59A30?style=for-the-badge&logo=dogecoin&logoColor=white" alt="Dogecoin">
  <img src="https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=ethereum&logoColor=white" alt="Ethereum">
  <img src="https://img.shields.io/badge/Polkadot-E6007A?style=for-the-badge&logo=polkadot&logoColor=white" alt="Polkadot">
  <img src="https://img.shields.io/badge/Tether-168363?style=for-the-badge&logo=tether&logoColor=white" alt="Tether">
  <img src="https://img.shields.io/badge/Uniswap-000?style=for-the-badge&logo=uniswap&logoColor=white" alt="Uniswap">
  <img src="https://img.shields.io/badge/USD Coin-2775CA?style=for-the-badge&logo=usdc&logoColor=white" alt="USD Coin">
  <img src="https://img.shields.io/badge/XRP-000?style=for-the-badge&logo=xrp&logoColor=white" alt="XRP">
</p>

# Projeto de Criptomoedas

Este repositório é destinado à criação do último projeto em grupo referente ao módulo 5 do curso **Formação em Análise de Dados** do **Senac + Resilia**.

### Objetivo

O objetivo deste projeto é explorar e analisar dados relacionados a criptomoedas, incluindo informações sobre preços, volumes de negociação, tendências e outras métricas relevantes, fazendo um ETL e um EDA.

### Ferramentas e Linguagens Utilizadas

<table border="0">
 <tr>
    <td><b style="font-size:30px"> Linguagens</b></td>
    <td><b style="font-size:30px"> Bibliotecas Python </b></td>
 </tr>
 <tr>
    <td>
      <ul>
        <li>Python</li>
        <li>Google Colab</li>
        <li>Markdown</li>
        <li>HTML</li>
        <li>MySQL</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Pandas</li>
        <li>NumPy</li>
        <li>Matplotlib</li>
        <li>Seaborn</li>
        <li>Scipy</li>
        <li>mysql_connector</li>
        <li>session_info</li>
      </ul>
    </td>
 </tr>
</table>


### Conteúdo

- `data/`: Diretório contendo os dados brutos das criptomoedas.
- `database/`: Diretório para armazenar arquivos relacionados ao banco de dados.
- `notebooks/`: Notebooks Jupyter com análises exploratórias e visualizações.
- `scripts/`: Scripts Python para processamento e limpeza dos dados.
- `archives/`: Arquivos extras essenciais para apresentação do projeto.

### Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* ou enviar *pull requests*.

### Autores

Este projeto é mantido por:

- [Luigi Maciel](https://github.com/LuigiPereira1709);

- [Beatriz Miranda](https://github.com/lastfirefly%29);

- [Ilma Gonçalves](https://github.com/estrela1921);

- [Debora Jansen](https://github.com/DeboraJansen95)



### 📁 Acesso ao projeto
Você pode acessar os arquivos do projeto clicando [aqui](https://github.com/lastfirefly/Cryptocurrency).

### 📃 Licença

Este projeto está licenciado sob a Licença Apache - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.



## Sobre o projeto
- Em grupo (squads);
- Obrigatório;
- Entregue via link no Portal;
- Entregue na aula final;
- Apresentado em grupo na aula final (15 min);
- Correção feita pela Facilitação por meio de rubricas com conceito como nota.


Esse é um projeto integrador, em que vocês vão utilizar todas as ferramentas e conhecimentos trabalhados ao longo do curso.  

### Contexto

***Criptomoedas são moedas digitais descentralizadas baseadas em criptografia, que 
operam em uma rede blockchain que permite transações seguras e transparentes 
sem a necessidade de intermediários, como bancos. Elas fazem parte do mundo 
digital, afetam a economia atual e são consideradas altamente voláteis.
Por isso, você e seu squad foram escalados por uma corretora financeira para 
realizar uma análise exploratória relacionada à série histórica dos valores de
criptomoedas.***

### O que é pra fazer?

Realizar uma análise exploratória histórica dos valores de
criptomoedas.
As fontes de dados que serão utilizadas no projeto estão 
disponíveis no [Kaggle](https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory/data?select=coin_Aave.csv). 

### Como fazer? 

#### Detalhes do projeto
A análise deverá responder às seguintes perguntas:
1. Como se comportaram os valores para todas as criptomoedas? Os valores tiveram uma 
tendência de queda ou de aumento?
2. Quais os valores médios para todas as criptomoedas?
3. Em quais anos houve maiores quedas e valorizações?
4. Existe alguma tendência de aumento ou queda dos valores pelo dia da semana?
5. Qual moeda se mostra mais interessante em relação à valorização pela análise da série 
histórica?
6. Qual moeda se mostra menos interessante em relação à valorização pela análise da série 
histórica?
7. Existe correlação entre os valores para todas as criptomoedas?

### Requisitos
- [x] Utilizar, VS Code, Jupyter Notebook ou Colab;

- [x] Realizar a limpeza dos dados;

- [x] Realizar análise exploratória;

- [x] Exportar os arquivos resultantes para um banco de dados (ex.: Postgres ou MySQL);

- [x] Fazer a conexão do banco de dados com a ferramenta de visualização de dados (Tableau, Power Bi ou Looker);

- [x] Escolher 10 criptomoedas, do conjunto disponibilizado, que serão utilizadas por vocês nesse projeto.

- [x] Gerar, no mínimo, cinco (5) gráficos para a apresentação dos resultados;

- [x] Focar no storytelling para criar a apresentação;

- [x] Responder cada uma das perguntas com a visualização mais adequada;

- [x] O notebook utilizado na análise deve estar organizado, com descrições do passo a passo da análise em markdown, apresentação dos resultados e insights gerados;

- [x] Levantar mais duas (2) perguntas e respondê-las da forma que achar mais adequada;
      
- [x] O projeto desenvolvido deverá ser disponibilizado em repositório no GitHub;
      
- [ ] O projeto precisa possuir uma evidência de entrega, ou seja, um pequeno parágrafo com uma explicação do que foi feito no projeto e a defesa das escolhas tomadas
