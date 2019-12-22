// 参考python注释
public class binary_search {
    public static void main(String[] args) {
        int[] nums = new int[]{1,3,4,5,6,7,10,13,14};
        int item = -1;
        int res = solution(nums, item);
        System.out.println(res);
    }
    public static int solution(int[] nums, int item){
        int low = 0;
        int high = nums.length;
        while (low <= high){
            int mid = (low + high) / 2;
            int guess = nums[mid];
            if (guess == item) {
                return mid;
            }else if (guess < item){
                low = mid + 1;
            }else if (guess > item){
                high = mid - 1;
            }
        }
        return -1;      // 没有该元素时 返回-1
    }
}