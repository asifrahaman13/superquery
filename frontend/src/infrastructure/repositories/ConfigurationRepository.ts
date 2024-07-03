import axios from 'axios';
import { SuccessEntity } from '@/domain/entities/Success';

class ConfigurationRepository {
  private backend_url = process.env.NEXT_PUBLIC_BACKEND_URL;
  async getConfiguration(dbType: string, token: string) {
    try {
      const response = await axios.post(
        `${this.backend_url}/config/configurations`,
        {
          db_type: dbType,
        },
        {
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (response.status === 200) {
        return new SuccessEntity(200, response.data);
      }
    } catch (e) {
      throw new Error("Couldn't get configurations");
    }
  }
}
export default ConfigurationRepository;
