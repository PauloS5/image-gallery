from sqlmodel import SQLModel, Field

class ImageBase(SQLModel, table=True):
    title: str = Field(
        title="Título",
        description="Título da imagem")
    desc: str = Field(
        default=None,
        title="Descrição",
        description="Descrição da imagem")
    
class ImageCreate(ImageBase):
    pass

class ImageRead(ImageBase):
    id: int = Field(
        title="ID",
        description="Identificador único da imagem"),
    content_type: str = Field(
        title="Tipo",
        description="Tipo da imagem")
    url: str = Field(
        title="URL",
        description="URL onde a imagem está armazenada")

class ImageUpdate(ImageBase):
    id: int = Field(
        title="ID",
        description="Identificador único da imagem")
    title: str = Field(
        default=None,
        title="Título",
        description="Título a ser modificado")

class ImageDelete(ImageBase):
    id: int = Field(
        title="ID",
        description="Identificador único da imagem")