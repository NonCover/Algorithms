import java.util.Arrays;

public class quickSort {
    public static void main(String[] args) {
        int[] a = {3,1,5,2};
        System.out.println(Arrays.toString(a));
        quicksort(a);
        System.out.println(Arrays.toString(a));
    }

    public static void quicksort(int[] a) {
        if(a.length>0) {
            quicksort(a, 0 , a.length-1);
        }
    }

    private static void quicksort(int[] a, int low, int high) {
        //1,找到递归算法的出口
        if( low > high) {
            return;
        }
        //2, 存
        int i = low;
        int j = high;
        //3, 用来比较大小的一个值
        int key = a[low];
        //4，完成一趟排序
        while( i< j) {
            //4.1 ，从右往左找到第一个小于key的数
            while(i<j && a[j] > key){
                j--;
            }
            // 4.2 从左往右找到第一个大于key的数
            while( i<j && a[i] <= key) {
                i++;
            }
            //4.3 交换 a[i] 和 a[j] 的位置
            // 将右边第一个比 key 小的和左边第一个比 key 大的交换
            if(i < j) {
                int p = a[i];
                a[i] = a[j];
                a[j] = p;
            }
        }
        System.out.println(Arrays.toString(a));
        // 4.4，调整key的位置
        int p = a[i];
        a[i] = a[low];
        a[low] = p;
        //5, 对key左边的数快排
        quicksort(a, low, i-1 );
        //6, 对key右边的数快排
        quicksort(a, i+1, high);
    }
}