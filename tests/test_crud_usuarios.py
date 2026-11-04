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
                "email": "beltrano+5@qa.com.br",
                "password": "teste",
                "administrador": "true"
            }
        )

        assert response_create.status == 201
        assert response_create.json()['message'] == 'Cadastro realizado com sucesso'       

        user_id = response_create.json()['_id']

        

