import time as t
import pyautogui as py

# nessa automatização foi utilizado o tratamento de imagem para localizar as coisas na tela na hora do cadastro.
t.sleep(1)
# abre o site
py.hotkey("win", "r")
py.typewrite("https://www.gabrielcasemiro.com.br/atividade_pyautogui/")
py.press("enter")

t.sleep(2)
# abre o arquivo e salva a variavel que foi definida.
# O FOR TEM Q SER DENTRO DO WITH PARA NAO DAR ERRO.
with open("membros.csv") as f:
    next(f)
# faz o tratamento da linhas do arquivo csv.
    for line in f:
        line = line.strip()
        line = line.split(";")

        # cada variavel esta recendo oq est escrito nas linhas do documento csv.
        nome = line[0]
        sexo = line[1]
        email = line[2]
        tel = line[3]
        # esta parte faz o tratamento de imagem e localiza os campos na tela, e vai digitar na velocidade escolhida.
        py.click(py.locateCenterOnScreen(
            r"C:\Users\mathe\Desktop\imagem\campo_nome.png", confidence=0.8), duration=1)
        py.typewrite(nome, interval=0.15)

        py.click(py.locateCenterOnScreen(
            r"C:\Users\mathe\Desktop\imagem\campo_email.png", confidence=0.8), duration=1)
        py.typewrite(email, interval=0.15)

        py.click(py.locateCenterOnScreen(
            r"C:\Users\mathe\Desktop\imagem\telefone.png", confidence=0.8), duration=1)
        py.typewrite(tel, interval=0.15)

        py.click(py.locateCenterOnScreen(
            r"C:\Users\mathe\Desktop\imagem\campo_sexo.png", confidence=0.8), duration=1)
        # teste logico para escolher masculino e feminino com base nas imagensa gravadas da tela.
        if sexo == "Masculino":
            py.click(py.locateCenterOnScreen(
                r"C:\Users\mathe\Desktop\imagem\Masculino.png", confidence=0.8), duration=1)
        else:
            py.click(py.locateCenterOnScreen(
                r"C:\Users\mathe\Desktop\imagem\Feminino.png", confidence=0.8), duration=1)

        py.click(py.locateCenterOnScreen(
            r"C:\Users\mathe\Desktop\imagem\cadastrar.png", confidence=0.8), duration=1)

# aviso de programa finalizado

py.alert(text="prorama finalzado com sucesso!", title="Aviso de conclusão")