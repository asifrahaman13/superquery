import FileRepository from '@/infrastructure/repositories/FileRepository';
import { FileInterface } from '../interfaces/fileInterface';
import { SuccessEntity } from '../entities/Success';

class FileService implements FileInterface {
  private fileRepository: FileRepository;

  constructor(fileRepository: FileRepository) {
    this.fileRepository = fileRepository;
  }

  async uploadFiles(token: string, formData: any) {
    return this.fileRepository.uploadFile(token, formData);
  }

  async presignedUrls(token: string): Promise<SuccessEntity | undefined> {
    return this.fileRepository.presignedUrls(token);
  }
}

export default FileService;
