# Tercera-pre_entrega_Martinez


Project name: NetZero Elevate Consulting

About Us
Specializing in comprehensive sustainability consulting services for diverse industries. The mission is to guide businesses toward achieving net-zero goals by implementing innovative, efficient, and sustainable practices. A team of dedicated experts offers tailored solutions that enhance environmental performance while driving economic growth and resilience.

Our Values
Commitment to sustainability, innovation, and integrity drives every project. Strive to create lasting value for clients by integrating eco-friendly solutions that promote both environmental stewardship and business success.

Our Impact Plan
Focus on measurable results, helping businesses reduce their carbon footprint, improve resource efficiency, and comply with regulatory standards. Emphasis on continuous improvement and adaptation to ensure long-term sustainability and resilience.

Functionalities
HTML Inheritance
All templates inherit from index.html.

Models
Three models have been defined in models.py: Industries, Services, Team.

Data Insertion Forms
Forms have been created to insert data into all the classes in models.py.

Search Form
A form has been implemented to search for data in the database.

Project Structure
index.html: Base template for HTML inheritance.
team.html: Template for the team form.
models.py: Definition of the models Industries, Services, Team.
forms.py: Definition of the forms TeamForm, FeedbackForm.
views.py: Views to handle the forms and the search.

Instructions to Test the Project
1. Clone the repository.
2. Install the dependencies.
3. Run the migrations with python manage.py makemigrations and python manage.py migrate.
4. Start the development server with python manage.py runserver.
5. Navigate to http://127.0.0.1:8000/ to access the main page.
6. Test the contact form at http://127.0.0.1:8000/contact/.
7. Test the search form at http://127.0.0.1:8000/search/.





