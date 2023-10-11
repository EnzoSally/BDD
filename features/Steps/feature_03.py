from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://nubank.com.br/"

@given("que esteja na tela inicial do nubank")
def acessar_site(context):
    context.web.get(base_url)

@when('preencher cpf com valor "{cpf}"')
def step_impl(context, cpf):    
    context.web.find_element(By.ID, "field-cpf").clear()
    context.web.find_element(By.ID, "field-cpf").send_keys(cpf)

    #encontrar o botao form
    btn_continuar = context.web.find_element(By.CSS_SELECTOR, "form button")
    btn_continuar.click()

@then('completar o Cadastro com os valores "{nome}" "{celular}" "{email_01}" "{email_02}"')
def step_impl(context, nome, celular, email_01, email_02):      
    pass