# Museu Tronco, Ramos e Raízes.

<img src="https://github.com/lucasemn1/web-tronco-ramos-e-raizes/blob/main/public/assets/img/green_logo.png?raw=true" height="150" width="175" alt="Unform" />


Cultura, história, conhecimento!

## Sobre o projeto

<p>
  Esse projeto é o back-end do novo sistema do Museu Tronco, Ramos e Raízes que tem como principal propósito a valorização e a divulgação da cultura indígena e quilombola do RN.
</p>


## Tecnologias utilizadas no projeto


- [![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
- [![Django](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.djangoproject.com/)

## Instalação

1. É necesário antes de começar a usar sistema, instalar um ambiente virtual para que as bibliotecas usadas no projeto também funcionem em seu workspace. 
Caso não tenha o virtualenv:
```console
pip install virtualenv
```

2. Iniciando ambiente virtual

```console
python -m virtualenv [nomeDoAmbiente]
```


3. Instalando bibliotecas do projeto

```console
pip install -r requirements.txt
```


4. Rodando migrations do projeto

```console
python manage.py makemigrations
```
e
```console
python manage.py migrate
```

5. Iniciando projeto

```console
python manage.py runserver
```


3. Só isso! O projeto já está rodando na sua máquina! 🎉
