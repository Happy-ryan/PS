n, m = map(int, input().split())
img1 = [list(input()) for _ in range(n)]
img2 = [list(input()) for _ in range(n)]

def solution(n, m, img1, img2):
    
    def resizeImg(num, img):
        resize_img = [[] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                for _ in range(num):
                    resize_img[i].append(img[i][j])
        return resize_img
    
    img = resizeImg(2, img1)

    if img == img2:
        return 'Eyfa'

    return 'Not Eyfa'

print(solution(n, m, img1, img2))