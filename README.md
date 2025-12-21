Exemplo de JSON de Cliente

json { "nome": "João Silva", "email": " joao.silva@example.com ", "cidade": "São Paulo", "estado": "SP" }

Clone o repositório: git clone https://github.com/seu-usuario/seu-repositorio.git cd api_clientes

Crie o ambiente virtual (opcional, mas recomendado): python -m venv venv source venv/bin/activate # Linux / Mac venv\Scripts\activate # Windows

Instale as dependências: pip install -r requisitos.txt

Realize as migrações: python manager.py migrar

Rodou o servidor local: python manage.py runserver

Testando a API Acesse no navegador ou use ferramentas como Postman, Insomnia ou cURL: http://localhost:8000/api/clientes/

Exemplo de busca por cidade: http://localhost:8000/api/clientes/?search=São Paulo

Estrutura de Pastas (MVC)

api_clientes/ ├── api_clientes/ # Configurações gerais (urls, configurações) ├── clientes/ # Módulo de Clientes (Modelos, Views, Serializadores, URLs) ├── db.sqlite3 # Banco de dados local (SQLite) ├── manage.py ├── requisitos.txt └── README.md

Melhores Futuras:

Autenticação via JWT

Implantar em ambiente Cloud (ex: AWS, Heroku)

Paginação de resultados

Testes unitários automatizados

Versionamento da API (ex: v1, v2)

Desenvolvido por: Alex Sander Francis de Oliveira Bootcamp Arquiteto(a) de Software - XP Educação | Dezembro/2025
