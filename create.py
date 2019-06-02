import sys
import os
import time
from github3 import login


gitUser = '<usuario>'
gitPass = '<senha>'

github = login(gitUser, gitPass)

repository = None


def create():
    folderName = str(sys.argv[1])

    try:
        os.mkdir(f'C:/Users/wsm/{folderName}')
        print(f'Diretório {folderName} criado com sucesso.')

    except FileExistsError:
        print(f"Diretório {folderName} já existe.")

    else:
        repository = github.create_repository(name=folderName)
        if repository:
            print(f"Repositorio git {folderName} criado com sucesso.")


if __name__ == "__main__":
    create()
