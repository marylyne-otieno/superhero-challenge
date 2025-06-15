
Superheroes Flask API

## 📖 Description

This is a Flask-based RESTful API for managing superheroes and their powers. The API allows users to:
- View all heroes and powers
- Retrieve a specific hero or power
- Update power descriptions
- Create relationships between heroes and powers with strengths like "Strong", "Weak", or "Average"

This project was built as part of the Phase 4 Code Challenge.


## 👩‍💻 Author

**Marylyne Otieno**
[GitHub Profile](https://github.com/marylyne-otieno)



##  Setup Instructions

### 1. Clone the repository

 bash
git clone https://github.com/your-username/superheroes-api.git
cd superheroes-api
2. Create and activate a virtual environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run migrations and seed the database
bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python seed.py
5. Run the app
bash
Copy
Edit
flask run
The API will be available at http://127.0.0.1:5556/

 API Endpoints
Heroes
GET /heroes – Get all heroes

GET /heroes/<id> – Get a single hero with powers

Powers
GET /powers – Get all powers

GET /powers/<id> – Get a specific power

PATCH /powers/<id> – Update a power's description

Hero Powers
POST /hero_powers – Assign a power to a hero with a strength level


 Postman Collection
A Postman collection is provided for testing all API endpoints. To use it:

Open Postman

Click Import

Upload the file challenge-2-superheroes.postman_collection.json

Testing
Use the Postman collection to:

Retrieve and inspect API responses

Check validation errors

Confirm nested data structures

