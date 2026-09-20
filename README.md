# 🔊 Text Speaker

Um pequeno aplicativo em Python capaz de **transformar textos digitados pelo usuário em fala** utilizando a biblioteca `pyttsx3`.

## 📌 Sobre o projeto

O **Text Speaker** permite que o usuário informe se deseja utilizar a função de voz e, em seguida, digite o texto que deseja ouvir.

O projeto utiliza o mecanismo de síntese de voz disponível no computador para reproduzir o conteúdo informado.

## ⚙️ Funcionalidades

* 🔊 Conversão de texto em fala
* ⌨️ Entrada de texto pelo usuário
* ✅ Confirmação para iniciar a leitura
* 🔡 Tratamento da resposta com `.lower()`
* 📴 Encerramento do programa quando a função de voz não é solicitada

## 🛠️ Tecnologias

* **Python**
* **pyttsx3**

## 📦 Instalação

Instale a dependência necessária:

```bash
pip install pyttsx3
```

## ▶️ Execução

Execute o arquivo Python:

```bash
python main.py
```

O programa solicitará:

```text
Você quer que eu fale? (sim/não):
```

Caso o usuário confirme, será solicitado o texto:

```text
O que você quer que eu fale?
```

O texto será então reproduzido através da síntese de voz.

## 💻 Código

```python
import pyttsx3

voz = pyttsx3.init()

pergunta = input("Você quer que eu fale? (sim/não): ").lower()

if pergunta == "sim":

    texto = input("O que você quer que eu fale? ")

    voz.say(texto)
    voz.runAndWait()

else:

    print("Fim do programa")
```

## 🔊 Funcionamento da síntese de voz

O projeto utiliza três operações principais do `pyttsx3`:

### Inicialização

```python
voz = pyttsx3.init()
```

Inicializa o mecanismo responsável pela síntese de voz.

### Definição do texto

```python
voz.say(texto)
```

Adiciona o texto à fila de reprodução.

### Reprodução

```python
voz.runAndWait()
```

Executa a fila de fala e aguarda a conclusão da reprodução.

## 🚀 Possíveis evoluções

O projeto pode ser expandido para incluir:

* Seleção de voz
* Controle de velocidade
* Controle de volume
* Suporte a diferentes idiomas
* Leitura de arquivos `.txt`
* Leitura contínua de vários textos
* Interface gráfica
* Atalhos de teclado
* Integração com outras aplicações

## 📄 Licença

Este projeto é disponibilizado para fins de uso e desenvolvimento pessoal.
