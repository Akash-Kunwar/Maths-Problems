//BRUTE FORCE METHOD

import java.util.*;
class party_dislike {
    public static void main(String args[] ) throws Exception {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int arr[][]=new int [n][n];
        for(int i=0;i<10;i++){
            int row=sc.nextInt();
            for(int j=0;j<9;j++){
                
                int col=sc.nextInt();
                arr[row-1][col-1]=1;
                arr[col-1][row-1]=1;
            }
        }
        int count=0;
        for (int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i==j) arr[i][j]=1;
                if(arr[i][j]==0)count++;
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    
        System.out.println(count/2);

    }
}
