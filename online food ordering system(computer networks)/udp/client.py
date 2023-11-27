import socket

def vote(server_address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.sendto('VOTE'.encode('utf-8'), (server_address, port))

        response, _ = client_socket.recvfrom(1024)
        print(response.decode('utf-8'))

        candidate_name = input("Enter the name of the candidate you want to vote for: ")
        client_socket.sendto(candidate_name.encode('utf-8'), (server_address, port))

        response, _ = client_socket.recvfrom(1024)
        print(response.decode('utf-8'))

def get_results(server_address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.sendto('RESULTS'.encode('utf-8'), (server_address, port))

        results, _ = client_socket.recvfrom(1024)
        print("Voting Results:")
        print(results.decode('utf-8'))

if __name__ == "__main__":
    server_address = '127.0.0.1'  # Change this to the IP address of your server
    server_port = 5555

    vote(server_address, server_port)
    get_results(server_address, server_port)