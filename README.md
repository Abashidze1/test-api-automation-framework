# API Automation Framework

Automation framework for testing [JSONPlaceholder](https://jsonplaceholder.typicode.com/) REST API.

## Tech Stack

- Python
- Requests — HTTP client
- Pytest — test runner
- Pydantic — response schema validation
- Loguru — logging
- GitHub Actions — CI/CD

## Project Structure

```
api-framework/
│
├── clients/              
│   ├── base_client.py    
│   ├── posts_client.py  
│   └── users_client.py 
│
├── models/              
│   ├── post_model.py
│   └── user_model.py
│
├── data/                  
│   └── test_data.py
│
├── utils/
│   └── logger.py         
│
├── tests/
│   ├── posts/           
│   └── users/
│
├── conftest.py            
├── pytest.ini              
└── requirements.txt
```

## Test Categories

Tests are organized using markers:

- `smoke` — quick checks that endpoints are alive and return expected schema
- `positive` — correct usage with valid data
- `negative` — invalid data / non-existent resources
- `parametrize` — same test repeated with multiple data sets
