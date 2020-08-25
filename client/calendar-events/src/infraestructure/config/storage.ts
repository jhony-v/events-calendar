import firebase from "firebase";

const firebaseConfigStorage = {
  apiKey: "",
  authDomain: "",
  databaseURL: "",
  storageBucket: "",
};

firebase.initializeApp(firebaseConfigStorage);

const storage: firebase.storage.Storage = firebase.storage();

export default storage;
