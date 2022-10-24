import unittest
import threading
import socket
import mock
from events import main_event


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("localhost", 6000))
        main_event.wait()
        sock.sendall(b"hello")


class MockTest(unittest.TestCase):
    def test_message_sent(self):
        with mock.patch("socket.socket") as mock_socket:
            threading.Thread(target=main).start()
            sendall = mock_socket.return_value.__enter__.return_value.sendall
            sendall.assert_called()

if __name__ == "__main__":
    unittest.main()
