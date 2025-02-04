// Author: Ji Bing Ni
// It is not ok to share my code anonymously for educational purposes

import java.io.*;
import java.util.*;

public class Ascent {

    // Comparator to compare arrays based on their elements
    static Comparator<int[]> comp = new Comparator<int[]>() {
        public int compare(int[] a, int[] b) {
            // Comparing arrays element-wise
            for (int i=0; i<a.length; i++) {
                if (a[i] < b[i])       return -1; 
                else if (a[i] > b[i])  return 1; 
            }
            return 0;
        }
    };

    public static void main(String[] args) throws IOException {
        
        FastReader in = new FastReader();  
        PrintWriter out = new PrintWriter(System.out); 
        double a = in.nextDouble(); 
        double b = in.nextDouble(); 
        int shields = in.nextInt(); 

        // DSAs used to store coordinates and corresponding factors
        HashMap<double[], Double> hash = new HashMap<>();
        ArrayList<double[]> coords = new ArrayList<>();
        double [] factor = new double[shields];

        // Loop to read shield coordinates and factors
        for (int i = 0; i < shields; i++) {
            double [] coord = new double[2];
            coord[0] = in.nextDouble(); 
            coord[1] = in.nextDouble(); 
            coords.add(coord); 
            factor[i] = in.nextDouble(); 
            hash.put(coord, factor[i]); 
        }

        // Sorting based on x-values
        coords.sort(Comparator.comparingDouble(array -> array[0]));

        // Calculating impact on 'b' due to each shield
        for (int i = 0; i < shields; i++) {
            double dist = coords.get(i)[1] - coords.get(i)[0]; 
            double change = dist * hash.get(coords.get(i)); 
            double changevert = dist - change;
            b -= changevert;
        }
        
        double result = a / b;
        out.println(result); 
        out.close(); 
    }

    /* FastReader code from Method 4 in the post https://www.geeksforgeeks.org/fast-io-in-java-in-competitive-programming/
       Modified nextLine() to allow arbitrary long lines,
       Modified fillBuffer(), read() to fix some issues
       Added next(), and hasNext()
       Use nextInt(), nextLong(), or nextDouble() to read numbers
       Use next() to read a string.
       Use nextLine() to read in the next line that is not empty (i.e., it
           contains at least one character that is > 32 (' ').
    */
    static class FastReader {
        final private int BUFFER_SIZE = 1 << 16;
        private int MAX_LINE_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer, lineBuf;
        private int bufferPointer, bytesRead;

        public FastReader() {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            lineBuf = new byte[MAX_LINE_SIZE];
            bufferPointer = bytesRead = 0;
        }
        public FastReader(String file_name) throws IOException {
            din = new DataInputStream(new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
        public boolean hasNext() throws IOException {
            byte c;
            while ((c = read()) != -1) {
                if (c > ' ') {      // Find first byte bigger than ' '
                    bufferPointer--;
                    return true;
                }
            }
            return false;
        }
        // return the next line that contains at least one character > ' '
        public String nextLine() throws IOException {
            int ctr = 0;
            byte c;
            boolean empty = true;
            while ((c = read()) != -1) {
                if (c == '\r')        continue;     // ignore '\r'
                if (c == '\n') {
                    if (empty)  { ctr = 0;   continue;  } // read only spaces etc. until \n
                    else        break;
                }
                if (ctr == MAX_LINE_SIZE) {
                    MAX_LINE_SIZE *= 2;
                    lineBuf = Arrays.copyOf(lineBuf, MAX_LINE_SIZE);
                }
                lineBuf[ctr++] = c;
                if (c > ' ')  empty = false;
            }
            return new String(lineBuf, 0, ctr);
        }
        public String next() throws IOException {
            int ctr = 0;
            byte c = read();
            while (c <= ' ')    c = read();
            while (c > ' ') {
                if (ctr == MAX_LINE_SIZE) {
                    MAX_LINE_SIZE *= 2;
                    lineBuf = Arrays.copyOf(lineBuf, MAX_LINE_SIZE);
                }
                lineBuf[ctr++] = c;
                c = read();
            }
            return new String(lineBuf, 0, ctr);
        }
        public int nextInt() throws IOException {
            int ret = 0;
            byte c = read();
            while (c <= ' ')   c = read();
            boolean neg = (c == '-');
            if (neg)           c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');

            if (neg)           return -ret;
            return ret;
        }
        public long nextLong() throws IOException {
            long ret = 0;
            byte c = read();
            while (c <= ' ')    c = read();
            boolean neg = (c == '-');
            if (neg)            c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (neg)            return -ret;
            return ret;
        }
        public double nextDouble() throws IOException {
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)    c = read();
            do {
                ret = ret * 10 + c - '0';
            }
            while ((c = read()) >= '0' && c <= '9');
            if (c == '.') {
                while ((c = read()) >= '0' && c <= '9') {
                    ret += (c - '0') / (div *= 10);
                }
            }
            if (neg)     return -ret;
            return ret;
        }
        private void fillBuffer() throws IOException {
            bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
        }
        private byte read() throws IOException {
            if (bufferPointer == bytesRead)     fillBuffer();
            if (bytesRead <= 0)  return -1;  // No data
            return buffer[bufferPointer++];
        }
        public void close() throws IOException {
            if (din == null)       return;
            din.close();
        }
    }
}
