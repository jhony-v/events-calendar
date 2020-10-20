import { KEY_PERSIST_STORAGE } from "../config/const";

export default class AuthPersistStorageService {
  /**
   * Set a token value
   * @param value
   */
  static setValue = (value: string) => {
    localStorage.setItem(KEY_PERSIST_STORAGE, value);
  };

  /**
   * Get the token value
   */
  static getValue = (): string => {
    return localStorage.getItem(KEY_PERSIST_STORAGE) || "";
  };

  /**
   * Delete the value from storage
   */
  static clear = () => {
    localStorage.removeItem(KEY_PERSIST_STORAGE);
  };
}
