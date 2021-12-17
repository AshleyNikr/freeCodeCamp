import hashlib

def crack_sha1_hash(hash, use_salts=False):
  password_hashes = {}
  with open("top-10000-passwords.txt") as file:
    for line in file:
      line = line.strip()
      if use_salts == False:
        password_hashes[hashlib.sha1(line.encode()).hexdigest()] = line
      else:
        with open("known-salts.txt") as salt_file:
          orig = line
          for salt in salt_file:
            line = salt.strip() + orig
            password_hashes[hashlib.sha1(line.encode()).hexdigest()] = orig
            line = orig + salt.strip()
            password_hashes[hashlib.sha1(line.encode()).hexdigest()] = orig
  
  if hash in password_hashes.keys():
    return password_hashes[hash]
  else:
    return "PASSWORD NOT IN DATABASE"