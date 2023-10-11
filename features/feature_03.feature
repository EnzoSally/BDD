# language: pt

Funcionalidade: Cadastro inicial Nubank

Esquema do Cenário: Preenchimento de formulário

    Dado que esteja na tela inicial do nubank
    Quando preencher cpf com valor "<cpf>"
    Então completar o Cadastro com os valores "<nome>" "<celular>" "<email_01>" "<email>"

    Exemplos:
    | cpf            | nome    | celular     | email_1        | email_2        |
    | 580.017.660-47 | Ronaldo | 54999991122 | ronaldo@r9.com | ronaldo@r9.com |