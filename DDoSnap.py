import socket
import json
import urllib.request

def obter_info_ip(ip):
    try:
        url = f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,zip,lat,lon,timezone,isp,org,as,reverse,mobile,proxy,hosting,query"
        with urllib.request.urlopen(url, timeout=10) as r:
            dados = json.loads(r.read().decode())
        return dados
    except Exception as e:
        print(f"[!] Erro ao consultar: {e}")
        return None

def main():
    print("=" * 50)
    print("   CONSULTA DE INFORMAÇÕES DE IP")
    print("=" * 50)
    ip = input("\nDigite o IP alvo: ").strip()

    try:
        socket.inet_aton(ip)
    except socket.error:
        print("[!] IP inválido.")
        return

    print(f"\n[*] Consultando informações de {ip}...\n")
    info = obter_info_ip(ip)

    if info and info.get("status") == "success":
        print(f"  IP        : {info.get('query')}")
        print(f"  País      : {info.get('country')}")
        print(f"  Região    : {info.get('regionName')}")
        print(f"  Cidade    : {info.get('city')}")
        print(f"  CEP       : {info.get('zip')}")
        print(f"  Lat/Lon   : {info.get('lat')}, {info.get('lon')}")
        print(f"  Fuso      : {info.get('timezone')}")
        print(f"  ISP       : {info.get('isp')}")
        print(f"  Org       : {info.get('org')}")
        print(f"  AS        : {info.get('as')}")
        print(f"  Reverse   : {info.get('reverse')}")
        print(f"  Mobile    : {'Sim' if info.get('mobile') else 'Não'}")
        print(f"  Proxy/VPN : {'Sim' if info.get('proxy') else 'Não'}")
        print(f"  Hosting   : {'Sim' if info.get('hosting') else 'Não'}")
    else:
        print("[!] Não foi possível obter informações (IP privado ou inválido).")

if __name__ == "__main__":
    main()
