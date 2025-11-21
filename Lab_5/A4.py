from collections import Counter
def load_sequences(filename):
    proteins = {}
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                name, organism, seq = line.strip().split("\t")
                proteins[name] = {"organism": organism, "seq": seq}
    return proteins
def search(seq, proteins):
    return "\n".join(f"{d['organism']}\t\t{name}"
                     for name, d in proteins.items() if seq in d["seq"]) or "NOT FOUND"
def diff(p1, p2, proteins):
    if p1 not in proteins or p2 not in proteins:
        return f"MISSING: {', '.join(p for p in (p1, p2) if p not in proteins)}"
    s1, s2 = proteins[p1]["seq"], proteins[p2]["seq"]
    return str(sum(a != b for a, b in zip(s1, s2)) + abs(len(s1) - len(s2)))
def mode(p, proteins):
    if p not in proteins:
        return f"MISSING: {p}"
    counter = Counter(proteins[p]["seq"]) #взять белок с именем p из словаря proteins и получить его аминокислотную последовательность
    max_count = max(counter.values())
    aa = min(k for k, v in counter.items() if v == max_count)
    return f"{aa}          {max_count}"
def main():
    proteins = load_sequences("sequences.0.txt")
    with open("commands.0.txt", encoding="utf-8") as f:
        commands = [line.strip().split("\t") for line in f if line.strip()]
    output = ["Dwight Barnette", "Genetic Searching"]
    for i, cmd in enumerate(commands, 1):
        op_id = str(i).zfill(3)
        output.append("-" * 74)
        if cmd[0] == "search":
            output += [f"{op_id}   search   {cmd[1]} ",
                       "organism\t\t\t\tprotein ",
                       search(cmd[1], proteins)]
        elif cmd[0] == "diff":
            output += [f"{op_id}   diff   {cmd[1]}   {cmd[2]} ",
                       "amino-acids difference: ",
                       diff(cmd[1], cmd[2], proteins)]
        elif cmd[0] == "mode":
            output += [f"{op_id}   mode   {cmd[1]}  ",
                       "amino-acid occurs: ",
                       mode(cmd[1], proteins)]
        else:
            output.append(f"{op_id} UNKNOWN COMMAND")
    output.append("-" * 74)
    with open("genedata.txt", "w", encoding="utf-8") as out:
        out.write("\n".join(output))
    # печать результата
    with open("genedata.txt", encoding="utf-8") as f:
        print(f.read().strip())
if __name__ == "__main__":
    main()
