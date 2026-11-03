# Atividade 4: Testes Automatizados do LocalEats

## Identificacao

- Unidade Curricular: Qualidade de Software
- Projeto: LocalEats
- Responsavel: Ramon Nogueira
- Modalidade: Individual

## Descricao da atividade

Esta atividade tem como objetivo aplicar testes automatizados a uma regra de negocio de pedidos e a um fluxo funcional do sistema LocalEats. Os testes unitarios utilizam pytest, enquanto o teste funcional utiliza Playwright com Chromium para interagir com o site publicado.

## Regra de negocio escolhida

**Regra 1 - Verificar valor minimo do pedido.**

A funcao recebe o valor de um pedido e considera R$ 30,00 o valor minimo para atendimento. Valores iguais ou superiores a R$ 30,00 retornam `True`; valores menores retornam `False`; valores negativos geram `ValueError`.

## Testes unitarios

| ID | Comportamento verificado | Arquivo | Funcao |
|---|---|---|---|
| TU01 | Pedido que atingiu o valor minimo | tests/test_regras_localeats.py | test_pedido_atinge_valor_minimo |
| TU02 | Pedido abaixo do valor minimo | tests/test_regras_localeats.py | test_pedido_abaixo_do_valor_minimo |
| TU03 | Pedido com valor negativo | tests/test_regras_localeats.py | test_pedido_com_valor_negativo |

A implementacao da regra esta em `src/regras_localeats.py`, na funcao `pedido_atingiu_valor_minimo`.

## TDD de Ramon Nogueira

- **Regra escolhida:** verificar se o pedido atingiu o valor minimo de R$ 30,00.
- **Primeiro teste escrito:** `test_pedido_atinge_valor_minimo`, cobrindo os valores 50 e 30.
- **Por que o teste falhou inicialmente:** como a implementacao nao existia no momento da preparacao do ciclo, o import inicial nao era resolvido; apos a implementacao minima, o teste passou.
- **Implementacao minima realizada:** validacao de valor negativo e comparacao do valor informado com o limite de R$ 30,00.
- **Segundo teste escrito:** `test_pedido_abaixo_do_valor_minimo`.
- **Melhoria ou refatoracao realizada:** centralizacao do limite em `VALOR_MINIMO_PEDIDO` para evitar numeros magicos e manter o criterio reutilizavel.

O historico literal de execucoes TDD anterior nao estava disponivel para registro; somente o ciclo realizado nesta maquina sera registrado pelo pytest apos a execucao.

## Teste funcional

O LocalEats redireciona a raiz para `https://local-eats-unisenac.vercel.app/static/login.html`. A funcionalidade escolhida e uma tentativa de acesso publico com credenciais invalidas, pois nao exige login valido nem dados pessoais. O teste:

1. abre a pagina com `page.goto`;
2. localiza os campos por `get_by_placeholder("teste@teste.com")` e `get_by_placeholder("Sua senha secreta")`;
3. localiza o botao de envio com `get_by_role("button", name="Entrar", exact=True).last`;
4. preenche credenciais inexistentes;
5. envia o formulario;
6. valida que os dois campos ficam visiveis antes da interacao e que a resposta observavel "Invalid credentials" aparece.

| ID | Responsavel | Tipo | Comportamento verificado | Arquivo e funcao |
|---|---|---|---|---|
| TF01 | Ramon Nogueira | Funcional | Acesso com credenciais invalidas e resposta do sistema | tests/test_localeats.py::test_local_eats_credenciais_invalidas |

Os locators foram confirmados pela interface real, nao foram usados nomes ou textos ficticios.

## Tabela geral de responsabilidades

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e funcao |
|---|---|---|---|---|
| TU01 | Ramon Nogueira | Unitario | Pedido atinge valor minimo | tests/test_regras_localeats.py::test_pedido_atinge_valor_minimo |
| TU02 | Ramon Nogueira | Unitario | Pedido abaixo do minimo | tests/test_regras_localeats.py::test_pedido_abaixo_do_valor_minimo |
| TU03 | Ramon Nogueira | Unitario | Pedido negativo | tests/test_regras_localeats.py::test_pedido_com_valor_negativo |
| TF01 | Ramon Nogueira | Funcional | Credenciais invalidas retornam feedback visivel | tests/test_localeats.py::test_local_eats_credenciais_invalidas |

## Uso de inteligencia artificial

- **Ferramenta utilizada:** GitHub Copilot e ChatGPT.
- **Como a ferramenta foi utilizada:** Auxilio na estruturacao do projeto, implementacao de testes automatizados, configuracao do pytest e Playwright e compreensao dos conceitos de TDD.
- **Uma sugestao que precisou ser alterada ou rejeitada:** A sugestao inicial de automatizar a pesquisa de restaurantes foi rejeitada porque essa interface exige navegacao apos autenticacao, e o teste realizado antes da implementacao nao confirmou um estado autenticado publicamente. Foi selecionado o fluxo de credenciais invalidas, que esta visivel e confirmado na pagina publica.
- **Como o codigo sugerido foi verificado:** O codigo sera verificado por execucao com `python -m pytest -v`, e os resultados reais deverao ser analisados. A interface real foi inspecionada por navegador antes da escrita dos locators.

## Comandos de execucao

```powershell
python -m pip install -r requirements.txt
playwright install chromium
python -m pytest -v
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```
