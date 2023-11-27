import socket

def vote(server_address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_address, port))
        client_socket.send('VOTE'.encode('utf-8'))

        print(client_socket.recv(1024).decode('utf-8'))

        candidate_name = input("Enter the name of the candidate you want to vote for: ")
        client_socket.send(candidate_name.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print(response)

def get_results(server_address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_address, port))
        client_socket.send('RESULTS'.encode('utf-8'))

        results = client_socket.recv(1024).decode('utf-8')
        print("Voting Results:")
        print(results)

if __name__ == "__main__":
    server_address = '127.0.0.1'  # Change this to the IP address of your server
    server_port = 5555

    vote(server_address, server_port)
    get_results(server_address, server_port)
