# coding=utf-8
def sauda(nome):
    print "Olá, " + nome + "!"
    sauda2(nome)
    print "preparando para dizer tchau..."
    tchau()

def sauda2(nome):
    print 'Como vai ' + nome + '?'

def tchau():
    print 'Ok, tchau!'


sauda('Edkallenn')