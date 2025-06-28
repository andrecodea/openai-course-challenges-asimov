# Curso de API da OpenAI

Este repositório contém exemplos e miniprojetos utilizando a API da OpenAI.

## 1. Chatbot com Reconhecimento de Voz CLI
 Implementação de um chatbot de voz que utiliza a API da OpenAI para gerar respostas a partir de prompts em áudio (tts-1, whisper-1 e gpt-3.5-turbo). Ele é capaz de: capturar áudio do usuário via microfone, transcrever o áudio para texto via Whisper, gerar respostas com GPT 3.5 turbo, converter a resposta para áuvio via TTS e reproduzir a resposta em áudio para o usuário.

## 2. Chatbot CLI
Implementação de um chatbot em Python usando a API GPT da OpenAI (gpt-3.5-turbo) para gerar respostas em tempo real. Eu implementei um chatbot de CLI simples que pode receber prompts e gerar texto.

3. Chatbot Financeiro CLI:
 Implementação de um chatbot financeiro em Python usando a API GPT da OpenAi (gpt-3.5-turbo), a API do Yahoo Finance e function calling para gerar respostas em tempo real. Eu implementei um chatbot de CLI que pode receber prompts e respondê-los utilizando function calling para perguntas sobre o mercado financeiro.

## Uso local
1. Clone o repositório.
2. Certifique-se de instalar os requisitos do arquivo `requirements.txt`.
3. Adicione sua chave de API da OpenAI em um arquivo `.env`.
4. Execute o seu arquivo `chatbot.py`

## Requisitos
Os requisitos podem ser encontrados no arquivo `requirements.txt`. Eles podem ser instalados via `pip`.

```bash
pip install -r requirements.txt
``` 