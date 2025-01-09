# 📑 Mini Blog

Este é um projeto de um mini blog desenvolvido com Django.
O objetivo deste projeto é criar um blog simples onde os usuários podem criar, editar e deletar posts.

## ⚙️ Instruções para rodar o projeto localmente 

### Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)
- virtualenv (opcional)

### Instalação

1. Clone o repositório para o seu ambiente local:
```
git clone https://github.com/ingrlopes/mini_blog.git
cd mini_blog
```

2. Crie um ambiente virtual:
```
python -m venv env
source env/bin/activate
no Windows, use `env\Scripts\activate`
```

3. Instale as dependências do projeto:
```
pip install -r requirements.txt
```

4. Realize as migrações do banco de dados:
```
python manage.py makemigrations
python manage.py migrate
```

5. Crie um superusuário para acessar o admin do Django:
```
python manage.py createsuperuser
```

6. Inicie o servidor de desenvolvimento:
```
python manage.py runserver
```

7. Acesse o projeto no navegador:
```
http://127.0.0.1:8000/
```

## 🔍 Decisões técnicas relevantes

#### Django
>Utilizei o Django como framework principal devido à sua robustez e facilidade de uso para desenvolvimento rápido de aplicações web.

#### SQLite
>Utilizei o SQLite como banco de dados para simplificar a configuração e o desenvolvimento local.

#### Bootstrap
>Utilizei classes de estilo do Bootstrap para estilizar os botões e garantir uma aparência consistente e responsiva.


## ✏️ Resumo do que foi implementado

#### CRUD de Posts
>Implementação das funcionalidades de criação, leitura, atualização e deleção de posts.

#### Autenticação
>Utilização do sistema de autenticação do Django para proteger as rotas de criação, edição e deleção de posts.

#### Templates
>Criação de templates para listar posts, exibir detalhes de um post, criar e editar posts, e confirmar a deleção de um post.

#### Estilização
>Utilização de CSS para estilizar os templates e garantir uma aparência agradável e consistente.


## 💡 Aprendizados para o futuro

### Melhoria na UI/UX
- Investir mais tempo na melhoria da interface do usuário e na experiência do usuário, utilizando frameworks de frontend mais avançados como React ou Vue.js.

### Testes automatizados
- Implementar testes automatizados para garantir a qualidade do código e facilitar a manutenção do projeto.

### Desempenho e escalabilidade
- Considerar o uso de bancos de dados mais robustos como PostgreSQL e otimizações de desempenho para suportar um maior número de usuários e posts.

---
Ingrid Lopes © 2025