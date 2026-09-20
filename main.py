import pyttsx3
voz = pyttsx3.init()
pergunta = input("Você quer que eu fale? (sim/não): ").lower()
if pergunta == "sim":
    texto = input("O que voçê quer que eu fale?")
    voz.say(texto)
    voz.runAndWait()
else:
    print("Fim do programa")
