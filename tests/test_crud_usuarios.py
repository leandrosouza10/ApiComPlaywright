from playwright.sync_api  import sync_playwright

URL_BASE = 'https://serverest.dev/usuarios'

def test_crud_usuarios():
    with sync_playwright() as p:
        request_context = p.request.new_context()

        # CREATE

        response_create = request_context.post(
            URL_BASE,
            data = {
                "nome": "Fulano da Silva",
                "email": "beltrano+11@qa.com.br",
                "password": "teste",
                "administrador": "true"
            }
        )

        assert response_create.status == 201
        assert response_create.json()['message'] == 'Cadastro realizado com sucesso'       

        user_id = response_create.json()['_id']


        # READ

        response_read = request_context.get(f"{URL_BASE}/{user_id}")
        assert response_read.status == 200
        assert response_read.json()['_id'] == user_id
        assert response_read.json()['email'] == 'beltrano+11@qa.com.br'

        #UPDATE

        response_update = request_context.put(f"{URL_BASE}/{user_id}",
        data = {
                "nome": "UP DATE FULANO 1",
                "email": "beltrano+12@qa.com.br",
                "password": "teste",
                "administrador": "true"
            })

        assert response_update.status == 200
        assert response_update.json()['message'] == 'Registro alterado com sucesso'

        response_read = request_context.get(f"{URL_BASE}/{user_id}")
        assert response_read.status == 200
        assert response_read.json()['email'] == 'beltrano+12@qa.com.br'


        # DELETE

        response_delete =request_context.delete (f"{URL_BASE}/{user_id}")

        assert response_delete.status == 200
        assert response_delete.json()['message'] == 'Registro excluído com sucesso'






