def isHappy(n):
    """
    Return True if n is a happy number, and False if not.
    """
    a = []
    while n != 1:
        if n in a:
            return False
        a.append(n)
        b = str(n)
        n = 0
        for j in b:
            n += int(j) ** 2
    return True

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
    print("Results saved to /app/bind_mount/output.txt")
