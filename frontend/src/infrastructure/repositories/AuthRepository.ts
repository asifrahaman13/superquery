import { SuccessEntity } from '@/domain/entities/Success';
import axios from 'axios';

class AuthRepository {
  async signup(email: string, username: string, password: string) {
    const backend_url = process.env.NEXT_PUBLIC_BACKEND_URL;

    const response = await axios.post(`${backend_url}/auth/signup`, {
      email,
      username,
      password,
    });

    if (response.status === 200) {
      return new SuccessEntity(200, response.data.data);
    }
  }

  async login(username: string, password: string) {
    const backend_url = process.env.NEXT_PUBLIC_BACKEND_URL;

    const response = await axios.post(`${backend_url}/auth/login`, {
      username,
      password,
    });

    if (response.status === 200) {
      return new SuccessEntity(200, response.data);
    }
  }
}

export { AuthRepository };
