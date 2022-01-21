def prime_finder(n):
  # Write your code here
  n = int(n)
  outgoing_primes = []

  ######FUNCTIONS######

  # 6K +- 1 Theory Populator
  def populator(n):   
    pointer = 0
    while n > pointer:
      for number in range(1, n):
        temp_no = (6*number)
        lo_hi = [(temp_no - 1), (temp_no + 1)]
        lo = lo_hi[0]
        hi = lo_hi[1]
        pointer = hi
        lo_hi_tester(lo, hi)
        if pointer >= n:
          break

  # pass/fail prime number tester
  def lo_hi_tester(lo, hi):
    # to test low input value
    lo_test = 0

    for prime in outgoing_primes:
      if lo % prime == 0:
          lo_test += 1
      
    if lo_test == 0:
        outgoing_primes.append(lo)

    # to test high input values
    hi_test = 0

    for prime in outgoing_primes:
      if hi % prime == 0:
          hi_test += 1
      
    if hi_test == 0:
        outgoing_primes.append(hi)

  # output trimmer
  def popper(list_name, index):
    if index <= list_name[-1]:
      list_name.pop()
  
  #########CODE#########
  if n < 2:
    return "There are no prime numbers in that range."
  elif n <= 11:
    if n == 2:
      outgoing_primes += [2]     
    if n == 3 or n == 4:
      outgoing_primes += 2, 3
    if n == 5 or n == 6:
      outgoing_primes += 2, 3, 5  
    if n == 7 or n == 8 or n == 9 or n == 10:
      outgoing_primes += 2, 3, 5, 7    
    if n == 11:
      outgoing_primes += 2, 3, 5, 7, 11
  elif n >= 12:
    outgoing_primes += [2, 3, 5]
    populator(n)
    while outgoing_primes[-1] > n:
      popper(outgoing_primes, n)
    
  return outgoing_primes


print(prime_finder(11))