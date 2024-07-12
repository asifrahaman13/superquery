import { SuccessEntity } from '../entities/Success';

export interface FileInterface {
  uploadFiles(token: string, formData: any): Promise<SuccessEntity | undefined>;
  presignedUrls(token: string): Promise<SuccessEntity | undefined>;
}
