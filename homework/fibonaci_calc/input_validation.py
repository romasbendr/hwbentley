from flask import abort

def query_validation(n: str|int) -> int:
    """Ensures input value n is castable to int and n>0"""
    try:
        n = int(n)
    except ValueError:
        abort(400, f"Bad input value. Expected n greater than 0, but got {n}")
    
    if n < 0:
            abort(400, "Input must be higher or equal to 0")

    return n
    