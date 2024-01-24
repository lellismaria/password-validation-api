
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

