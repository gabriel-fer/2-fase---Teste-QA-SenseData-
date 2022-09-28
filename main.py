import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By



class TesteSwaglabs:
    def __init__(self,user,password,first_name,last_name,CEP):
        
        
        self.user = user
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.CEP = CEP

    def iniciar_teste(self):
        self.driver =webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.fazer_login()
        self.filtrar_preco()
        self.add_carrinho()
        self.finalizar_compra()
        print("O navegador foi aberto corretamente")

    
    def fazer_login(self):
        username = self.driver.find_element(By.XPATH,'//*[@id="user-name"]')
        password = self.driver.find_element(By.XPATH,'//*[@id="password"]')
        username.send_keys(self.user)
        password.send_keys(self.password)
        login = self.driver.find_element(By.XPATH,'//*[@id="login-button"]')
        login.click()
        print("foi feito login com sucesso")
        print(self.user)
    
    def filtrar_preco(self):
        filtro = self.driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/div[2]/span/select')
        filtro.click()
        menor_p_maior = self.driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/div[2]/span/select/option[3]')
        menor_p_maior.click()
        print("O filtro foi ativado")
    
    def add_carrinho(self):
        item1 = self.driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-onesie"]')
        item1.click()
        item2 = self.driver.find_element(By.XPATH,'//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
        item2.click()
        carrinho = self.driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
        carrinho.click()
        print("os produtos foram adiconado ao carrinho")
    
    def finalizar_compra(self):

        finalizar_compra = self.driver.find_element(By.XPATH,'//*[@id="checkout"]')
        finalizar_compra.click()

        primeiro_nome = self.driver.find_element(By.XPATH,'//*[@id="first-name"]')
        primeiro_nome.send_keys(self.first_name)

        sobrenome = self.driver.find_element(By.XPATH,'//*[@id="last-name"]')
        sobrenome.send_keys(self.last_name)

        cep = self.driver.find_element(By.XPATH,'//*[@id="postal-code"]')
        cep.send_keys(self.CEP)

        continuar = self.driver.find_element(By.XPATH,'//*[@id="continue"]')
        continuar.click()

        finalizar = self.driver.find_element(By.XPATH,'//*[@id="finish"]')
        finalizar.click()
        print("a compra foi finalizada com sucesso")
        time.sleep(2)
        self.driver.close()
        self.driver.quit()
    


class TesteUser:
    def multiplos_usuarios(self):
        with open("user.json",encoding='utf-8') as meus_usuarios:
            dados = json.load(meus_usuarios)


        for i in dados:
            iniciar = TesteSwaglabs(i["user"],i["password"], i["CEP"],i["last_name"],i["CEP"])
            iniciar.iniciar_teste()

    def usuario_manual(self):
        print("""
        ATENÇÃO ALGUNS USUÁRIOS PODEM APRESENTAR FALHA AO TENTAR FAZER LOGIN. NESSE CASO ENCERRE 
        O SCRIPT E EXECUTE COM OUTRO USUÁRIO.NÃO ESQUEÇA DE RELATAR QUAL USUÁRIO E QUAL FALHA OCORREU
        Usuários válidos:  
        """)
        with open("user.json",encoding='utf-8') as meus_usuarios:
            dados = json.load(meus_usuarios)

        for i in dados:
            print(i['user'])



        user = input("Digite um usuário válido: ")
        password = input("Digite uma senha válida: ")
        first_name = input("Digite o primeiro nome:  ")
        last_name = input("Digite o sobrenome: ")
        CEP = input("Digite um CEP válido: ")


        iniciar = TesteSwaglabs(user,password,first_name,last_name,CEP)
        iniciar.iniciar_teste()    


while True:
    print("""
    Bem vindo ao teste de QA. Escolha uma das opções a seguir:
    Digite 1 para testar todos os usuários armazenados
    Digite 2 para testar um usuário manualmente
    Digite 3 para encerrar o programa
    """)

    opc = int(input(">>>"))
    start = TesteUser()

    if opc == 1:
        start.multiplos_usuarios()
    elif opc == 2:
        start.usuario_manual()
    elif opc == 3:
        print("Encerrando...")
        break
    else:
        print("Escolha uma opção válida")
