from behave import given, when, then

base_url = "https://www.atitus.edu.br/"

@when("eu acesso a página principaç")
def acessar_site(context):
    context.web.get(base_url)

@then("deve ser mostrado um banner sobre vestibular")
def banner_vestibular(context):
    pass