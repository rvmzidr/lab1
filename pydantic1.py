from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value


user = User(name='Ali', email='ali@gmail.com', account_id=1234)

# JSON string
user_json_str = user.model_dump_json()
print("JSON string:", user_json_str)


user_recreated = User.model_validate_json(user_json_str)
print("User from JSON:", user_recreated)