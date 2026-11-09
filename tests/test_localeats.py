# Responsavel: Ramon Nogueira.

from playwright.sync_api import expect


def test_local_eats_credenciais_invalidas(page):
    page.goto("https://local-eats-unisenac.vercel.app/", wait_until="domcontentloaded")

    campo_email = page.get_by_placeholder("teste@teste.com")
    campo_senha = page.get_by_placeholder("Sua senha secreta")
    botao_entrar = page.get_by_role("button", name="Entrar", exact=True).last

    expect(campo_email).to_be_visible()
    expect(campo_senha).to_be_visible()

    campo_email.fill("usuario.inexistente@example.com")
    campo_senha.fill("SenhaInvalida123")
    botao_entrar.click()

    mensagem_erro = page.get_by_text("Invalid credentials", exact=True)
    expect(mensagem_erro).to_be_visible()
    expect(mensagem_erro).to_have_text("Invalid credentials")

# Responsavel: Alessandro Reis da Silva.

def test_local_eats_favoritar_e_desfavoritar(page: Page) -> None:
    page.goto("https://local-eats-unisenac.vercel.app/static/index.html")
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    page.get_by_role("textbox", name="teste@teste.com").click()
    page.get_by_role("textbox", name="teste@teste.com").fill("teste3@teste.com")
    page.get_by_role("textbox", name="Sua senha secreta").click()
    page.get_by_role("textbox", name="Sua senha secreta").fill("teste")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    page.get_by_role("link", name="Restaurante Sabor 0").click()
    page.get_by_role("button", name=" Favoritar").click()
    expect(page.locator("#favBtn")).to_contain_text("Favoritado!")
    page.get_by_role("link", name="Meus Favoritos").click()
    page.get_by_role("button", name=" Remover Favorito").click()
    page.get_by_role("link", name="Explorar").click()
    page.get_by_role("link", name="Restaurante Sabor 0").click()
    expect(page.locator("#favBtn")).to_contain_text("Favoritar")