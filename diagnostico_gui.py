import subprocess
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import os
import shutil

# Função para executar comandos, mostrar resultados e salvar no arquivo
def run_command(description, command):
    def task():  # Executa o comando em uma thread separada
        output_text.insert(tk.END, f"\n{description}\n{'-' * len(description)}\n")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
            
            # Exibe a saída padrão ou o erro
            if result.stdout:
                output_text.insert(tk.END, result.stdout + "\n")
            if result.stderr:
                output_text.insert(tk.END, f"Erro: {result.stderr}\n")
            
            # Salvando o resultado no arquivo
            with open("relatorio_diagnostico.txt", "a", encoding="utf-8") as file:
                file.write(f"{description}\n{'-' * len(description)}\n")
                file.write(result.stdout if result.stdout else result.stderr)
                file.write("\n\n")
                
        except Exception as e:
            output_text.insert(tk.END, f"Erro ao executar o comando: {e}\n")
        
        output_text.see(tk.END)  # Rola para o final
    
    # Cria e inicia uma thread para evitar congelamento da interface
    thread = threading.Thread(target=task)
    thread.start()

# Função para limpar arquivos temporários do Windows
def clear_temp_files():
    temp_dirs = [
        os.getenv('TEMP'),  # Diretório temporário do usuário (%temp%)
        os.path.join(os.getenv('USERPROFILE'), r'AppData\Local\Temp')  # Diretório alternativo do usuário
    ]
    
    for temp_dir in temp_dirs:
        try:
            for root_dir, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root_dir, file)
                    try:
                        os.remove(file_path)
                    except Exception as e:
                        output_text.insert(tk.END, f"Erro ao excluir arquivo temporário {file_path}: {e}\n")
            output_text.insert(tk.END, f"\nArquivos temporários de {temp_dir} limpos com sucesso.\n")
        except Exception as e:
            output_text.insert(tk.END, f"Erro ao limpar arquivos temporários: {e}\n")
    
    output_text.see(tk.END)

# Função para limpar cache e cookies do Chrome
def clear_chrome_cache():
    user_profile = os.getenv('USERPROFILE')
    chrome_cache_dir = os.path.join(user_profile, r'AppData\Local\Google\Chrome\User Data\Default')
    
    # Caminhos dos diretórios de cache e cookies
    cache_dir = os.path.join(chrome_cache_dir, 'Cache')
    cookies_file = os.path.join(chrome_cache_dir, 'Cookies')
    
    try:
        # Apagar o conteúdo do cache
        if os.path.exists(cache_dir):
            for file in os.listdir(cache_dir):
                file_path = os.path.join(cache_dir, file)
                try:
                    os.remove(file_path)
                except Exception as e:
                    output_text.insert(tk.END, f"Erro ao excluir arquivo de cache {file_path}: {e}\n")
            output_text.insert(tk.END, "\nCache do Chrome limpo com sucesso.\n")
        else:
            output_text.insert(tk.END, "Cache do Chrome não encontrado.\n")
        
        # Apagar o arquivo de cookies
        if os.path.exists(cookies_file):
            os.remove(cookies_file)
            output_text.insert(tk.END, "Cookies do Chrome limpos com sucesso.\n")
        else:
            output_text.insert(tk.END, "Cookies do Chrome não encontrados.\n")
        
    except Exception as e:
        output_text.insert(tk.END, f"Erro ao limpar cache/cookies do Chrome: {e}\n")
    
    output_text.see(tk.END)

# Função para limpar a área de texto
def clear_output():
    output_text.delete(1.0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Ferramenta de Diagnóstico Windows")
root.geometry("1000x500")

# Frame para os botões (agora em um único frame à esquerda)
buttons_frame = tk.Frame(root)
buttons_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

# Área de texto para exibir resultados
output_text = scrolledtext.ScrolledText(root, width=80, height=25, wrap=tk.WORD)
output_text.pack(pady=8, padx=10, side=tk.RIGHT)

# Adiciona um botão para limpar a área de texto
clear_button = tk.Button(buttons_frame, text="Limpar Saída", command=clear_output, width=30)
clear_button.grid(row=0, column=0, padx=10, pady=5)

# Comandos a serem executados
commands = [
    ("Informações dos adaptadores de rede", "ipconfig /all"),
    ("Testar conectividade com Google", "ping google.com"),
    ("Mostrar rota para Google", "tracert google.com"),
    ("Listar conexões ativas", "netstat -an"),
    ("Consultar DNS do Google", "nslookup google.com"),
    ("Exibir tabela ARP", "arp -a"),
    ("Exibir tabela de roteamento", "route print"),
    ("Mostrar nomes NetBIOS", "nbtstat -n")
]

# Função para criar os botões
def create_button(description, command, row):
    button = tk.Button(buttons_frame, text=description, command=lambda d=description, c=command: run_command(d, c), width=30)
    button.grid(row=row, column=0, padx=10, pady=5, sticky='w')

# Adiciona os botões de comandos
for index, (description, command) in enumerate(commands):
    create_button(description, command, index + 1)

# Botões para limpeza de arquivos temporários e cache do Chrome
clean_temp_button = tk.Button(buttons_frame, text="Limpar Arquivos Temporários", command=clear_temp_files, width=30)
clean_temp_button.grid(row=len(commands) + 1, column=0, padx=10, pady=5, sticky='w')

clean_chrome_button = tk.Button(buttons_frame, text="Limpar Cache e Cookies do Chrome", command=clear_chrome_cache, width=30)
clean_chrome_button.grid(row=len(commands) + 2, column=0, padx=10, pady=5, sticky='w')

# Inicia o loop da interface
root.mainloop()
