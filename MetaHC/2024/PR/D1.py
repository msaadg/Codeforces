def read_input_file(input_filename):
  with open(input_filename, 'r') as file:
    data = file.readlines()
  return data

def write_output_file(output_filename, results):
  with open(output_filename, 'w') as file:
    for i, result in enumerate(results, 1):
      file.write(f"Case #{i}: {result[0], result[1]}\n")

def solve(data):
  results = []
  idx = 0
  num_cases = int(data[idx])
  idx += 1

  for __ in range(num_cases):
    n, g = map(int, data[idx].split())
    idx += 1

    lst = []
    for i in range(n):
      lst.append(int(data[idx]))
      idx += 1
    
    right = 0
    m = 10 ** 7

    val = -1
    for i in range(n):
      if lst[i] > g:
        right += 1
      if abs(lst[i] - g) < m:
        m = abs(lst[i] - g)
        val = lst[i]
    
    if val <= g:
      results.append([right + 1, m])
    else:
      results.append([right, m])

  return results

if __name__ == "__main__":
  input_filename = "s.txt"
  output_filename = "output.txt"
  
  input_data = read_input_file(input_filename)
  output_data = solve(input_data)
  write_output_file(output_filename, output_data)
