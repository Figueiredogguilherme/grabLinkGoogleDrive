import pandas
import os

loop = True
caminho = os.getcwd()
caminho = caminho.split("\\")
usuario = caminho[2]

while loop == True:

    planilha = {"%":[],"link":[]}

    links = input("Aberte o botão direito do mouse para colar os links: ")
    numero = int(input("Qual o número? "))

    links = links.split(",")
    contagem = (numero*100) + 5
    for linha in links:
        link = linha.split("/d/")
        link = link[1].split("/view?")
        if contagem != ((numero*100) + 100):
            planilha["%"].append(contagem)
        else:
            planilha["%"].append(((numero*100) + 99))
        planilha["link"].append(f"https://drive.google.com/uc?id={link[0]}")
        contagem = contagem + 5

    planilha = pandas.DataFrame.from_dict(planilha)

    try:
        with pandas.ExcelWriter(rf"C:\Users\{usuario}\Desktop\links.xlsx", mode="a",if_sheet_exists="replace") as writer:
            planilha.to_excel(writer, f"{numero}")
    except:
        with pandas.ExcelWriter(rf"C:\Users\{usuario}\Desktop\links.xlsx", mode="w") as writer:
            planilha.to_excel(writer, f"{numero}")

    print("OK")

    parar = input('Digite "S" para parar ou só aperte enter para continuar rodando ')
    if(parar == "S"):
        loop = False