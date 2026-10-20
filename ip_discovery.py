import requests
import socket


def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        return f"Erro ao obter IP local: {e}"


def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        response.raise_for_status()
        return response.json()["ip"]
    except Exception as e:
        return f"Erro ao obter IP público: {e}"


def main():
    print("=" * 40)
    print("      IP Discovery Tool")
    print("=" * 40)

    print(f"IP Local:  {get_local_ip()}")
    print(f"IP Público: {get_public_ip()}")


if __name__ == "__main__":
    main()