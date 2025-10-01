import os
from datetime import datetime

def gerar_email(caminho_template, dados):
    try:
        with open(caminho_template, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print("\n--- Conteúdo do template carregado ---")
            print(conteudo)
            email_final = conteudo.format(**dados)
            return email_final
    except FileNotFoundError:
        print("Erro: Arquivo de template não encontrado.")
        return None
    except KeyError as e:
        print(f"Erro: Chave faltando nos dados fornecidos - {e}")
        return None
    
if __name__ == "__main__":
    print("--- Gerador de E-mails com Templates ---")

    dados_email = {
        'nome_destinatario': input("Nome do destinatário: ").strip(),
        'data': input("Data do encontro: ").strip(),
        'meu_nome': input("Seu nome: ").strip()
    }

    caminho_template = 'template.txt'
    email_gerado = gerar_email(caminho_template, dados_email)

    if email_gerado:
        print("\n--- E-mail Gerado ---")
        print(email_gerado)

        # Criar pasta de saída
        pasta_saida = "saida_emails"
        os.makedirs(pasta_saida, exist_ok=True)

        # Gerar nome de arquivo dinâmico
        data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nome_destinatario = dados_email['nome_destinatario'].replace(" ", "_")
        nome_arquivo = f"email_{nome_destinatario}_{data_atual}.txt"

        caminho_saida = os.path.join(pasta_saida, nome_arquivo)

        # Salvar o arquivo
        with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
            arquivo_saida.write(email_gerado)

        print(f"\n✅ E-mail salvo em '{caminho_saida}'")
    else:
        print("\n⚠️ Nenhum e-mail foi gerado. Verifique o template.")
