# Sistema de Veículos usando BotCity com Programação Orientada a Objetos

Este projeto utiliza o conceito de orientação a objetos em _Python_ e uma _API_ _Flask_ para gerenciar um sistema de aluguel de veículos (carros e motocicletas). São utilizadas diferentes rotas em cada template para instanciar um objeto das classes Carro ou Motocicleta ao utilizar o _submit_ do formulário _HTML_. Ao final da execução, os objetos estarão em um arquivo txt e na própria aplicação _Flask_.

## Pré-requisitos
- Ter o _Python_ 3.10 ou superior instalado na máquina

## Execução
 1. Criar ambiente virtual e instalar o _requiriments_:
  ```
  python -m venv venv
  . venv/bin/activate (Linux)
  . venv/Scripts/Activate (Windows)
  
  (venv) pip install -r requirements.txt
  ```

 Abrir dois terminais para executar a API e o Bot:
  - API:
    ```
    python app.py 
    ```
  - Bot:
    ```
    python bot.py
    ```