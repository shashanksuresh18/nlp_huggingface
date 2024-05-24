import time
import socket

def wait_for_service(host, port, timeout=300):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection((host, port), timeout=10):
                print(f"Service at {host}:{port} is available")
                return True
        except (socket.timeout, ConnectionRefusedError):
            print(f"Waiting for service at {host}:{port}...")
            time.sleep(5)
    return False

if __name__ == "__main__":
    import sys
    if wait_for_service("web", 5000):
        print("Service is up, proceeding to run the test script.")
        sys.exit(0)
    else:
        print("Service did not start in the expected time.")
        sys.exit(1)
