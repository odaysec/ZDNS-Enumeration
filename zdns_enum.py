import subprocess
import argparse
import json
import os

def run_zdns(domain, wordlist, output_file, query_type="A"):
    """Menjalankan ZDNS dengan wordlist untuk mendapatkan hasil enumerasi DNS."""
    if not os.path.exists(wordlist):
        print(f"[ERROR] Wordlist {wordlist} tidak ditemukan!")
        return

    with open(wordlist, "r") as file:
        subdomains = file.read().splitlines()
    
    print(f"[INFO] Menjalankan ZDNS pada {domain} dengan {len(subdomains)} subdomain...")

    command = f"zdns {query_type} --name-servers=8.8.8.8 --input-file={wordlist} --output-file={output_file}"
    process = subprocess.run(command, shell=True, capture_output=True, text=True)

    if process.returncode != 0:
        print(f"[ERROR] Gagal menjalankan ZDNS: {process.stderr}")
        return
    
    print(f"[SUCCESS] Hasil tersimpan di {output_file}")

def parse_output(output_file):
    """Parsing hasil output JSON dari ZDNS untuk analisis lebih lanjut."""
    if not os.path.exists(output_file):
        print(f"[ERROR] File output {output_file} tidak ditemukan!")
        return

    with open(output_file, "r") as file:
        data = [json.loads(line) for line in file.readlines()]

    print(f"\n[RESULT] Hasil Resolusi DNS:\n" + "=" * 40)
    for entry in data:
        if "data" in entry and "answers" in entry["data"]:
            for answer in entry["data"]["answers"]:
                print(f"{entry['name']} -> {answer['answer']} ({answer['type']})")

def main():
    parser = argparse.ArgumentParser(description="ZDNS Enumeration Automation Tool")
    parser.add_argument("-d", "--domain", required=True, help="Domain target")
    parser.add_argument("-w", "--wordlist", required=True, help="File wordlist subdomain")
    parser.add_argument("-o", "--output", required=True, help="File output hasil ZDNS")
    parser.add_argument("-t", "--type", default="A", help="Tipe query DNS (A, CNAME, MX, NS, dll.)")

    args = parser.parse_args()
    run_zdns(args.domain, args.wordlist, args.output, args.type)
    parse_output(args.output)

if __name__ == "__main__":
    main()
