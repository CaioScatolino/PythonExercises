#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 2</font>
# 
# ## Download: http://github.com/dsacademybr

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios Cap02

# In[2]:


# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista1 = [1,2,3,4,5,6,7,8,9,10]
print(lista1)


# In[4]:


# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista2 = ["banana", "chocolate", "arroz", "feijao", "carne"]
print(lista2)


# In[9]:


# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
st1 = "Bom "
st2 = "dia!"
st3 = st1 + st2
print(st3)


# In[10]:


# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla1 = (1,2,2,3,4,4,4)
tupla1.count(4)


# In[12]:


# Exercício 5 - Crie um dicionário vazio e imprima na tela
dict1 = {}
print (dict1)


# In[13]:


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dict2 = {"Mauro":26, "Rodrigo":29, "Elisa": 25}
print(dict2)


# In[14]:


# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dict2["Alberto"] = 22
print(dict2)


# In[15]:


# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dict3 = {"k1":"escada", "k2":["martelo","prego"], "k3":"madeira"}
print(dict3)


# In[16]:


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.

list4 = ["suco de laranja", ("4 laranjas","água"), {"açúcar":"40gr","gelo":"4 cubos"}, 5.50]
print(list4)


# In[17]:


# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase[0:18]


# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
