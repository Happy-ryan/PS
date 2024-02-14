import java.util.*;

class leafNode {
    char left, right;

    public leafNode(char left, char right) {
        this.left = left;
        this.right = right;
    }
}

public class Main {
    private static int n;
    private static Map<Character, leafNode> tree = new HashMap<>();
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < n; i++) {
            String row = sc.nextLine();
            char root = row.charAt(0);
            char left = row.charAt(2);
            char right = row.charAt(4);
            tree.put(root, new leafNode(left, right));
        }
        char rootNode = 'A';

        preOrder(rootNode);
        sb.append('\n');
        inOrder(rootNode);
        sb.append('\n');
        postOrder(rootNode);

        System.out.print(sb);
    }

    private static void preOrder(char rootNode) {
        char left = tree.get(rootNode).left;
        char right = tree.get(rootNode).right;

        if (left == '.' && right == '.') {
            sb.append(rootNode);
            return;
        }

        sb.append(rootNode);

        if (left != '.') {
            preOrder(left);
        }

        if (right != '.') {
            preOrder(right);
        }

    }

    private static void inOrder(char rootNode) {
        char left = tree.get(rootNode).left;
        char right = tree.get(rootNode).right;

        if (left == '.' && right == '.') {
            sb.append(rootNode);
            return;
        }

        if (left != '.') {
            inOrder(left);
        }

        sb.append(rootNode);

        if (right != '.') {
            inOrder(right);
        }
    }

    private static void postOrder(char rootNode) {
        char left = tree.get(rootNode).left;
        char right = tree.get(rootNode).right;

        if (left == '.' && right == '.') {
            sb.append(rootNode);
            return;
        }

        if (left != '.') {
            postOrder(left);
        }

        if (right != '.') {
            postOrder(right);
        }

        sb.append(rootNode);
    }

}