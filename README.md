# 📧 Gerador de E-mails com Template

Este é um projeto em **Python** para gerar e-mails personalizados a partir de um arquivo de **template de texto**.  
A ideia é evitar retrabalho: em vez de escrever sempre a mesma mensagem, você preenche um modelo com dados dinâmicos (nome, data, remetente) e o programa cria automaticamente um arquivo `.txt` com o e-mail pronto.

## Como funciona? 

_O usuário informa:
   - Nome do destinatário
   - Data do encontro
   - Seu nome
_O programa lê o arquivo `template.txt` (onde ficam as variáveis entre {chaves}).
_Substitui essas variáveis pelos dados digitados.
_Cria um novo arquivo de saída em `saida_emails/`, com um nome único para cada execução.

Exemplo de template:
_Olá {nome_destinatario},

Este é um lembrete do nosso encontro no dia {data}.

Atenciosamente,  
{meu_nome}_
