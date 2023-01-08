# Desafio 1 - Backend

Este desafio é a implementação de uma *webservice* que retorna dados dos estabelecimentos de saúde vinculados ao SUS, tais como nome e localização (latitude e longitude).

___
## Instruções 
Para rodar o projeto é necessário o **python 3.10.6**.

Execute os comandos abaixo:
* Instalação das dependências

```
 $ pip3 install -r requirements.txt
```
* Executar *webservice*

```
$ uvicorn main:app --reload
```
**Obs:** caso esteja usando algum ambiente virtual, por exemplo *virtual env*, certifique-se de rodar o binário do *uvicorn* correspondente ao seu ambiente.

## Edpoints

**Listar estabelecimentos por municípios: /estabelecimentos/listar/{id_município} [GET]**

O id recebido pelo parâmetro corresponde ao código identificador do município, onde se localiza o estabelecimento nos sistemas do SUS. Retorna um *JSON* com uma lista de objetos, em que cada objeto contém as informações (código CNES, nome, latitude e longitude) de um estabelecimeto de saúde localizado no município solicitado.


**Obter estabelecimento por id: /estabelecimento/{id_cnes} [GET]**

Recebe como parâmetro um valor correspondente ao código identificador do estabelecimento no Cadastro Nacional de Estabelecimentos de Saúde, e retorna um *JSON* contendo unicamente um objeto com as informações (código CNES, nome, latitude e longitude) do estabelecimento solicitado.