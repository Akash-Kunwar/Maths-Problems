import java.util.*;
class array{
    public static void main(String args[]){
        int arr[]=new int[]{99,25,93,0,50,65,7,85,9,10};
        // Arrays.sort(arr);
        // System.out.println(Arrays.binarySearch(arr,99));
        // for(int i=0;i<arr.length;i++){
        //     System.out.println(arr[i]);
        // }
        Collections.reverse(Arrays.asList(arr));
        for(int i=0;i<arr.length;i++){
            System.out.println(arr[i]);
        }
    }
}