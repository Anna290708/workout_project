

# 🏠 Home Workout Generator 🏋️‍♀️

Welcome to the **Home Workout Generator** — a web-based app that helps users stay active and fit from the comfort of their own home. Whether you're into pilates, yoga, cardio, or strength training, this app generates personalized workout plans tailored to your preferences!

🔗 **Live Site:** [https://workoutproject-production-94bc.up.railway.app/](https://workoutproject-production-94bc.up.railway.app/)

---

## 🚀 Features

* 🔐 **User Registration & Login**
  Secure authentication system with email verification and password reset.

* 🧠 **Custom Workout Generator**
  Generate workouts by selecting:

  * Type (e.g., arms, legs, cardio, yoga, pilates)
  * Difficulty level
  * Duration (short, medium, long)

* 💬 **Motivational Quotes**
  After generating a workout, users receive a random motivational quote to stay inspired. *(Coming soon to frontend)*

* 📜 **Workout History**
  Authenticated users can view their previously generated workouts.

* 🔍 **Filtering & Search**
  Easily find specific workouts based on type or difficulty.

* 🎨 **Beautiful & Responsive Design**
  Includes scroll animations, clean UI, and a light/dark mode toggle for a smooth user experience.

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Frontend:** HTML, CSS, Bootstrap (custom styling and animations)
* **Database:** SQLite (default for development)
* **Deployment:** [Railway](https://railway.app/)
* **Other Tools:** Git, GitHub

---

## 📁 Project Structure

```
workout_project/
├── users/              # Custom user model, registration, login, email verification
├── workout/            # Workout generation logic, models, and APIs
├── templates/          # HTML templates for registration, login, and home page
├── static/             # CSS and image files
├── manage.py
└── requirements.txt
```

---

## 📦 Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/YourUsername/workout_project.git
   cd workout_project
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the server**

   ```bash
   python manage.py runserver
   ```

---

## 📬 Future Plans

* Add video demonstrations for workouts
* Let users save favorite workouts
* Integrate progress tracking and reminders
* Improve motivational quote display on frontend


