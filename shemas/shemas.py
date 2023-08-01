from pydantic import BaseModel


class Data(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class Support(BaseModel):
    url: str
    text: str


class ListResourses(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[Data]
    support: Support


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class User(BaseModel):
    data: UserData
    support: Support


class UnsuccessfulRegister(BaseModel):
    error: str


class CreatedUser(BaseModel):
    id: str
    createdAt: str


class LoginSuccessful(BaseModel):
    token: str


class UpdateUser(BaseModel):
    name: str
    job: str
    updatedAt: str
