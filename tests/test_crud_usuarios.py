
from page_objects.usuarios import Usuarios
from helpers.validators import validar_status, validar_mensagem_json


def test_crud_usuarios(api_context):
    service = Usuarios(api_context=api_context)

        # CREATE
    response_create = service.cadastrarUsuario(nome="Fulano da Silva1",
                                               email="beltrano+22@qa.com.br",
                                               password="teste",
                                               administrador="true")

    validar_status (response_create, 201)
    validar_mensagem_json(response_create, "Cadastro realizado com sucesso" )  
    user_id = response_create.json()['_id']


        # READ
    response_read = service.listarUsuario(id_usuario= user_id)

    validar_status (response_read,200)   
    assert response_read.json()['_id'] == user_id
    assert response_read.json()['email'] == 'beltrano+22@qa.com.br'


        #UPDATE
    response_update = service.editarUsuario(id_usuario= user_id, 
                                            nome = "UP DATE FULANO 3",
                                            email= "beltrano+16@qa.com.br",
                                            password= "teste",
                                            administrador="true")

    validar_status (response_update, 200)
    validar_mensagem_json (response_update, 'Registro alterado com sucesso' )
    

    response_read = service.listarUsuario(id_usuario= user_id)
    validar_status (response_read, 200)    
    assert response_read.json()['email'] == 'beltrano+16@qa.com.br'


        # DELETE
    response_delete = service.deletarUsuario(id_usuario= user_id)

    validar_status (response_delete, 200)
    validar_mensagem_json (response_delete,'Registro excluído com sucesso' )
    





