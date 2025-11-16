def read_sequences(filename):
    sequences = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 3:
                protein_name, organism, sequence = parts
                sequences.append({
                    'protein': protein_name,
                    'organism': organism,
                    'sequence': sequence
                })
    return sequences

def process_search(commands_file, sequences):
    with open(commands_file, 'r', encoding='utf-8') as cmd_file:
        operation_number = 1

        for line in cmd_file:
            if line.startswith('search'):
                _, query = line.strip().split('\t')
                found = []

                for entry in sequences:
                    if query in entry['sequence']:
                        found.append((entry['organism'], entry['protein']))

                # Вывод результата в консоль
                print(f"{operation_number:03d}   search   {query}")
                print("organism\t\t\t\tprotein")
                if found:
                    for organism, protein in found:
                        print(f"{organism}\t\t{protein}")
                else:
                    print("NOT FOUND")
                print("-" * 74)

                operation_number += 1

# Основной запуск
sequences = read_sequences("sequences.0.txt")
process_search("commands.0.txt", sequences)
