import pytest
from playwright.sync_api import sync_playwright
from page_objects.usuarios import Usuarios

BASE_URL = "https://serverest.dev"
EMAIL_TESTE = "teste2@teste.com"
SENHA_TESTE = "123456"


@pytest.fixture(scope="session")
def api_context():
    """Cria um contexto de API do playwright para ser usado nos testes"""
    print("Criando contexto de API...")
    with sync_playwright() as p:
        request_context = p.request.new_context(base_url=BASE_URL) # Contexto de requisições
        yield request_context # Disponibiliza o contexto para testes
        request_context.dispose() # Fecha o contexto ao final
    print("Contexto de API encerrado.")


@pytest.fixture(scope="session")
def token(api_context):
    """Cria o usuário caso não exista e realiza login para obter token."""

    print(f"Verificando se o usuário '{EMAIL_TESTE}' já existe...")
    response_usuarios = api_context.get("/usuarios") # Lista todos os usuários

    assert response_usuarios.ok, "Falha ao buscar usuários"
    usuarios = response_usuarios.json()["usuarios"]

    if any(u["email"] == EMAIL_TESTE for u in usuarios):
      print("Usuário já existe. Não é necessário criar.")
    else: 
     print("Usuário não existe. Criando usuário...")
     response_create = api_context.post("/usuarios", data={
        "nome": "Aluno Teste12", 
        "email": EMAIL_TESTE, 
        "password": SENHA_TESTE, 
        "administrador": "true"
     })

    # Faz login
    print("Realizando login...")
    response_login = api_context.post("/login", data={
       "email": EMAIL_TESTE, 
       "password": SENHA_TESTE
    })

    assert response_login.ok
    assert response_login.json()["message"] == "Login realizado com sucesso"

    token_str = response_login.json()["authorization"] # Salva token JWT
    print(f"Login realizado com sucesso. Token gerado {token_str[:20]}...")
    return token_str

@pytest.fixture()
def usuario_servico(api_context):
   """Retorna um service já pronto para testes de usuários"""
   return Usuarios(api_context)

 





