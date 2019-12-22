import java.util.Arrays;
public class selection_sort {
    public static void main(String[] args) {
        int[] arr = {4,2,6,8,3,9};
        arr = solution(arr, arr.length);
        System.out.println(Arrays.toString(arr));
    }

    // 找到数组的最小值，并返回下标
    public static int findSmallest(int[] arr) {
        int smallest = arr[0];
        int smallest_index = 0;
        for (int i = 1; i < arr.length; i++){
            if (arr[i] < smallest){
                smallest = arr[i];
                smallest_index = i;
            }
        }
        return smallest_index;
    }

    // 删除最小值
    static int[] del(int[] arr, int e){
        arr[e] = arr[arr.length - 1];     // 将最后一个值赋值给要删除
        arr = Arrays.copyOf(arr, arr.length - 1);
        return arr;
    }

    public static int[] solution(int[] arr, int arrLength) {
        int[] newArr = new int[arrLength];
        int smallest;
        int n = arr.length;
        for (int i = 0; i < n; i++){
            smallest = findSmallest(arr);
            newArr[i] = arr[smallest];

            arr = del(arr, smallest);
        }
        return newArr;
    }
}
