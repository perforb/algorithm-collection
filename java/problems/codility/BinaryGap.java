package codility;

// https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
public class BinaryGap {

    public static void main(String[] args) {
        int answer = new BinaryGap().solution(529); // 1000010001
        System.out.println(answer);
    }

    private int solution(int N) {
        String binary = Integer.toBinaryString(N);
        if (!hasBinaryGap(binary)) {
            return 0;
        }
        binary = normalize(binary);
        String[] gaps = binary.split("1");
        int count = 0;
        for (String gap : gaps) {
            int length = gap.length();
            if (count < length) {
                count = length;
            }
        }
        return count;
    }

    private boolean hasBinaryGap(String binary) {
        if (binary.length() < 3) {
            return false;
        }
        return binary.indexOf('0') >= 0 && binary.indexOf('1') >= 0;
    }

    private String normalize(String binary) {
        String[] numbers = binary.split("");
        StringBuilder builder = new StringBuilder(binary);
        int length = binary.length();
        for (int i = (length - 1); i > 0; i--) {
            if (numbers[i].equals("1")) {
                break;
            } else {
                builder.deleteCharAt(i);
            }
        }
        return builder.toString();
    }
}
