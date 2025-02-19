"""
File: simple_hash.py
Created Time: 2023-06-15
Author: Krahets (krahets@163.com)
"""


def add_hash(key: str) -> int:
    """加法哈希"""
    hash = 0
    modulus = 1000000007
    for c in key:
        hash += ord(c)
    return hash % modulus


def mul_hash(key: str) -> int:
    """乘法哈希"""
    hash = 0
    modulus = 1000000007
    for c in key:
        hash = 31 * hash + ord(c)
    return hash % modulus


def xor_hash(key: str) -> int:
    """异或哈希"""
    hash = 0
    modulus = 1000000007
    for c in key:
        hash ^= ord(c)
    return hash % modulus


def rot_hash(key: str) -> int:
    """旋转哈希"""
    hash = 0
    modulus = 1000000007
    for c in key:
        hash = (hash << 4) ^ (hash >> 28) ^ ord(c)
    return hash % modulus


"""Driver Code"""
if __name__ == "__main__":
    hash = add_hash("Hello 算法")
    print(f"加法哈希值为 {hash}")

    hash = mul_hash("Hello 算法")
    print(f"乘法哈希值为 {hash}")

    hash = xor_hash("Hello 算法")
    print(f"异或哈希值为 {hash}")

    hash = rot_hash("Hello 算法")
    print(f"旋转哈希值为 {hash}")
