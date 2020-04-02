import java.util.*;

class TestClass {
    public static int gcd(int a, int b)  
    {  
    while (a != b)  
    {  
        if (a > b)      
            a = a - b;      
        else    
            b = b - a;      
    }  
    return a;  
    }  
    public static void main(String args[] ) throws Exception {
        Scanner sc=new Scanner(System.in);
        int x,y,p,q,b1,b2,b3;
        x=sc.nextInt();
        y=sc.nextInt();
        p=sc.nextInt();
        q=sc.nextInt();
        b1=p*y;
        b2=q*x;
        int gcd=gcd(b1,b2);
        b1=b1/gcd;
        b2=b2/gcd;
        b3=(x*b1+y*b2)/(p+q);
        System.out.println(b1+" "+b2+" "+b3);
        
        

    }
}
