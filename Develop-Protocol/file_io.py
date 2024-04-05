def read_file(filename: str) -> bytes:
    with open(filename, 'rb') as file:
        return file.read()

def write_file(data: bytes, location: str) -> None:
    with open(location, 'wb') as file:
        file.write(data)

