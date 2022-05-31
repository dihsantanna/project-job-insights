from functools import lru_cache
import csv


@lru_cache
def read(path):
    try:
        print(f"Abrindo arquivo no caminho '{path}'")
        with open(path, encoding="utf-8") as file:
            jobs_reader = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = jobs_reader
            info_jobs = list()

            for job in data:
                info = dict()
                for index in range(len(header)):
                    info[header[index]] = job[index]

                info_jobs.append(info)

            print("Manipulação de arquivo feita com sucesso")
            return info_jobs

    except OSError:
        print("Arquivo inexistente")
    finally:
        print("Processamento Encerrado")
