from helpers.validators import validar_status
from page_objects.usuarios import Usuarios

def test_cadastro_usuario_sem_nome (api_context):
    """Exemplo de validação de status e mensagem de erro."""
    service = Usuarios(api_context)

    response = service.cadastrarUsuario (nome="",
                                         email ="teste@test54545e.com.br", 
                                         password = "123456",
                                         administrador = "true")
    validar_status(response, 400)
    body = response.json()
    assert body ["nome"] == "nome não pode ficar em branco"


def test_cadastrar_usuario_sem_email (api_context):
    service = Usuarios(api_context)

    response = service.cadastrarUsuario (nome="Fulano de Tal",
                                         email="",
                                         password="123456",
                                         administrador= "false"
                                         )

    validar_status (response, 400)
    body = response.json()
    assert body ["email"] == "email não pode ficar em branco"

def test_cadastrar_usuario_com_email_invalido (api_context):
    service = Usuarios(api_context)

    response = service.cadastrarUsuario (nome="Fulano de Tal",
                                         email="teste@com.br",
                                         password="123456",
                                         administrador= "false"
                                         )

    validar_status (response, 400)
    body = response.json()
    assert body ["email"] == "email deve ser um email válido"

def test_cadastrar_usuario_sem_password (api_context):
    service = Usuarios(api_context)

    response = service.cadastrarUsuario (nome="Fulano de Tal",
                                         email="teste@test54545e.com.br",
                                         password="",
                                         administrador= "false"
                                         )

    validar_status (response, 400)
    body = response.json()
    assert body ["password"] == "password não pode ficar em branco"

def test_cadastrar_usuario_sem_administrador (api_context):
    service = Usuarios(api_context)

    response = service.cadastrarUsuario (nome="Fulano de Tal",
                                         email="teste@test54545e.com.br",
                                         password="123",
                                         administrador= ""
                                         )

    validar_status (response, 400)
    body = response.json()
    assert body ["administrador"] == "administrador deve ser 'true' ou 'false'"