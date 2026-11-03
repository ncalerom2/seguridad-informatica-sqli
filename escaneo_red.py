import argparse
import socket


def escanear_puertos(host, puertos):
    print(f'\n[+] Escaneando host: {host}')
    abiertos = []

    for puerto in puertos:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        resultado = s.connect_ex((host, puerto))
        s.close()

        if resultado == 0:
            print(f'Puerto {puerto}: ABIERTO')
            abiertos.append(puerto)
        else:
            print(f'Puerto {puerto}: CERRADO')

    return abiertos


def main():
    parser = argparse.ArgumentParser(description='Escaneo básico de puertos para una red local.')
    parser.add_argument('-t', '--target', default='127.0.0.1', help='Host a escanear.')
    parser.add_argument('-p', '--puertos', nargs='*', type=int, default=[21, 22, 80, 443, 3306, 3389], help='Puertos a comprobar.')
    args = parser.parse_args()

    escanear_puertos(args.target, args.puertos)


if __name__ == '__main__':
    main()
