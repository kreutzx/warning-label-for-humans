import os

# One-line warning label entry for humans.
ENTRY_TEXT = "WARNING: Contents under pressure. May form a lifelong opinion from one headline. Not rated for comment sections after midnight."


def main():
    # Ensure the output directory exists before writing the entry.
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
