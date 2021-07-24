Aplicacao WEB desenvolvida em Python usando Django

1 - Instalar Python:
``sudo apt-get install python3``

2 - Instalar Pip:
``sudo apt-get install python3-pip``

3 -Instalar Django:
``python -m pip install Django``

4 - Criar servidor:
``django-admin startapp application`` (**application** = nome do diretorio da aplicacao)

5 - Criar arquivo de migracao:
``python manage.py makemigrations``

6 - Fazer a migracao dos modelos criados:
``python manage.py migrate``

7 - Iniciar servidor:
``python3 manage.py runserver``

