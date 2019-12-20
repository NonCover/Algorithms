public class Tail_recursion {
    public static int func(int num, int value){
        if (num == 1){
            return value;
        }else{
            return func(num - 1, value * num);  // 每次递归时，当前函数出队
        }
    }
    public static void main(String[] args) {
        System.out.printf(String.valueOf(func(5, 1)));
    }
}
