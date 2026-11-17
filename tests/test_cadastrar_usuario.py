import pytest
from helpers.validators import validar_status

@pytest.mark.parametrize(
    "nome, email, password, administrador, status_esperado",
    [
        ("administrador", "teste@tessseeeete5.com", "1234", "true", 201),
        ("", "teste@teste.com", "errado", "false", 400),
        ("user", "", "1234", "false", 400),
    ]
)

def test_cadastrar_usuario(usuario_servico, nome, email, password, administrador, status_esperado):
    response = usuario_servico.cadastrarUsuario (nome=nome,
                                                 email=email,
                                                 password=password,
                                                 administrador=administrador
                                                 )
    validar_status(response,status_esperado)