import pyttsx3
voz = pyttsx3.init()
pergunta = input("Voçê quer que eu fale? (sim/não)")
if pergunta == "sim" or "Sim" or "SIM":
    texto = input("O que voçê quer que eu fale?")
    voz.say(texto)
    voz.runAndWait()
else:
    print("Fim do programa")
