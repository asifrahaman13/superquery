import ConfigurationRepository from '@/infrastructure/repositories/ConfigurationRepository';
import { ConfigurationInterface } from '../interfaces/configInterface';

class ConfigurationService implements ConfigurationInterface {
  private configRepository: ConfigurationRepository;

  constructor(configRepository: ConfigurationRepository) {
    this.configRepository = configRepository;
  }

  async getConfiguration(dbType: string, token: string) {
    return this.configRepository.getConfiguration(dbType, token);
  }
}

export default ConfigurationService;
