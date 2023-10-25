import socket
import sys
import psutil
import time
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from tutorial import ScoreboardService
from tutorial.ttypes import Player

class ScoreboardHandler:
    def __init__(self):
        self.scoreboard = []

    def registerPlayer(self, name, email):
        # Get the client's IP address
        ip = socket.gethostbyname(socket.gethostname())

        # Validate the email
        if not email.endswith("@sunydutchess.edu"):
            raise ValueError("Invalid email. Must end with '@sunydutchess.edu'.")

        # Create a new Player entry with a timestamp and add it to the scoreboard
        player = Player(name, ip, email, int(time.time()))
        print(f"*****{name} @ {email} via {ip}*****")
        dup_check = player in self.scoreboard
        if(dup_check):
            print(f"{email} is already in the system")
        else:
            self.scoreboard.append(player)
        #output
        for x in self.scoreboard: print(x.name)

        # Monitor memory usage after adding a player
        memory_info = psutil.virtual_memory()
        print(f"Memory Usage After Adding Player: {memory_info.percent:.2f}%")

        return player


if __name__ == "__main__":
    handler = ScoreboardHandler()
    processor = ScoreboardService.Processor(handler)
    transport = TSocket.TServerSocket(host="localhost", port=9091)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print("Starting the Scoreboard Service...")
    server.serve()
