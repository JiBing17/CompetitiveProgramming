// Author: Ji Bing Ni
// It is not ok to share my code anonymously for educational purposes
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException; 
import java.io.InputStreamReader; 
import java.util.Scanner; 
import java.util.StringTokenizer; 
import java.util.TreeMap;
import java.util.Arrays;

public class SoundOfSilence {

    
static class FastReader { // fast io template
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
    public static void main(String[] args) throws IOException{

        FastReader fr = new FastReader();
        String s = fr.nextLine();
        

        System.out.println(s);
        String [] temp = s.split(" ");


        int length = Integer.parseInt(temp[1]);
        int threshold = Integer.parseInt(temp[2]);


        String s2 = fr.nextLine();

        String [] temp2 = s2.split(" ");
        int [] data = new int[temp2.length];
        int count = 0;
        // type cast for accessibility
        for (int i = 0; i < temp2.length; i++) {
            data[i] = Integer.parseInt(temp2[i]);
        }
        
        // data structure used for getting max and min val
        TreeMap<Integer, Integer> tm = new TreeMap<>();
        
        int left = 0;
        int right = left + length;

        // add all number inside left and rigth pointer
        for (int i = left; i < right; i++) {
            if (tm.containsKey(data[i])) {
                int ref = tm.get(data[i]);
                int newRef = ref + 1;
                tm.replace(data[i], ref, newRef);
            } else {
                tm.put(data[i], 1);
            }
        }

        while (right != data.length + 1 ) {
            
            int biggest = tm.lastKey();
            int smallest = tm.firstKey();
            int res = biggest - smallest;

            // valid case
            if (res <= threshold) {
                // plus 1 since index val
                System.out.println(left + 1);
                count++;
            }  
            int val = tm.get(data[left]);
            // remove 1 ref
            if (val > 1) {
                tm.replace(data[left], val, val -1);
            // remove whole 
            } else {
                tm.remove(data[left]);
            }

            left++;

            // add to ref count if there 
            if (right != data.length && tm.containsKey(data[right])) {
                tm.replace(data[right],tm.get(data[right]), tm.get(data[right]) + 1 );
            // add new key / val
            } else if (right != data.length) {
                tm.put(data[right], 1); 
            }
            
            right++;  

        }
        if (count == 0) {
            System.out.println("NONE");
        }
        //input.close();
    }
  }