import base64

def decode_base64_file(input_file):
  try:
    with open(input_file, 'r') as file:
      encoded_data = file_read()
   
    decoded_data = base64.b64decode(encoded_data).decode('utf-8')

    print(decoded_data)

  except Exception as e:
    print(f"An error has occourred: {e}")

if __name__ == "__main__":
    input_file = input("Path to file: ")
    decode_base64_file(input_file)
