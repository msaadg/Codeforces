def read_input_file(input_filename):
  with open(input_filename, 'r') as file:
    data = file.readlines()
  return data

def write_output_file(output_filename, results):
  with open(output_filename, 'w') as file:
    for i, result in enumerate(results, 1):
      file.write(f"Case #{i}: {result[1]} {result[0]}\n")

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
    
    for i in range(n):
      lst[i] += i
    
    lst.sort()

    for i in range(n):
      lst[-i - 1] -= i
    ans = (10**18, 10**18)
    for i in range(n):
      ans = min(ans, (abs(lst[i] - g), n - i))

    results.append(ans)
  return results

if __name__ == "__main__":
  input_filename = "s.txt"
  output_filename = "output.txt"
  
  input_data = read_input_file(input_filename)
  output_data = solve(input_data)
  write_output_file(output_filename, output_data)
