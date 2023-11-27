import socket
import threading

# Dictionary to store candidate votes
candidate_votes = {
    "Candidate1": 0,
    "Candidate2": 0,
    "Candidate3": 0
}

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    if request == 'VOTE':
        vote_for_candidate(client_socket)
    elif request == 'RESULTS':
        get_results(client_socket)
    else:
        client_socket.send("Invalid request".encode('utf-8'))
   
    client_socket.close()

def vote_for_candidate(client_socket):
    client_socket.send("Candidates: Candidate1, Candidate2, Candidate3".encode('utf-8'))
    candidate_name = client_socket.recv(1024).decode('utf-8')

    if candidate_name in candidate_votes:
        candidate_votes[candidate_name] += 1
        client_socket.send(f"Vote for {candidate_name} recorded.".encode('utf-8'))
    else:
        client_socket.send("Invalid candidate name.".encode('utf-8'))

def get_results(client_socket):
    results = "\n".join(f"{candidate}: {votes}" for candidate, votes in candidate_votes.items())
    client_socket.send(results.encode('utf-8'))

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)

    print("[INFO] Server listening on port 5555")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
