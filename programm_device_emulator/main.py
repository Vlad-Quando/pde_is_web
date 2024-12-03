import client_class


def main():

    client = client_class.TCPClient()       # Creating client object

    try:
        client.handle_connection()          # starting the client

    # Stopping client if there is some errors
    except ConnectionResetError:
        print("Error occured. Closing connection.")
        client.close()

    except KeyboardInterrupt:
        print("Closing connection.")
        client.close()

    except OSError:
        print("Lost connection to the server.")
        print("Closing connection.")
        client.close()


if __name__ == "__main__":      # Starting client
    main()