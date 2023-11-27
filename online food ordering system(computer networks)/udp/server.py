import socket

# Dictionary to store candidate votes
candidate_votes = {
    "Candidate1": 0,
    "Candidate2": 0,
    "Candidate3": 0
}

def handle_request(data, client_address, server_socket):
    request = data.decode('utf-8')
    if request == 'VOTE':
        vote_for_candidate(client_address, server_socket)
    elif request == 'RESULTS':
        get_results(client_address, server_socket)
    else:
        server_socket.sendto("Invalid request".encode('utf-8'), client_address)

def vote_for_candidate(client_address, server_socket):
    server_socket.sendto("Candidates: Candidate1, Candidate2, Candidate3".encode('utf-8'), client_address)
    candidate_name, _ = server_socket.recvfrom(1024)
    candidate_name = candidate_name.decode('utf-8')

    if candidate_name in candidate_votes:
        candidate_votes[candidate_name] += 1
        server_socket.sendto(f"Vote for {candidate_name} recorded.".encode('utf-8'), client_address)
    else:
        server_socket.sendto("Invalid candidate name.".encode('utf-8'), client_address)

def get_results(client_address, server_socket):
    results = "\n".join(f"{candidate}: {votes}" for candidate, votes in candidate_votes.items())
    server_socket.sendto(results.encode('utf-8'), client_address)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 5555))

    print("[INFO] Server listening on port 5555")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        handle_request(data, client_address, server_socket)

if __name__ == "__main__":
    start_server()
