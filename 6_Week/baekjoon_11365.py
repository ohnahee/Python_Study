# Day 33

def decode_messages():
    input_lines = []
    while True:
        line = input()
        if line == "END":
            break
        input_lines.append(line)
    
    decoded_lines = [line[::-1] for line in input_lines]
    
    for line in decoded_lines:
        print(line)

decode_messages()
