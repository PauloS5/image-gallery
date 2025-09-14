from sqlmodel import SQLModel, Field

class Image(SQLModel, table=True):
    id: int = Field(
        default=None,
        primary_key=True,
        title="ID",
        description="Identificador único da imagem")
    filename: str = Field(
        unique=True, 
        title="Nome do arquivo",
        description="Diretório onde o arquivo de imagem está salvo")
    content_type: str = Field(
        title="Tipo",
        description="Tipo da imagem")
    title: str = Field(
        title="Título",
        description="Título da imagem")
    desc:str = Field(
        default=None,
        title="Descrição",
        description="Descrição da imagem")