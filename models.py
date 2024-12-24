from typing import Annotated, List, Optional
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, field_validator

PyObjectId = Annotated[str, BeforeValidator(str)]


class CarModel(BaseModel):

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    brand: str = Field(...)
    make: str = Field(...)
    year: int = Field(..., gt=1970, lt=2025)
    cm3: int = Field(..., gt=0, lt=5000)
    km: int = Field(..., gt=0, lt=500000)
    price: int = Field(..., gt=0, lt=100000)

    @field_validator("brand")
    @classmethod
    def check_brand_case(cls, v: str) -> str:
        return v.title()

    @field_validator("make")
    @classmethod
    def check_make_case(cls, v: str) -> str:
        return v.title()

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "brand": "Ford",
                "make": "Fiesta",
                "year": 2019,
                "cm3": 1500,
                "km": 120000,
                "price": 10000,
            }
        }
    )

# test_car = CarModel(
#     brand="ford", make="fiesta", year=2019, cm3=1500, km=120000, price=10000
# )

# print(test_car.model_dump())

class UpdateCarModel(BaseModel):

    brand: Optional[str] = Field(...)
    make: Optional[str] = Field(...)
    year: Optional[str] = Field(..., gt=1970, lt=2025)
    cm3: Optional[int] = Field(..., gt=0, lt=5000)
    km: Optional[int] = Field(..., gt=0, lt=500 * 1000)
    price: Optional[int] = Field(..., gt=0, lt=100 * 1000)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "brand": "Ford",
                "make": "Fiesta",
                "year": 2019,
                "cm3": 1500,
                "km": 120000,
                "price": 10000,
            }
        },
    )

class CarCollection(BaseModel):
    cars: List[CarModel]