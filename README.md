# Projeto de Matrícula

Este é um projeto simples desenvolvido em Django para gerenciar matrículas de alunos.

## Requisitos

- Python 3.11
- Django 5.2.6

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd matricula
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Executar

1. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

2. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

3. Acesse o projeto no navegador em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

