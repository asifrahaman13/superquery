import axios from 'axios';
import { SuccessEntity } from '@/domain/entities/Success';

class FileRepository {
  private backend_url = process.env.NEXT_PUBLIC_BACKEND_URL;

  async uploadFile(token: string, formData: any) {
    try {
      const response = await axios.post(
        `${this.backend_url}/upload/aws-file-upload`,
        formData,
        {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'multipart/form-data',
          },
        }
      );

      if (response.status === 200) {
        return new SuccessEntity(200, response.data);
      }
    } catch (error) {
      console.error('Error uploading file:', error);
      alert('Failed to save chart');
    }
  }

  async presignedUrls(token: string) {
    try {
      const response = await axios.get(
        `${this.backend_url}/upload/aws-file-url`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (response.status === 200) {
        return new SuccessEntity(200, response.data);
      }
    } catch (error) {
      console.error('Error getting presigned urls:', error);
      alert('Failed to get presigned urls');
    }
  }
}

export default FileRepository;
