"""
data stored on google - cloud storage bucket .
already have configured firebase SDK 

Cloud Storage for Firebase provides a declarative rules language that allows you to define how your data should be structured,
how it should be indexed, and when your data can be read from and written to
By default, read and write access to Storage is restricted so only authenticated users can read or write data. 

--
This does make Storage open to anyone, even people not using your app, 
so be sure to restrict your Storage again when you set up authentication.

as we store data in bucket . ADD : bucket to FireBase SDK configuration  .

get Storage bucket url :::  add the storageBucket attribute to your config Object:

SECURITY :
By default, your rules allow all reads and writes.
Once you have defined your data structure, you will have to write rules to secure your data specific to your app
"""
service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read, write: if request.auth != null;
    }
  }
}

-------my url  :: gs://crowdalert-webapp-a5719.appspot.com/--------

# configuration 
var config = {
    apiKey: '<your-api-key>',
    authDomain: '<your-auth-domain>',
    databaseURL: '<your-database-url>',
    storageBucket: '<your-storage-bucket>'
  };
  firebase.initializeApp(config);

  // Get a reference to the storage service, which is used to create references in your storage bucket
  var storage = firebase.storage();
  
