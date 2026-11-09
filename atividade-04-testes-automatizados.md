# Atividade 4: Testes Automatizados do LocalEats

## Identificacao

- Unidade Curricular: Qualidade de Software
- Projeto: LocalEats
- Responsavel: Ramon Nogueira e Alessandro Reis da Silva
- Modalidade: Dupla

## Descricao da atividade

Esta atividade tem como objetivo aplicar testes automatizados a uma regra de negocio de pedidos e a um fluxo funcional do sistema LocalEats. Os testes unitarios utilizam pytest, enquanto o teste funcional utiliza Playwright com Chromium para interagir com o site publicado.

## Regra de negocio escolhida

**Regra 1 - Verificar valor minimo do pedido.**

A funcao recebe o valor de um pedido e considera R$ 30,00 o valor minimo para atendimento. Valores iguais ou superiores a R$ 30,00 retornam `True`; valores menores retornam `False`; valores negativos geram `ValueError`.


**Regra 3 - Validar quantidade de itens.**

A funcao recebe o valor de quantidade de itens e considera menor que 10 ou igual a 10 ou maior que 1 ou igual a 1 retornam `True`; valores menores retornam `False`; valores negativos geram `ValueError`.

## Testes unitarios

| ID | Comportamento verificado | Arquivo | Funcao |
|---|---|---|---|
| TU01 | Pedido que atingiu o valor minimo | tests/test_regras_localeats.py | test_pedido_atinge_valor_minimo |
| TU02 | Pedido abaixo do valor minimo | tests/test_regras_localeats.py | test_pedido_abaixo_do_valor_minimo |
| TU03 | Pedido com valor negativo | tests/test_regras_localeats.py | test_pedido_com_valor_negativo |
| TU04 | Quatidade de itens permitidos | tests/test_regras_localeats.py | test_quatidade_de_itens_permitidos |
| TU05 | Quatidade de itens acima do permitido | tests/test_regras_localeats.py | test_quatidade_de_itens_acima_do_permitido |
| TU06 | Quatidade de itens igual a zero | tests/test_regras_localeats.py | test_quatidade_de_itens_igual_a_zero |
| TU07 | Quatidade de itens negativos | tests/test_regras_localeats.py | test_quatidade_de_itens_negativos |

A implementacao da regra esta em `src/regras_localeats.py`, na funcao `pedido_atingiu_valor_minimo`.

## TDD de Ramon Nogueira

- **Regra escolhida:** verificar se o pedido atingiu o valor minimo de R$ 30,00.
- **Primeiro teste escrito:** `test_pedido_atinge_valor_minimo`, cobrindo os valores 50 e 30.
- **Por que o teste falhou inicialmente:** como a implementacao nao existia no momento da preparacao do ciclo, o import inicial nao era resolvido; apos a implementacao minima, o teste passou.
- **Implementacao minima realizada:** validacao de valor negativo e comparacao do valor informado com o limite de R$ 30,00.
- **Segundo teste escrito:** `test_pedido_abaixo_do_valor_minimo`.
- **Melhoria ou refatoracao realizada:** centralizacao do limite em `VALOR_MINIMO_PEDIDO` para evitar numeros magicos e manter o criterio reutilizavel.

O historico literal de execucoes TDD anterior nao estava disponivel para registro; somente o ciclo realizado nesta maquina sera registrado pelo pytest apos a execucao.

## TDD de Alessandro Reis da Silva

- **Regra escolhida:** Validar quantidadde de itens.
- **Primeiro teste escrito:** `test_quatidade_de_itens_permitidos`, cobrindo os valores da quantidade de itens 10, 5 e 1.
- **Por que o teste falhou inicialmente:** Os símbolos de maior ou menor a igual estavam invertidos, o que causava erro na hora de comparar o valor e o programa ditar que é válido ou não.
- **Implementacao minima realizada:** Correção dos símbolos de maior ou menor a igual na comparação e a implementação de erro ao usar valores negativos.
- **Segundo teste escrito:** `test_quatidade_de_itens_acima_do_permitido`.
- **Melhoria ou refatoracao realizada:** Não tem nada para melhorar pois o código é bem simples e de facil leitura.

O historico literal de execucoes TDD anterior nao estava disponivel para registro; somente o ciclo realizado nesta maquina sera registrado pelo pytest apos a execucao.

## Teste funcional

## Ramon Noqueira
O LocalEats redireciona a raiz para `https://local-eats-unisenac.vercel.app/static/login.html`. A funcionalidade escolhida e uma tentativa de acesso publico com credenciais invalidas, pois nao exige login valido nem dados pessoais. O teste:

1. abre a pagina com `page.goto`;
2. localiza os campos por `get_by_placeholder("teste@teste.com")` e `get_by_placeholder("Sua senha secreta")`;
3. localiza o botao de envio com `get_by_role("button", name="Entrar", exact=True).last`;
4. preenche credenciais inexistentes;
5. envia o formulario;
6. valida que os dois campos ficam visiveis antes da interacao e que a resposta observavel "Invalid credentials" aparece.

## Alessandro Reis da Silva
A funcionalidade escolhida do local eats é de favoritar e desfavoritar, quando inicia o teste, vai para o endereço `https://local-eats-unisenac.vercel.app/static/login.html`.
1. abre a pagina com `page.goto`;
2. localiza os campos por `get_by_role("textbox", name="teste@teste.com")` e `get_by_role("textbox", name="Sua senha secreta")`;
3. localiza o botao de envio com `get_by_role("button", name="Entrar", exact=True).last`;
4. preenche as informações do formulario;
5. envia o formulario para acessar a conta;
6. localiza e interage com `get_by_role("link", name="Restaurante Sabor 0")`;
7. localiza e interage com `get_by_role("button", name=" Favoritar").click()` para favoritar;
8. localiza e analiza o `expect(page.locator("#favBtn")).to_contain_text("Favoritado!")` para confirmar que está favoritado;
9. localiza e interage com `get_by_role("link", name="Meus Favoritos").click()` para ir as meus favoritos;
10. localiza e interage com `get_by_role("button", name=" Remover Favorito")` para remover do ravorito o Restaurante Sabor 0;
11. localiza e interage com `get_by_role("link", name="Explorar").click()` para ir nas visualizações dos restaurantes;
12. localiza e interage com `get_by_role("link", name="Restaurante Sabor 0")`;
13. localiza e analiza o `expect(page.locator("#favBtn")).to_contain_text("Favoritar")` para confirmar que não está mais favoritado; 

| ID | Responsavel | Tipo | Comportamento verificado | Arquivo e funcao |
|---|---|---|---|---|
| TF01 | Ramon Nogueira | Funcional | Acesso com credenciais invalidas e resposta do sistema | tests/test_localeats.py::test_local_eats_credenciais_invalidas |
| TF02 | Alessandro Reis da Silva | Funcional | Favoritar e desfavoritar | tests/test_localeats.py::test_local_eats_favoritar_e_desfavoritar |

Os locators foram confirmados pela interface real, nao foram usados nomes ou textos ficticios.

## Tabela geral de responsabilidades

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e funcao |
|---|---|---|---|---|
| TU01 | Ramon Nogueira | Unitario | Pedido atinge valor minimo | tests/test_regras_localeats.py::test_pedido_atinge_valor_minimo |
| TU02 | Ramon Nogueira | Unitario | Pedido abaixo do minimo | tests/test_regras_localeats.py::test_pedido_abaixo_do_valor_minimo |
| TU03 | Ramon Nogueira | Unitario | Pedido negativo | tests/test_regras_localeats.py::test_pedido_com_valor_negativo |
| TF01 | Ramon Nogueira | Funcional | Credenciais invalidas retornam feedback visivel | tests/test_localeats.py::test_local_eats_credenciais_invalidas |
| TU04 | Alessandro Reis da Silva | Unitario | Quatidade de itens permitidos | tests/test_regras_localeats.py.py::test_quatidade_de_itens_permitidos |
| TU05 | Alessandro Reis da Silva | Unitario | Quatidade de itens acima do permitido | tests/test_regras_localeats.py.py::test_quatidade_de_itens_acima_do_permitido |
| TU06 | Alessandro Reis da Silva | Unitario | Quatidade de itens igual a zero | tests/test_regras_localeats.py.py::test_quatidade_de_itens_igual_a_zero |
| TU07 | Alessandro Reis da Silva | Unitario | Quatidade de itens negativos | tests/test_regras_localeats.py.py::test_quatidade_de_itens_negativos |
| TF02 | Alessandro Reis da Silva | Funcional | Favoritar e desfavoritar | tests/test_localeats.py::test_local_eats_favoritar_e_desfavoritar |


## Uso de inteligencia artificial

- **Ferramenta utilizada:** GitHub Copilot, ChatGPT, languagetool.
- **Como a ferramenta foi utilizada:** Auxilio na estruturacao do projeto, implementacao de testes automatizados, configuracao do pytest e Playwright, compreensao dos conceitos de TDD e correção de texto.
- **Uma sugestao que precisou ser alterada ou rejeitada:** A sugestao inicial de automatizar a pesquisa de restaurantes foi rejeitada porque essa interface exige navegacao apos autenticacao, e o teste realizado antes da implementacao nao confirmou um estado autenticado publicamente. Foi selecionado o fluxo de credenciais invalidas, que esta visivel e confirmado na pagina publica.
- **Como o codigo sugerido foi verificado:** O codigo sera verificado por execucao com `python -m pytest -v`, e os resultados reais deverao ser analisados. A interface real foi inspecionada por navegador antes da escrita dos locators.

## Comandos de execucao

```powershell
python -m pip install -r requirements.txt
playwright install chromium
python -m pytest -v
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```
