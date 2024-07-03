import { AuthRepository } from '@/infrastructure/repositories/AuthRepository';
import { AuthInterface } from '@/domain/interfaces/authInterface';
import { AuthService } from '@/domain/usecases/authService';
import ConfigurationRepository from '@/infrastructure/repositories/ConfigurationRepository';
import ConfigurationService from '@/domain/usecases/ConfigurationService';
import { ConfigurationInterface } from '@/domain/interfaces/configInterface';

const authRepository: AuthRepository = new AuthRepository();
const auth_interface: AuthInterface = new AuthService(authRepository);

const configurationRepository: ConfigurationRepository =
  new ConfigurationRepository();
const configuration_interface: ConfigurationInterface =
  new ConfigurationService(configurationRepository);

export { auth_interface, configuration_interface };
