import storage from "../config/storage";

interface UploadReference {
  path: string;
  file: File;
}

type RefStorage = firebase.storage.Reference;

export default class ManageFilesRepository {
  uploadNewFile = async ( dataUpload: UploadReference ): Promise<firebase.storage.UploadTaskSnapshot> => {
    const refStorage: RefStorage = storage.ref(dataUpload.path);
    const putUpload = await refStorage.put(dataUpload.file);
    return putUpload;
  };

  deleteFile = async (path: string): Promise<boolean> => {
    const refStorage : RefStorage = storage.ref(path);
    const promiseDelete = refStorage.delete();
    return promiseDelete.then(() => true).catch(() => false);
  };

  downloadFile = async (path : string) : Promise<any> => {
    const refStorage : RefStorage = storage.ref(path);
    try {
      const fileDownload = await refStorage.getDownloadURL(); 
      return fileDownload;
    }
    catch(e) {
      return null;
    }
  }
}
