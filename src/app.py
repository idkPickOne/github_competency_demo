def greet(name: str) -> str:
    name = (name or "").strip() or "world"
    return f"Hello, {name}!"
