import pandas as pd

class ExtrairArquivo:
    def __init__(self, nomeArquivo: str, urlDownload: str):
        self.nome = nomeArquivo
        self.url = urlDownload

    def ReadUrl(self):
        nomeArquivo = pd.read_csv(f'{self.url}', sep=',')
        nomeArquivo = nomeArquivo.drop(columns=['SNo','Name'])
        
        return nomeArquivo
