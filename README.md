## 🌐 Password Validator API

A API desenvolvida em Python com o FastAPI auxilia na garantia de que as senhas sejam fortes o suficiente. Caso a senha não cumpra algumas das regras estabelecidas abaixo, a API retornará um erro indicando que a senha não é válida, dando detalhes sobre o que está faltando. Se a senha atender a todas as condições estabelecidas, será considerada válida.

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


## 📌 Uso do Endpoint /validate_password

- Para utilizar a API, é necessário que você envie uma requisição do tipo POST para o endpoint "/validate_password", incluindo a senha que será validada no body. Essa ação vai permitir a verificação da senha fornecida com relação aos critérios que foram estabelecidos, tendo uma análise mais detalhada do processo de validação.

- Para testar a aplicação é necessário que você possua o Insomnia ou Postman. No VsCode, caso queira, instale a extensão Thunder Client ou acesse a aplicação	pelo:

```bash
  http://localhost:8000/docs
```

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

- ❌ Aqui está alguns exemplos de quando a senha acabar sendo inválida: 

<img src="https://imgur.com/LwoeSEJ.png">

<img src="https://imgur.com/039qaIe.png">

<img src="https://imgur.com/QvPgapr.png">

- ✅ E aqui um exemplo de quando a senha for válida:

<img src="https://imgur.com/3JLdAjf.png">

## Detahes da solução


- A ideia aqui é oferecer uma API que verifica se uma senha atende aos critérios necessários para ser considerada forte. Para implementar isso, utilizei o framework FastAPI em conjunto com a linguagem Python.
- O ponto de entrada ("/validate_password") foi configurado para aceitar requisições do tipo POST, proporcionando uma interação fácil e direta.
- Em resposta aos requisitos do desafio, optei por criar regras de validação de forma individual. Cada critério possui sua própria função, facilitando a manutenção e compreensão do código.
- Adicionei um sistema de tratamento de erros, de modo que cada validação gera um código de erro específico, tornando mais claro o motivo pelo qual uma senha pode ser considerada fraca.
- Caso a senha passe por todas as validações, a função retorna uma mensagem indicando que a senha é válida, proporcionando feedback positivo ao usuário.
