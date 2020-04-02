import java.util.*;
class dis{
    public static int binary(int a ,int b){
        return (int)(a+b)/2;
    }
    public static int check(int arr[],int k,int s){
        int max_till_now=0,sum_till_now=0,count=1;
        int n=arr.length;
        for(int i=0;i<n;i++){
            if(sum_till_now+arr[i]<s){
                sum_till_now+=arr[i];
            }
            else{
                count++;
                if(max_till_now<sum_till_now)max_till_now=sum_till_now;
                sum_till_now=arr[i];
            }
        }
        // System.out.println(max_till_now);
        if (count==k){
            return max_till_now;
        }
        else if(count<k) return 2;
        else return 0;

    }
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        for(int temp=0;temp<t;temp++){
            int n=sc.nextInt();
        int k=sc.nextInt();
        int arr[]=new int[n];
        int sum=0,max=0;
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
            sum+=arr[i];
            if(max<arr[i]){
                max=arr[i];
            }
        }
        int a=max;
        int b=sum;
        // System.out.println(a+" "+b);
        while(true){
            
            int s=binary(a,b);
            System.out.println("FOR"+s);
            int res=check(arr,k,s);
            if(res==2) b=s;
            else if(res==0) {a=s;}
            else {
                System.out.println(res);
                break;
            }

        }
        }
    }
}