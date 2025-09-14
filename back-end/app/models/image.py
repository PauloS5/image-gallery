from sqlmodel import SQLModel, Field

class Image(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True,
        title="ID", description="Identificador único da imagem")
    filename: str = Field(unique=True, regex=r"^uploads/[a-zA-z\d_]+$",
        title="Nome do arquivo", description="Diretório onde o arquivo de imagem está salvo")
    title: str = Field(title="Título", description="Título da imagem para aparecer na interface")
    desc:str = Field(default=None,
        title="Descrição", description="Descrição da imagem")