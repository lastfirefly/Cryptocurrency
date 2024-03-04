import pandas as pd

class ExtractArquive:
    def __init__(self, arquiveName: str, urlDownload: str):
        self.name = arquiveName
        self.url = urlDownload

    def ReadUrl(self):
        fileName = pd.read_csv(f'{self.url}', sep=',')
        return fileName
