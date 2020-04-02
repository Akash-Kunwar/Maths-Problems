import java.io.*;
import java.util.*;


public class TestClass {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter wr = new PrintWriter(System.out);
        int testcase = Integer.parseInt(br.readLine().trim());
        for(int t_i=0; t_i<testcase; t_i++)
        {
            String S = br.readLine();
            String T = br.readLine();

            int out_ = Maximum(S, T);
            System.out.println(out_);
         }

         wr.close();
         br.close();
    }
    static int Maximum(String S, String T){
        int flag=1;
        int count=0;
        int slen=S.length();
        int tlen=T.length();
        char s1[],s2[];
        if(slen>tlen){

            s1=new char[tlen];
            S.getChars(0,tlen,s1,0);
            s2=T.toCharArray();

        }
        else{
            s1=S.toCharArray();
            s2=T.toCharArray();
        }
        

        if(true){
            HashMap<Character,Integer> hm =new HashMap<Character,Integer>();
            for(char c :s1){
                if(hm.containsKey(c)){
                    int val=hm.get(c);
                    hm.put(c,val+1);
                }
                else{
                    hm.put(c,1);
                }
            }
            for(char c :s2){
                if(hm.containsKey(c) && hm.get(c)!=0){
                    int val=hm.get(c);
                    hm.put(c,val-1);
                    count++;
                }
            }

        }
        else{

        }
        // System.out.println(count);
        return count;



        
    
    }
}