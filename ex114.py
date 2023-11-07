# Exercício 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com.br/')
except urllib.error.URLError: # poderia ser apenas except:
    print('Deu erro!')
else:
    print('Tudo ok')
    print(site.read()) # para ler o código HTML do site desejado
