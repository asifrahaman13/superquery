import { AuthRepository } from '@/infrastructure/repositories/AuthRepository';
import { AuthInterface } from '@/domain/interfaces/authInterface';
import { AuthService } from '@/domain/usecases/authService';

const authRepository: AuthInterface = new AuthRepository();
const auth_interface: AuthInterface = new AuthService(authRepository);

export { auth_interface };
