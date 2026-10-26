# NTH — IP LOOKUP PRO v2.0

Ferramenta de reconhecimento passivo de IPs e domínios, escrita em Python.
Sem dependências externas — usa apenas a biblioteca padrão.

> ⚠️ **Aviso:** use apenas em IPs e servidores que você tem autorização
> para analisar. Reconhecimento não autorizado pode ser ilegal.

---

## 📋 Funcionalidades

- **Lookup de IP/domínio** — geolocalização, ISP, organização, ASN
- **Suporte a IPv4 e IPv6** — com validação correta da entrada
- **DNS reverso** — descobre o hostname associado ao IP
- **Ping** — verifica se o host está online e o tempo de resposta
- **Scan de portas comuns** — 15 portas (SSH, HTTP, RDP, MySQL, Minecraft...)
- **Aceita domínios** — digita `google.com` e o script resolve para IP
- **Detecção de IP privado** — avisa antes de consultar a API
- **Relatório em JSON** — salva tudo que foi coletado com data/hora
- **Interface colorida** — banner ASCII "NTH" e saída amigável no terminal

---

## 🚀 Instalação e uso

Requisitos:
- Python 3.6+
- Conexão com a internet (para a API de geolocalização)

```bash
python ip_info.py
