from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

base_url = "https://nubank.com.br/"

@given("que esteja na tela inicial do nubank")
def acessar_site(context):
    context.web.get(base_url)

@when('preencher cpf com valor "{cpf}"')
def step_impl(context, cpf):    
    context.web.find_element(By.ID, "field-cpf").clear()
    context.web.find_element(By.ID, "field-cpf").send_keys(cpf)

    # Encontrar o botao form
    btn_continuar = context.web.find_element(By.CSS_SELECTOR, "form button")
    btn_continuar.click()

    time.sleep(5)

@then('completar o Cadastro com os valores "{nome}" "{celular}" "{email_01}" "{email_02}"')
def step_impl(context, nome, celular, email_01, email_02):      
    # Vamos preencher o formulário
    # Preenchimento dos campos de texto
    context.web.find_element(By.CSS_SELECTOR, "form input[id=field-name]"). send_keys(nome)
    context.web.find_element(By.CSS_SELECTOR, "form input[id=field-phone]"). send_keys(celular)
    context.web.find_element(By.CSS_SELECTOR, "form input[id=field-email]"). send_keys(email_01)
    context.web.find_element(By.CSS_SELECTOR, "form input[id=field-emailConfirmation]"). send_keys(email_02)

    # marcação dos checkboxes
    context.web.find_element(By.CSS_SELECTOR, "form input[id=field-accepted-whatsapp]").click()
    context.web.find_element(By.CSS_SELECTOR, "form input[id=field-accepted]").click()

    time.sleep(3)