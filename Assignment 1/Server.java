import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        try {
            // Create Server Socket on port 5000
            ServerSocket serverSocket = new ServerSocket(5000);
            System.out.println("Server is waiting for client...");

            // Accept client connection
            Socket socket = serverSocket.accept();
            System.out.println("Client connected!");

            // Input and Output Streams
            BufferedReader input = new BufferedReader(
                    new InputStreamReader(socket.getInputStream()));
            PrintWriter output = new PrintWriter(
                    socket.getOutputStream(), true);

            // Receive message from client
            String message = input.readLine();
            System.out.println("Client: " + message);

            // Send response
            output.println("Hello Client! Message received successfully.");

           
            input.close();
            output.close();
            socket.close();
            serverSocket.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}