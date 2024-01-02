file_path = input("File name: ")
file_path = file_path.strip().lower()
file_parts = file_path.split('.')
file_extension=file_parts[-1]
if file_extension=="gif":
    print("image/gif")
elif file_extension=="jpg" or file_extension=="jpeg":
    print("image/jpeg")
elif file_extension=="png":
    print("image/png")
elif file_extension=="pdf":
    print("application/pdf")
elif file_extension=="txt":
    print("text/plain")
elif file_extension=="zip":
    print("application/zip")
else:
    print("application/octet-stream")