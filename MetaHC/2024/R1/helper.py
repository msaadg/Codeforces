def read_input_file(input_filename):
  with open(input_filename, 'r') as file:
    data = file.readlines()
  return data

def write_output_file(output_filename, results):
  with open(output_filename, 'w') as file:
    for i, result in enumerate(results, 1):
      file.write(f"Case #{i}: {result}\n")

def solve(data):
  results = []
  idx = 0
  num_cases = int(data[idx])
  idx += 1

  for __ in range(num_cases):
    n, k = map(int, data[idx].split())
    idx += 1

  return results

if __name__ == "__main__":
  input_filename = "s.txt"
  output_filename = "output.txt"
  
  input_data = read_input_file(input_filename)
  output_data = solve(input_data)
  write_output_file(output_filename, output_data)
