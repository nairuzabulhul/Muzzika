
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 

TheNewBoston Django Tutorial Notes
1- 

2- 

8- Activating Database:
   Whenever there is a change in the Model.py file, run two commands:
    - python manage.py makemigrations
    - python manage.py migrate

9- Database API
    -- Use python manage.py shell
    -- Populate the Database:
        album1 = Album() pass the paramenter inside the Album object
                -- album1 = Album(album_title= "", artist="", album_logo="")

    -- save the changed to the database
       album1.save()
       
    -- updating elements in the database
        album1.title = "NEW NAME"
        album1.save()
        
10 - Filtering the Database Results:

    album1 = Album.objects.filter(artist__startswith="Name")

11- Admin Interface

    Create admin account
    >> python manage.py createsuperuser 
    >> enter username, email and password
    
    -- To manage the database from the admin interface
      Add the models to the admin.py file
      >> 
      
12- Writing Another View

    creating a detailed view with an custom id
     1- urls.py
     - 0-9 + means that the id number includes all numbers
    urlpatterns= [
            # /music/id_number
            
            url(r'^(?P<album_id>[0-9]+)/$')
        ]

     2- views.py
        create a view for show the custom page (that has special id)
        
        def detailed_views(request, album_id):
          pass

13- Connecting to the Database

    album = Album.objects.all()
    

14- Templates:
     - User render (request, "TemplatesNAME.htm", {context})
     context to connect view with html template

15- Rasing 404 Error 

    import Http404
    use try and except to raise the 404 error or render custom error page 
    


17 - Adding Songs to our Database    
    - To specify specific album 
    album1 = Album.objects.get(pk=1)
    album1.song_set.create(song_title="New song")
    album1.save()
    
    this addes a new song to the album 
    
    - To count the songs in the album 
       album.song_set.count()
    
19 - Designing the detail page
    

20- remove hardcored URLs (Creating Dynamic urls)

    
22- Simple Form:
    - Add Favorite attribute to the Song model (BooleanField(default=False)
    - Add the url for favorit songs

    
  
23-   
