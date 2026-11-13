import os
import sys

def main():
    """Writes the AI joke to the specified output directory."""
    joke = "My agent’s 'I fixed it' message is just a polite way of saying 'I moved the bug to a line of code you never read.'"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    # Ensure output file is written with explicit UTF-8 encoding
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(joke)

if __name__ == "__main__":
    main()
