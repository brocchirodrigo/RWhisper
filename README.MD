# RWhisper - API Simples com uso da IA Whisper OpenAI

A IA Whisper é a inteligência responsável por executar transcrições de áudio e vídeo.
Utilizando o modelo oficial, este repositório possui uma api que usa o Whisper de forma independente.

Aplicação simples com Flask para uso do whisper.

## Config

É possível ajustar o model no arquivo config.py

- Models:
  - tiny
  - base
  - small
  - medium
  - large

## Requer instalações adicionais no sistema

- ffmpeg
- nvidia-cudnn no Ubuntu (sudo apt install nvidia-cudnn)

# Inicialização

Instalação:

Iniciar a "venv" com o comando:

```shell
  python3 -m venv venv
```

Ativar o ambiente virtual:

```shell
  source venv/bin/activate
```

Obs: Para desativar a 'venv', basta digitar deactivate no local do activate.

Instalar as dependências:

```shell
  pip install -r requirements.txt
```

Executar com comando local:

```shell
  python3 main.py
```

Executar com WSGI Serverless (Requer instalação do framework e suas dependências - Leia https://www.npmjs.com/package/serverless-wsgi)

```shell
  serverless wsgi serve
```

# Chamada API

Abaixo um exemplo de chamada via cURL

```shell
  curl --request POST \
    --url http://127.0.0.1:5000/ \
    --header 'Content-Type: multipart/form-data' \
    --form 'file=[arquivo de vídeo ou áudio]'
```

Com NodeJS usando Fetch

```javascript
const fs = require("fs");
const FormData = require("form-data");
const fetch = require("node-fetch");
const formData = new FormData();

formData.append("file", fs.createReadStream("[ARQUIVO DE VÍDEO]"));

let url = "http://127.0.0.1:5000/";

let options = {
  method: "POST",
  headers: {
    "Content-Type": "multipart/form-data; boundary=---011000010111000001101001",
  },
};

options.body = formData;

fetch(url, options)
  .then((res) => res.json())
  .then((json) => console.log(json))
  .catch((err) => console.error("error:" + err));
```

## Whisper Openai Oficial

Repositório oficial https://github.com/openai/whisper
