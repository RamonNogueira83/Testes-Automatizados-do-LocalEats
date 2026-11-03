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
