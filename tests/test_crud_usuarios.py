
from page_objects.usuarios import Usuarios


def test_crud_usuarios(api_context):
    service = Usuarios(api_context=api_context)

        # CREATE
    response_create = service.cadastrarUsuario(nome="Fulano da Silva1",
                                               email="beltrano+21@qa.com.br",
                                               password="teste",
                                               administrador="true")

    assert response_create.status == 201
    assert response_create.json()['message'] == 'Cadastro realizado com sucesso' 
    user_id = response_create.json()['_id']


        # READ
    response_read = service.listarUsuario(id_usuario= user_id)

    assert response_read.status == 200
    assert response_read.json()['_id'] == user_id
    assert response_read.json()['email'] == 'beltrano+21@qa.com.br'


        #UPDATE
    response_update = service.editarUsuario(id_usuario= user_id, 
                                            nome = "UP DATE FULANO 3",
                                            email= "beltrano+16@qa.com.br",
                                            password= "teste",
                                            administrador="true")

    assert response_update.status == 200
    assert response_update.json()['message'] == 'Registro alterado com sucesso'

    response_read = service.listarUsuario(id_usuario= user_id)
    assert response_read.status == 200
    assert response_read.json()['email'] == 'beltrano+16@qa.com.br'


        # DELETE
    response_delete = service.deletarUsuario(id_usuario= user_id)

    assert response_delete.status == 200
    assert response_delete.json()['message'] == 'Registro excluído com sucesso'





