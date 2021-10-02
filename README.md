## Py

### This project is build on python and Docker is used.  
----

### Steps to run the project

1. Clone the project
2. Go inside the folder
    
       Vernacular.ai_task
   
3. Build Docker image:
    
        docker build -t project:1.0 .

4. Run the image:
        
       docker run -p 8000:8000 -i -t project:1.0

---
### Curl command for api:

1. **validate_finite_values_entity_api** 
    
        curl --location --request POST 'http://127.0.0.1:8000/api/validate_value' \
        --header 'Authorization: SLA083fb498-8ab3-48ef-83af-fdf0af77eae4TE' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "invalid_trigger": "invalid_ids_stated",
          "key": "ids_stated",
          "name": "govt_id",
          "reuse": true,
          "support_multiple": true,
          "pick_first": false,
          "supported_values": [
            "pan",
            "aadhaar",
            "college",
            "corporate",
            "dl",
            "voter",
            "passport",
            "local"
          ],
          "type": [
               "id"
          ],
          "validation_parser": "finite_values_entity",
          "values": [
              {
                "entity_type": "id",
                "value": "college"
              }
          ]
        }'

2. **validate_numeric**
        
        curl --location --request POST 'http://127.0.0.1:8000/api/validate_numeric' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "invalid_trigger": "invalid_age",
            "key": "age_stated",
            "name": "age",
            "reuse": true,
            "pick_first": false,
            "support_multiple": true,
            "type": [
                "number"
            ],
            "validation_parser": "numeric_values_entity",
            "constraint": "x>=18 and x<=30",
            "var_name": "x",
            "values": [
                {
                "entity_type": "number",
                "value": 22
                }
            ]
        }'

---

### Note

- Docker image size: 481MB 
