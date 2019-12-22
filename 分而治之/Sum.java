import java.util.ArrayList;
public class Sum {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        int[] arr = {2, 4, 5, 7, 9};
        for (int i: arr){
            list.add(i);
        }
        System.out.println(sum(list));
    }
    // 分而治之 递归
    private static int sum(ArrayList<Integer> list){
        if (list.size() == 1) {
            return list.get(0);
        }
        return list.remove(0) + sum(list);
        // 2 + sum(4 + sum(4 + ***))
    }
}
