import grpc
import chat_pb2
import chat_pb2_grpc

def run():
    # Establish insecure channel to server node
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = chat_pb2_grpc.ChatServiceStub(channel)
        
        # Create request payload
        request = chat_pb2.ClientMessage(
            sender="Node-Alpha",
            message="Hello Server, this is distributed node Alpha!"
        )
        
        print(f" Sending message to gRPC Server...")
        response = stub.SendMessage(request)
        
        # Process server response
        print(f"[SERVER STATUS]: {response.status}")
        print(f"[SERVER REPLY] : {response.reply}")

if __name__ == '__main__':
    run()