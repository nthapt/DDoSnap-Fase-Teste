#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import json
import subprocess
import urllib.request
import ipaddress
import sys
import os
from datetime import datetime

class Cor:
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    VERMELHO = "\033[91m"
    CIANO = "\033[96m"
    RESET = "\033[0m"
    NEGRITO = "\033[1m"

BANNER = f"""{Cor.CIANO}{Cor.NEGRITO}
 ██  ██  ██████████  ██
 ██  ██  ██      ██  ██
 ██  ██  ██      ██  ██
 ██  ██  ██████████  ██
 ██  ██  ██   ██     ██
 ██  ██  ██    ██    ██
 ██████  ██     ██   ███████
{Cor.RESET}
       IP LOOKUP PRO v2.0
"""

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def cabecalho():
    print(BANNER)

def validar_ip(ip):
    try:
        obj = ipaddress.ip_address(ip)
        return True, obj.version, obj.is_private
    except ValueError:
        return False, None, None

def obter_meu_ip():
    try:
        with urllib.request.urlopen("https://api.ipify.org", timeout=10) as r:
            return r.read().decode().strip()
    except Exception:
        return None

def dns_reverso(ip):
    try:
        nome, _, _ = socket.gethostbyaddr(ip)
        return nome
    except (socket.herror, socket.gaierror, OSError):
        return "Não encontrado"

def ping_host(ip):
    param = "-n" if os.name == "nt" else "-c"
    tempo_arg = "-w" if os.name == "nt" else "-W"
    try:
        r = subprocess.run(
            ["ping", param, "4", tempo_arg, "2000", ip],
            capture_output=True, text=True, timeout=15
        )
        vivo = (r.returncode == 0)
        tempo_medio = None
        for linha in r.stdout.splitlines():
            l = linha.lower()
            if "média" in l or "avg" in l or "average" in l:
                numeros = [n for n in l.replace("/", " ").split() if n.replace(".", "").isdigit()]
                if numeros:
                    tempo_medio = numeros[-1]
        return vivo, tempo_medio
    except Exception:
        return False, None

PORTAS_COMUNS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS",
    445: "SMB", 3306: "MySQL", 3389: "RDP", 8080: "HTTP Alt",
    25565: "Minecraft", 27017: "MongoDB",
}

def escanear_portas(ip, portas=None, timeout=1.0):
    if portas is None:
        portas = PORTAS_COMUNS
    abertas = []
    print(f"\n{Cor.AMARELO}[*] Escaneando {len(portas)} portas comuns... (pode demorar um pouco){Cor.RESET}")
    for porta, servico in portas.items():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                if s.connect_ex((ip, porta)) == 0:
                    abertas.append((porta, servico))
                    print(f"  {Cor.VERDE}[+] Porta {porta:>5} aberta  ({servico}){Cor.RESET}")
        except OSError:
            continue
    return abertas

def obter_info_api(ip):
    url = (f"http://ip-api.com/json/{ip}?fields=status,message,"
           f"country,countryCode,regionName,city,zip,lat,lon,timezone,"
           f"isp,org,as,reverse,mobile,proxy,hosting,query")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "IpLookupPro/2.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        print(f"{Cor.VERMELHO}[!] Erro ao consultar a API: {e}{Cor.RESET}")
        return None

def mostrar_info_api(info):
    print(f"""{Cor.CIANO}
─────────── INFORMAÇÕES DE LOCALIZAÇÃO ───────────{Cor.RESET}
  IP        : {info.get('query')}
  País      : {info.get('country')} ({info.get('countryCode')})
  Região    : {info.get('regionName')}
  Cidade    : {info.get('city')}
  CEP       : {info.get('zip')}
  Lat/Lon   : {info.get('lat')}, {info.get('lon')}
  Fuso      : {info.get('timezone')}
{Cor.CIANO}──────────── INFORMAÇÕES DE REDE ────────────{Cor.RESET}
  ISP       : {info.get('isp')}
  Org       : {info.get('org')}
  AS        : {info.get('as')}
  Reverse   : {info.get('reverse') or dns_reverso(info.get('query', ''))}
  Mobile    : {'Sim' if info.get('mobile') else 'Não'}
  Proxy/VPN : {'Sim' if info.get('proxy') else 'Não'}
  Hosting   : {'Sim' if info.get('hosting') else 'Não'}
""")

def resolver_host(host):
    try:
        return socket.gethostbyname(host.strip())
    except socket.gaierror:
        return None

def salvar_relatorio(ip, dados):
    nome = f"relatorio_{ip.replace(':', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    try:
        with open(nome, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print(f"{Cor.VERDE}[+] Relatório salvo em: {nome}{Cor.RESET}")
    except Exception as e:
        print(f"{Cor.VERMELHO}[!] Não foi possível salvar: {e}{Cor.RESET}")

def main():
    limpar_tela()
    cabecalho()

    entrada = input("Digite o IP ou domínio alvo: ").strip()
    if not entrada:
        print(f"{Cor.VERMELHO}[!] Nada foi digitado. Saindo...{Cor.RESET}")
        sys.exit(0)

    valido, versao, privado = validar_ip(entrada)
    if not valido:
        resolvido = resolver_host(entrada)
        if resolvido:
            print(f"{Cor.AMARELO}[*] '{entrada}' resolvido para o IP: {resolvido}{Cor.RESET}")
            ip = resolvido
        else:
            print(f"{Cor.VERMELHO}[!] '{entrada}' não é um IP válido nem um domínio resolvível.{Cor.RESET}")
            sys.exit(1)
    else:
        ip = entrada

    if privado:
        print(f"{Cor.AMARELO}[!] Este é um IP privado/rede local. A API não terá dados de localização.{Cor.RESET}")

    print(f"\n{Cor.AMARELO}[*] Coletando informações de {ip}...{Cor.RESET}")
    info = obter_info_api(ip)

    relatorio = {"alvo": ip, "data": datetime.now().isoformat()}

    if info and info.get("status") == "success":
        mostrar_info_api(info)
        relatorio["api"] = info
    else:
        print(f"{Cor.AMARELO}[!] Sem dados de geolocalização (IP privado ou API indisponível).{Cor.RESET}")

    hostname = dns_reverso(ip)
    print(f"  Hostname  : {hostname}")
    relatorio["hostname"] = hostname

    print(f"\n{Cor.AMARELO}[*] Testando se o host responde (ping)...{Cor.RESET}")
    vivo, tempo = ping_host(ip)
    if vivo:
        print(f"{Cor.VERDE}[+] Host está ONLINE!" + (f" Tempo médio: {tempo} ms" if tempo else "") + f"{Cor.RESET}")
    else:
        print(f"{Cor.VERMELHO}[-] Host não respondeu ao ping (pode estar bloqueando ICMP ou offline).{Cor.RESET}")
    relatorio["ping_online"] = vivo
    relatorio["ping_tempo_ms"] = tempo

    if vivo:
        escolha = input(f"\n{Cor.AMARELO}Deseja escanear as portas comuns deste host? (s/n): {Cor.RESET}").strip().lower()
        if escolha in ("s", "sim"):
            abertas = escanear_portas(ip)
            relatorio["portas_abertas"] = [{"porta": p, "servico": s} for p, s in abertas]
            if not abertas:
                print(f"{Cor.AMARELO}[*] Nenhuma porta comum encontrada aberta.{Cor.RESET}")
    else:
        print(f"{Cor.AMARELO}[*] Host offline — scan de portas pulado.{Cor.RESET}")

    escolha = input(f"\n{Cor.AMARELO}Deseja salvar o relatório em JSON? (s/n): {Cor.RESET}").strip().lower()
    if escolha in ("s", "sim"):
        salvar_relatorio(ip, relatorio)

    print(f"\n{Cor.VERDE}[✓] Análise concluída. Até mais!{Cor.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Cor.AMARELO}[*] Interrompido pelo usuário. Saindo...{Cor.RESET}")
        sys.exit(0)
