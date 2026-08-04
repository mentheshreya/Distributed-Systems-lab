import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        try {
            // Connect to server and keep same port number
            Socket socket = new Socket("localhost", 5000);

            // I/O Streams
            BufferedReader input = new BufferedReader(
                    new InputStreamReader(socket.getInputStream()));
            PrintWriter output = new PrintWriter(
                    socket.getOutputStream(), true);

            // Send message to server
            output.println("Hello Server!");

            // Receive message
            String response = input.readLine();
            System.out.println("Server: " + response);

            // Close 
            input.close();
            output.close();
            socket.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}