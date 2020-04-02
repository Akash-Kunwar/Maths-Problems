import java.io.*;
import java.util.*;


public class TestClass {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter wr = new PrintWriter(System.out);
        int T = Integer.parseInt(br.readLine().trim());
        for(int t_i=0; t_i<T; t_i++)
        {
            String[] NK = br.readLine().split(" ");
            int N = Integer.parseInt(NK[0]);
            int K = Integer.parseInt(NK[1]);
            String[] arr_arr = br.readLine().split(" ");
            int[] arr = new int[N];
            for(int i_arr=0; i_arr<arr_arr.length; i_arr++)
            {
            	arr[i_arr] = Integer.parseInt(arr_arr[i_arr]);
            }

            int out_ = Solution(N, K, arr);
            System.out.println(out_);
         }

         wr.close();
         br.close();
    }
    public static int ksum(int arr[],int n,int k){
        int min=99999;
        int sum=0,m=0;
        for(int i=0;i<n;i++){
            sum=0;
            for(int j=i;j<n;j++){
                sum+=arr[j];
                if(sum==k){
                    if(j-i+1<min){
                        min=j-i+1;
                    }
                    break;
                } 
            }
        }
        return min;
    }
    static int Solution(int n, int k, int[] arr){
        
        int sum=0;
        for(int i :arr) sum+=i;
        int count=k;
        while(count<sum){
            int ans=ksum(arr,n,count);
            if(ans!=99999){
                return ans;
            }
            count+=k;


        }
        return -1;
    }
}