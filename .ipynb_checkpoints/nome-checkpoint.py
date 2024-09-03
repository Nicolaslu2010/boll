#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Animal():
    def __init__(self):
        print('Animal criando')

    def  oQueSou(self):
        print('animal')

    def come(self):
        print('comendo')


class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('cachorro criado')


    def oQueSou(self):
        print('cachorro')

    def late(self):
        print ('auau!') 


# In[14]:


c = Cachorro()


# In[15]:


c.oQueSou()


# In[16]:


c.come()


# In[17]:


c.late()


# In[28]:


class Animal_selvagem():
    
    def mover (self):
        print('estou correndo')

    def come(self):
        print('comendo')

class Animal_domestico():
    def mover():
        print ('estou andando')

    def getDono(self):
        return self.dono 


class cachorro(Animal_selvagem,Animal_domestico):
    def __init__(self,dono):
      self.dono = dono 

    def late(self):
        print('auaua!')


# In[32]:


c = cachorro('Luiz')


# In[33]:


print(c.getDono())
c.come()
c.late()
c.mover()


# In[35]:


class Classe(): #Aqui criamos o molde de nossa classe (class)

    jogo = 'defensores da grande mãe'

    def __init__(self,nome,vida,arma,magia): #aqui criamos o metodo de inicialização __init__
        self.nome =nome  #definimos os atributos deste metodos 
        self.vida = vida
        self.arma = arma

        def getjogo(): #o metodo set define qual valor sera guardado dentro da variavel
            return self.jogo

        def setjogo(i):
            self.jogo= i


# In[43]:


def sobrenomeNaOrdem(nome,sobrenome1,sobrenome2):
    if(len(sobrenome2)>len(sobrenome1)):
        return nome+' '+sobrenome1+' '+sobrenome2
    else: 
        return nome+' '+sobrenome2+' '+sobrenome1
print (sobrenomeNaOrdem('Nicolas','Luiz','Teixeira'))
print (sobrenomeNaOrdem('Melissa','Vitoria','Menezes'))


# In[ ]:




