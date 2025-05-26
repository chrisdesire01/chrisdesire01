# -*-coding:Latin-1 -*
import mechanize
url = raw_input ('Entrez une URL : ')
print "="*60
def view_page(url):
#fonction qui affiche le code source de la page
web
navigateur = mechanize.Browser()
page_site = navigateur.open(url)
code_source = page_site.read()
print code_source
view_page(url)
source
#la fonction est appelée pour chercher le code source
