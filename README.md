# CatFactory: RocketData 🚀
___
# Installation ⚙️

1. `git clone https://github.com/WittyB0y/CatFactory.git` - Clone the project from GitHub.
2. `cd CatFactory` - Go to the directory with docker-compose.yml.
3. `docker-compose build` - Build image for Docker ().
4. `docker-compose up` - Up containers.
5. `docker-compose run --rm web-app sh -c "python manage.py makemigrations"` - Prepare for migrations.
6. `docker-compose run --rm web-app sh -c "python manage.py migrate"` - Do migrate.
7. `docker-compose run --rm web-app sh -c "python manage.py fill_db_user"` - Fill up DB with test user data.
8. `docker-compose run --rm web-app sh -c "python manage.py fill_db_product"` - Fill up DB with test product data.
9. `docker-compose run --rm web-app sh -c "python manage.py fill_db_company"` - Fill up DB with test company data.

### You launched the project! 🐱‍

---
# Links 

#### Project (CatFactory) 🏭: http://localhost:8000/admin/ 
#### Swagger 📖: http://localhost:8000/swagger/
#### Flower 🌼: http://localhost:5555/

---
# Login details for admin 🆔
##### Login: `admin`
##### Password: `admin`

---
# Conclusion ✏️

✅ All tasks were completed! ✅

# ⚠️ I didn't delete .env file from project! ⚠️