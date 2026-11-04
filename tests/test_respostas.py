from playwright.sync_api import sync_playwright

def test_reposta_detalhada():
    with sync_playwright() as p:
        request_context = p.request.new_context()

        response = request_context.get('https://serverest.dev/usuarios')
    
        assert response.ok

        headers = response.headers 
        assert 'application/json' in headers['content-type']

        body = response.json()
        assert isinstance(body ['usuarios'],list)
        assert isinstance(body ['quantidade'],int)