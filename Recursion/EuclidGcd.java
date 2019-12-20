/*
    欧几里得求最大公约数又称辗转相除法
    例如： 36 和 15的最大公约数：
        36 一直减去 15，直到无法再减，取余也就是 6。
        再用 15 一直减去 6， 取余也就是 3
        用 6 一直减去 3， 余数为 0
        当余数为 0 时， 3 也就是 36 和 15 的 最大公约数
*/
public class EuclidGcd {
    static int gcd(int a, int b){
        /// a > b
        if (b == 0) return a;
        else return gcd(b, a % b);    }

    public static void main(String[] args) {
        /// 欧几里得 求 最大公约数
        int res = gcd(36, 15);
        System.out.println(res);
    }
}
