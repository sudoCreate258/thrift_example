import sys
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from tutorial import ScoreboardService
from tutorial.ttypes import Player

def main(name='joe snow', email='joe821@sunydutchess.edu'):
    try:
        # Connect to the server
        transport = TSocket.TSocket("localhost", 9091)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        client = ScoreboardService.Client(protocol)
        transport.open()

        # Prompt the user for their name and email
        #name = "first last" #input("Enter your name: ")
        #email = "joe@sunydutchess.edu" #input("Enter your email: ")

        try:
            # Register the player with the server
            player = client.registerPlayer(name, email)
            print("Player registered with a dramatic timestamp:")
            print(f"   Player: {player.name} ({player.ip}), Email: {player.email}")
            print(f"   Timestamp: *** {player.timestamp} ***")

            # Retrieve and display the scoreboard with dramatic timestamps
            #exit(0)
            #scoreboard = client.getScoreboard()
            #print("Dramatic Scoreboard:")
            #for player in scoreboard:
            #    print(f"   Player: {player.name} ({player.ip}), Email: {player.email}")
            #    print(f"   Timestamp: *** {player.timestamp} ***")

        except ValueError as e:
                print(f"Error: {e}")
                exit_flag = false   #
            
        transport.close()
    except Thrift.TException as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
