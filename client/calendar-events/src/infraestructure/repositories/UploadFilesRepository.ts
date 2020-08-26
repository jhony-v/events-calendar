import storage from "../config/storage";

interface UploadReference {
  path: string;
  file: File;
}

export default class UploadFilesRepository {
  uploadNewFile = async ( dataUpload: UploadReference ): Promise<firebase.storage.UploadTaskSnapshot> => {
    const refStorage: firebase.storage.Reference = storage.ref(dataUpload.path);
    const putUpload = await refStorage.put(dataUpload.file);
    return putUpload;
  };

  deleteFile = async (path: string): Promise<boolean> => {
    const refStorage = storage.ref(path);
    const promiseDelete = refStorage.delete();
    return promiseDelete.then(() => true).catch(() => false);
  };
}
