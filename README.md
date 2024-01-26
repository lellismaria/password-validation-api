
## 🌐 Password Validator API

A API desenvolvida em Python com o FastAPI auxilia na garantia de que as senhas sejam fortes o suficiente. Caso a senha não cumpra algumas das regras estabelecidas abaixo, a API retornará um erro indicando que a senha não é válida, dando detalhes sobre o que está faltando. Se a senha atender a todas as condições estabelecidas, será considerada válida.

## 📃 Regras

- Nove ou mais caracteres
- Ao menos 1 dígito
- Ao menos 1 letra minúscula
- Ao menos 1 letra maiúscula
- Ao menos 1 caractere especial
  - Considere como especial os seguintes caracteres: !@#$%^&*()-+
- Não possuir caracteres repetidos dentro do conjunto

Exemplos:  

```python
IsValid("") // false  
IsValid("aa") // false  
IsValid("ab") // false  
IsValid("AAAbbbCc") // false  
IsValid("AbTp9!foo") // false  
IsValid("AbTp9!foA") // false
IsValid("AbTp9 fok") // false
IsValid("AbTp9!fok") // true
```


## Instruções iniciais do Projeto

Clone o projeto

```bash
  git clone https://github.com/lellismaria/password-validation-api.git
```

Depois, certifique-se de ter os pacotes necessários instalados. Caso você não possua, instale utilizando os seguintes comandos:

```fastapi
  pip install fastapi 
```
```pydantic
  pip install pydantic
```
```uvicorn
  pip install uvicorn
```

Inicie o servidor

```bash
  uvicorn main:app --reload
```


## 📌 Uso do Endpoint /validate_password

- Para utilizar a API, é necessário que você envie uma requisição do tipo POST para o endpoint "/validate_password", incluindo a senha que será validada no body. Essa ação vai permitir a verificação da senha fornecida com relação aos critérios que foram estabelecidos, tendo uma análise mais detalhada do processo de validação.

- Para testar a aplicação é necessário que você possua o Insomnia ou Postman. No VsCode, caso queira, instale a extensão Thunder Client ou acesse a aplicação	pelo:

```bash
  http://localhost:8000/docs
```

## Como utilizar

- Caso queira testar pelo Thunder Client, busque pela extensão no VsCode:

<img src="https://imgur.com/GA3ZckE.png">

- Vamos criar uma nova requisição:

<img src="https://imgur.com/uXFnrPC.png">

- Vamos selecionar o método POST, digitar a URL com o Endpoint e passar um Body para ter o retorno esperado.

- Para realizar essa requisição você deve passar o seguinte body:

```bash
  {
	"password":"senha_aqui"
  }
```

- ❌ Aqui está um exemplo de quando a senha tem algum caractere repetido: 

<img src="https://imgur.com/LwoeSEJ.png">

- ❌ Aqui está um outro exemplo de quando a senha não tem os caracteres suficientes: 

<img src="https://imgur.com/039qaIe.png">

- ❌ Temos outro exemplo de quando a senha não tem ao menos um caracter especial: 

<img src="https://imgur.com/QvPgapr.png">

- ❌ Um outro exemplo de quando a senha deve conter ao menos uma letra maiúscula:

<img src="https://imgur.com/KlRptL9.png">

- ❌ Um outro exemplo de quando a senha deve conter ao menos uma letra minúscula:

<img src="https://imgur.com/j3pBh6l.png">

- ✅ E por último um exemplo de quando a senha for válida:

<img src="https://imgur.com/3JLdAjf.png">

## 

