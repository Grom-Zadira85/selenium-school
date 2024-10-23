from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from enum import Enum
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:5173",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Priority(str, Enum):
    low = "низкий"
    medium = "средний"
    high = "высокий"


def generate_id():
    return len(cases)


class Case(BaseModel):
    id: int = Field(default_factory=generate_id)
    name: str = Field(max_length=100)
    description: str = Field(max_length=1000)
    steps: list[str]
    expected_result: str
    priority: Priority = Field(max_length=10)


cases = []


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/testcases/", response_model=Case)
def create_test_case(test_case: Case):
    cases.append(test_case)
    return test_case


@app.get("/testcases/{test_case_id}", response_model=Case)
def read_test_case(test_case_id: int):
    for test in cases:
        if test.id == test_case_id:
            return test
    raise HTTPException(status_code=404, detail="Test case not found.")


@app.get("/testcases/", response_model=list[Case])
def read_cases():
    return cases


@app.put("/testcases/{test_case_id}", response_model=Case)
def update_case(test_case_id: int, updated_case: Case):
    for index, test in enumerate(cases):
        if test.id == test_case_id:
            cases[index] = updated_case
            return updated_case
    raise HTTPException(status_code=404, detail="Test case not found.")


@app.delete("/testcases/{test_case_id}", response_model=dict)
def delete_test_case(test_case_id: int):
    for index, test in enumerate(cases):
        if test.id == test_case_id:
            cases.pop(index)
            return {"detail": "Test case deleted."}
    raise HTTPException(status_code=404, detail="Test case not found.")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
