import { AuthInterface } from '@/domain/interfaces/authInterface';
import { AuthRepository } from '@/infrastructure/repositories/AuthRepository';

class AuthService implements AuthInterface {
  private authRepository: AuthRepository;

  constructor(authRepository: AuthRepository) {
    this.authRepository = authRepository;
  }

  async signup(email: string, username: string, password: string) {
    return this.authRepository.signup(email, username, password);
  }

  async login(username: string, password: string) {
    return this.authRepository.login(username, password);
  }
}

export { AuthService };
