# 🔊 Leitor de Texto com Python

Este é um pequeno projeto desenvolvido em **Python** utilizando a biblioteca **pyttsx3** para transformar texto em fala.

O programa pergunta ao usuário se ele deseja que o computador fale alguma coisa. Caso a resposta seja **"sim"**, o usuário pode digitar um texto e o computador irá lê-lo em voz alta.

## 🐍 Tecnologias utilizadas

* Python
* pyttsx3

## 📦 Instalação

Para utilizar o projeto, primeiro é necessário instalar a biblioteca `pyttsx3`:

```bash
pip install pyttsx3
```

## ⚙️ Como o programa funciona

Primeiro, a biblioteca `pyttsx3` é importada:

```python
import pyttsx3
```

Depois, o mecanismo de voz é inicializado:

```python
voz = pyttsx3.init()
```

O programa pergunta ao usuário se ele quer que o computador fale:

```python
pergunta = input("Você quer que eu fale? (sim/não): ").lower()
```

O `.lower()` transforma a resposta em letras minúsculas.

Por exemplo:

```text
SIM → sim
Sim → sim
sIm → sim
```

Assim, podemos verificar apenas:

```python
if pergunta == "sim":
```

Se a resposta for `"sim"`, o programa pergunta qual texto deve ser falado:

```python
texto = input("O que você quer que eu fale? ")
```

Depois, o método `say()` recebe o texto:

```python
voz.say(texto)
```

Por fim, `runAndWait()` executa a fala:

```python
voz.runAndWait()
```

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

## 🧠 O que aprendi

Com esse projeto, pratiquei alguns conceitos importantes de Python:

* Importação de bibliotecas
* Variáveis
* `input()`
* `if` e `else`
* Comparação de textos
* Método `.lower()`
* Síntese de voz
* Uso de bibliotecas externas
* Métodos como `say()` e `runAndWait()`

## 🔊 Sobre o pyttsx3

O **pyttsx3** é uma biblioteca que permite fazer programas Python transformarem texto em fala utilizando os mecanismos de voz disponíveis no computador.

Neste projeto, utilizei principalmente:

### `pyttsx3.init()`

Inicializa o mecanismo de voz.

### `voz.say()`

Define o texto que será falado.

### `voz.runAndWait()`

Executa a fala e espera que ela termine.

### `.lower()`

Transforma um texto em letras minúsculas, facilitando comparações.

## 🚀 Possíveis melhorias

No futuro, posso adicionar:

* 🗣️ Escolha de diferentes vozes
* ⚡ Controle da velocidade da fala
* 🔊 Controle do volume
* 🔁 Opção para falar vários textos
* 🌎 Suporte para outros idiomas
* 🖥️ Interface gráfica
* ❌ Uma opção específica para sair do programa

## 🎯 Objetivo

O objetivo deste projeto foi praticar **Python, estruturas condicionais, entrada de dados e síntese de voz**, criando um programa simples capaz de transformar um texto digitado pelo usuário em fala.

---

🐍 **Projeto criado como prática de programação em Python.**
