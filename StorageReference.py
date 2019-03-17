"""
files stored in google cloud storage bucket.files in the bucket follow heirarchieal structure .
reference can point to a specific file or to a higher level node in the heirarchy .
STEP1 : create a reference to the file you want t operate on 

reference : pointer to file in cloud.
-are lightweight 
- reusable for multiple operations
"""

// Get a reference to the storage service, which is used to create references in your storage bucket
var storage = firebase.storage();

// Create a storage reference from our storage service
var storageRef = storage.ref();

// Create a child reference
var imagesRef = storageRef.child('images');
// imagesRef now points to 'images'

// Child references can also take paths delimited by '/'
var spaceRef = storageRef.child('images/space.jpg');
// spaceRef now points to "images/space.jpg"
// imagesRef still points to "images"

# navigation to parent or root 
var imagesRef = spaceRef.parent;
var rootRef = spaceRef.root;

reference properties :
spaceRef.fullPath;
spaceRef.name;
spaceRef.bucket;
