from sqlmodel import SQLModel, Field

class ImageBase(SQLModel, table=True):
    title: str = Field(
        title="Título",
        description="Título da imagem para aparecer na interface")
    desc: str = Field(
        default=None,
        title="Descrição",
        description="Descrição da imagem")
    
class ImageCreate(ImageBase):
    pass

class ImageRead(ImageBase):
    id: int = Field(
        title="ID",
        description="Identificador único da imagem")
    content_type: str = Field(regex="^image/[a-z]+$")
    url: str

class ImageUpdate(ImageBase):
    id: int = Field(
        title="ID",
        description="Identificador único da imagem")

class ImageDelete(ImageBase):
    id: int = Field(
        title="ID",
        description="Identificador único da imagem")