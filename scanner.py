import socket
import time

def scan_port(host, port):
    """Attempts to connect to a port and returns True if open."""

    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout so scanner doesn't freeze
        sock.settimeout(0.5)

        # connect_ex() returns a code instead of raising an exception
        result = sock.connect_ex((host, port))

        # 0 = port open
        if result == 0:
            return True
        else:
            return False

    except socket.gaierror:
        # Happens if hostname is invalid
        print("[ERROR] Invalid hostname.")
        return None

    except Exception as e:
        # General fallback error
        print(f"[ERROR] Unexpected error: {e}")
        return None

    finally:
        # Always close socket
        sock.close()


def port_scanner():
    """Main scanner function handling input and scanning loop."""

    host = input("Enter host (127.0.0.1 or scanme.nmap.org): ").strip()

    try:
        # Gather port range
        start = int(input("Enter start port: "))
        end = int(input("Enter end port: "))
    except ValueError:
        # Non-numeric input
        print("[ERROR] Port numbers must be integers.")
        return

    # Validate port range
    if start < 0 or end > 65535 or start > end:
        print("[ERROR] Invalid port range.")
        return

    print(f"\nScanning {host} from port {start} to {end}...\n")
    time.sleep(1)

    # Scan through the range
    for port in range(start, end + 1):
        open_port = scan_port(host, port)

        if open_port is True:
            print(f"[OPEN] Port {port} is open")
        elif open_port is False:
            print(f"[CLOSED] Port {port} closed")
        else:
            # Host unreachable or other error
            print("[ERROR] Host unreachable.")
            break

    print("\nScan complete.")

if __name__ == "__main__":
    port_scanner()
