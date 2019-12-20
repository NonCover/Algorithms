/*
 * 农民工问题：
 *      有一块矩形土地，农民工需要把这一块土地均匀分成若干个长宽等距的且面积最大的小土地
 * 解决方案：
 *      欧几里得求解
 * */
public class FarmerProblem {
    static int DC(int Long, int Wide){
        if (Wide == 0) return Long;
        else return DC(Wide, Long % Wide);
    }
    public static void main(String[] args) {
        System.out.println(DC(168, 64));
    }
}
