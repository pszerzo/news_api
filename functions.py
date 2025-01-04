import smtplib
import ssl
import os
import zipfile
import pathlib

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read text file and return list of that"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write text file"""
    with open(filepath, "w") as file_local:
        newtodos = file_local.writelines(todos_arg)

# if __name__ == "__main__": #only runs when it's runned from here and not imported
#     print("hello")


def archive_file(filepaths, dest_dir):
    """creates zip file"""
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

# #test function with given parameters
# if __name__ == "__main__":
#     archive_file(filepaths=["another.py", "quiz.py"], dest_dir="../dest")


def extract_archive(filepaths, dest_dir):
    """opens zip files"""
    # dest_path = pathlib.Path(dest_dir)
    with zipfile.ZipFile(filepaths, "r") as extract:
        for filepath in filepaths:
            # filepath = pathlib.Path(filepath)
            extract.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive(filepaths="/Users/Surface/PycharmProjects"
                              "/myapp/dest/compressed.zip", dest_dir="/Users/Surface/PycharmProjects/myapp/dest")


def send_email(message, receiver="peterszerzo@gmail.com", username="peterszerzo@gmail.com"):
    mycontext = ssl.create_default_context()
    host = "smtp.gmail.com"
    port = 465
    pw = os.getenv("PASSWORD")
    mycontext = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=mycontext) as server:
        server.login(username, pw)
        server.sendmail(username, receiver, message)