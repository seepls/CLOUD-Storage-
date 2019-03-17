
var storageRef = firebase.storage().ref();
var imagesRef = storageRef.child('images');
var fileName = 'space.jpg';
var spaceRef = imagesRef.child(fileName);
var path = spaceRef.fullPath

var name = spaceRef.name

var imagesRef = spaceRef.parent;
