'''
Teste básico de Processamento de Linguagem Natural utilizando nltk e google translate
A função falar utiliza o comando say do terminal do macOS
Autor: Alef Matias
'''
import speech_recognition as sr
import subprocess
from nltk.sentiment import SentimentIntensityAnalyzer
from googletrans import Translator

vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
amareloClaro = '\033[1;93m'
azul = '\033[1;34m'
negrito = '\033[;1m'
reset = '\033[0;0m'

tradutor = Translator()

erro = amarelo + 'Opa! Parece que não entendi o que você disse...' + reset


def falar(comando):
    subprocess.Popen(comando, shell=True).wait()


def ouvir():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print(amareloClaro + 'Diga alguma coisa...' + reset)
        falar(f'say Diga alguma coisa')
        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio, language='pt-br')
        print(f'Você disse: {azul}{frase}{reset}')
        falar(f'say Você disse: {frase}')
    except:
        print(erro)
        falar(f'say {erro}')
    return frase


while True:
    frase = ouvir()
    traducao = str(tradutor.translate(frase, src='pt', dest='en')).split(',')[2][6:]
    print(f'Frase traduzida para inglês: {azul}{traducao}{reset}\n')
    analisador = SentimentIntensityAnalyzer()
    resultado = analisador.polarity_scores(traducao)
    print(f"{negrito}RESULTADO{reset}\n{vermelho}Negativo: {resultado['neg'] * 100:.2f}%{reset}\n{amarelo}Neutro: {resultado['neu'] * 100:.2f}%{amarelo}\n{verde}Positivo: {resultado['pos'] * 100:.2f}%{reset}\n")
    if str(frase) == 'sair' or str(frase) == 'não':
        falar('say Foi bom falar com você, até a próxima')
        break
