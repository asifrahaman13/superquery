import { SuccessEntity } from '@/domain/entities/Success';
import axios from 'axios';

class RawQueryRepository {
  private backend_url = process.env.NEXT_PUBLIC_BACKEND_URL;

  async rawQuery(query: string, token: string, dbType: string) {
    try {
      const response = await axios.post(
        `${this.backend_url}/raw-query/raw-query`,
        {
          raw_query: query,
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
      throw new Error("Couldn't get raw query");
    }
  }
}

export default RawQueryRepository;
