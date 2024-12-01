# 🛠️ **Ferramenta de Diagnóstico Windows com GUI**

Este projeto fornece uma interface gráfica simples para executar comandos de diagnóstico do Windows. Desenvolvido com `Python` e `tkinter`, ele facilita a verificação de conectividade de rede, análise do sistema e limpeza de arquivos temporários.

---

## 📋 **Descrição do Projeto**

A aplicação executa comandos comuns de diagnóstico do Windows, como `ipconfig`, `ping`, `tracert`, `netstat`, entre outros, e permite a limpeza de arquivos temporários do sistema, além de cache e cookies do Chrome. Ela exibe os resultados diretamente em uma interface gráfica, ideal para técnicos de informática que desejam otimizar ou resolver problemas de rede em máquinas Windows.

---

## 🚀 **Funcionalidades**

- 📡 **Informações de Rede**: Exibe detalhes dos adaptadores de rede.
- 🌐 **Testes de Conectividade**: Realiza ping e rastreia rotas até o host.
- 🗂️ **Visualização de Conexões**: Mostra conexões ativas e tabelas ARP.
- 🔍 **Consultas DNS**: Verifica informações de DNS.
- 📊 **Tabela de Roteamento**: Visualiza rotas de rede do sistema.
- 🧹 **Limpeza de Arquivos Temporários**: Remove arquivos temporários do sistema.
- 🧑‍💻 **Limpeza de Cache e Cookies do Chrome**: Apaga o cache e os cookies do navegador Google Chrome.

---

## 🖥️ **Tecnologias Utilizadas**

- **Python** (3.6 ou superior)
- **tkinter** (biblioteca padrão para interfaces gráficas)

---

## 🛠️ **Pré-requisitos**

- Ter o Python instalado na máquina.
- Certifique-se de ter permissões de administrador para executar alguns comandos.
- O Google Chrome deve estar instalado para a funcionalidade de limpeza de cache e cookies.

---

## ⚠️ **Aviso Importante**

A função de **limpeza de arquivos temporários** pode remover arquivos que são usados por outros programas ou o próprio sistema, e embora esses arquivos geralmente sejam descartáveis, existe o risco de **perda de dados**. É altamente recomendado que você tenha backup dos dados importantes antes de executar a limpeza.

Além disso, ao limpar **cache e cookies do Google Chrome**, todos os dados armazenados localmente, como informações de login, preferências de navegação e histórico, serão apagados. Certifique-se de que deseja realizar essa ação antes de executá-la.

---

## ▶️ **Como Executar o Projeto**

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/seu-usuario/diagnostico-windows-gui.git
   cd diagnostico-windows-gui
