from concurrent import futures
import grpc
import chat_pb2
import chat_pb2_grpc

class ChatServiceServicer(chat_pb2_grpc.ChatServiceServicer):
    def SendMessage(self, request, context):
        print(f"\n[RECEIVED] From: {request.sender} | Message: {request.message}")
        
        # Build and return response
        return chat_pb2.ServerResponse(
            status="200 OK",
            reply=f"Ack from server: Received message from '{request.sender}'."
        )

def serve():
    # Instantiate multi-threaded server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatServiceServicer(), server)
    
    # Listen on all network interfaces on port 50051
    server.add_insecure_port('[::]:50051')
    print("gRPC Server is listening on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()