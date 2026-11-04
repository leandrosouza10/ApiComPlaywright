from playwright.sync_api import sync_playwright

def test_listar_usuarios():
    with sync_playwright() as p:
        request_context = p.request.new_context()

        response = request_context.get('https://serverest.dev/usuarios')


        # Valida se resposta é 200 
        assert response.status == 200


        # Valida se retorna um json
        data = response.json()
        assert "usuarios" in data


        print("\nQuantidade de usuários:", len(data["usuarios"]))

