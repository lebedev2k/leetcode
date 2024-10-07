def bitwiseComplement(n: int) -> int:
    bin_str = ""
    for c in bin(n)[2:]:
        bin_str += "1" if c == "0" else "0"
    return int(bin_str, 2)


assert bitwiseComplement(5) == 2
assert bitwiseComplement(7) == 0
assert bitwiseComplement(10) == 5