import { SuccessEntity } from '@/domain/entities/Success';
import axios from 'axios';

class AuthRepository {
  private backend_url = process.env.NEXT_PUBLIC_BACKEND_URL;
  async signup(email: string, username: string, password: string) {
    const response = await axios.post(`${this.backend_url}/auth/signup`, {
      email,
      username,
      password,
    });

    if (response.status === 200) {
      return new SuccessEntity(200, response.data.data);
    }
  }

  async login(username: string, password: string) {
    const response = await axios.post(`${this.backend_url}/auth/login`, {
      username,
      password,
    });

    if (response.status === 200) {
      return new SuccessEntity(200, response.data);
    }
  }
}

export { AuthRepository };
