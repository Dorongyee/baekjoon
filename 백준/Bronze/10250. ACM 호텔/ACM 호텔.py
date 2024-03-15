for _ in range(int(input())):
    h, w, n = map(int, input().split())
    floor = n % h
    floor = h if floor == 0 else floor # 최상층 배정 예외
    room_number = (n - 1) // h + 1  
    
    print(f"{floor}{room_number:02d}")
