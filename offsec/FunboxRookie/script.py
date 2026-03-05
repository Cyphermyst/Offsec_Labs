#!/usr/bin/env python3

import subprocess
import os

# Output file for john
OUTPUT_FILE = "all_hashes.txt"

def extract_hash(zip_file):
    """
    Runs zip2john on a single zip file
    Returns extracted hash as string
    """
    try:
        result = subprocess.run(
            ["zip2john", zip_file],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"[!] Error processing {zip_file}: {e}")
        return None


def main():
    zip_files = [f for f in os.listdir(".") if f.endswith(".zip")]

    if not zip_files:
        print("[!] No zip files found in current directory.")
        return

    print(f"[+] Found {len(zip_files)} zip files.")

    with open(OUTPUT_FILE, "w") as outfile:
        for zip_file in zip_files:
            print(f"[+] Extracting hash from {zip_file}")
            hash_output = extract_hash(zip_file)

            if hash_output:
                outfile.write(hash_output + "\n")

    print(f"[+] All hashes saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
