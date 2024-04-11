import mimetypes

def read_file(filename: str) -> bytes:
    with open(filename, 'rb') as file:
        return file.read()

def write_file(data: bytes, location: str) -> None:
    with open(location, 'wb') as file:
        file.write(data)

def identify_file_type(filename: str) -> str:
    # Use the mimetypes module to identify the file type based on its extension
    mime_type, _ = mimetypes.guess_type(filename)
    if mime_type:
        return mime_type
    else:
        # If the mimetype is not recognized, return a generic binary type
        return 'application/octet-stream'
