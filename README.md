# Task2
Ques 5. Learn how to handle file uploads in Flask (https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask)

Ans 5. Python Filename: app.py
       
       HTML Filename: index.html
       
       Decription of the code: app.py file contains the code to upload the file and also contains the code to display the uploaded file.index.html file is used to provide the                template to the application
       
       
       
Ques 6. Learn how to pass GET/POST data to Flask (https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask)

Ans 6. Pythn Filename: app2.py
       
       HTML Filenames: index1.html,login.html 
       
       Decription of the code: app.py2 file contains the code to perform the get and post operation and also display the values enter in the post operation. index1.html file is used 
       to provide the navigation bar in the application index1.html file also contain the jinja2 block to perform the templates inheritance between different templates. login.html is        used to provide the structure for the POST operation(username,Passsword,etc).
       
       

7. Finally, create a Flask app with an endpoint /upload where a user can upload a file along with a JSON structure as follows:
{
   orgID: 123,
   type:  "sales",
   year:  2021
}
You would then take the file and save it to a GCP bucket at path gcs://<bucket_name>/{orgID}/{year}/file-sales.csv

Ans 7. Python Filename: app3.py
       
       Screenshot Filename: Postman Json Request , CSV file uploaded at the specific location on GCP bucket
       
       Decription of the code: app3.py file contains a /upload endpoint where you we can upload the file(.csv) along with a JSON structure and upload that file(csv) in the GCP bucket        in the specified location which is gcs://<bucket_name>/{orgID}/{year}/file-sales.csv for example: gcs://resourcebusymanan_587/123/2021/october/file-sales.csv. Postman Json            Request conatains the screenshot of the request send the postman app. CSV file uploaded at the specific location on GCP bucket contains the screenshot displaying that the            file(.csv) is uploaded on the specified location in the GCP bucket.
       
