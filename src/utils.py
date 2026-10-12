def slugify(text: str) -> str:
    out = []
    for ch in text.strip().lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " \t-_":
            out.append("-")
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")

def safe_div(a: float, b: float) -> float:
    return a / b if b else 0.0

def month_key(year: int, month: int) -> str:
    return f"{year:04d}-{month:02d}"