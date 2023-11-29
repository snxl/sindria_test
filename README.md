para rodar o projeto é necessário

transformar o .env.example em .env

````shell
cp .env.example .env
````

gerar uma chave de api na open ai e colocar em

````env
OPENAI_API_KEY="your key here"
````

ter em sua maquina docker e docker-compose instalados.

para executar basta rodar

````shell
docker-compose up -d --build
````

para ver os logs da aplicação

````shell
docker-compose logs -f app
````

para ver a documentação de rotas acesse

<http://127.0.0.1:5000/api-docs>