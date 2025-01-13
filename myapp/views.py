import pymysql
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.contrib import messages
import os


def index(request):
    # Establish connection to the database
    load_dotenv()
    timeout = 10
    connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db=os.getenv("database"),
    host=os.getenv("host"),
    password=os.getenv("password"),
    read_timeout=timeout,
    port=int(os.getenv("port")),
    user=os.getenv("user"),
    write_timeout=timeout,
    )
    
    
    

    try:
        with connection.cursor() as cursor:
            # Fetch all events (only upcoming events)
            cursor.execute("SELECT * FROM event WHERE date >= %s ORDER BY date", (now(),))
            events = cursor.fetchall()

        # Handle form submission
        if request.method == "POST":
            email = request.POST.get('email')
            prayer_request = request.POST.get('prayerRequest')

            # Check if the required fields are filled
            if email and prayer_request:
                with connection.cursor() as cursor:
                    # Insert prayer request into the database
                    cursor.execute(
                        "INSERT INTO prayer_request (r_email, request) VALUES (%s, %s)",
                        (email, prayer_request),
                    )
                    connection.commit()  # Commit the transaction

                messages.success(request, "Your prayer request has been submitted successfully!")
                return redirect('index')  # Redirect to prevent form resubmission
            else:
                messages.error(request, "Please fill in all fields.")

        # Context for rendering the template
        context = {
            'events': events,
        }

    finally:
        connection.close()  # Always close the database connection

    return render(request, 'layout.html', context)
