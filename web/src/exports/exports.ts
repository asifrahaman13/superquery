import { AuthRepository } from '@/infrastructure/repositories/AuthRepository';
import { AuthInterface } from '@/domain/interfaces/authInterface';
import { AuthService } from '@/domain/usecases/authService';
import ConfigurationRepository from '@/infrastructure/repositories/ConfigurationRepository';
import ConfigurationService from '@/domain/usecases/ConfigurationService';
import { ConfigurationInterface } from '@/domain/interfaces/configInterface';
import RawQueryRepository from '../infrastructure/repositories/RawQueryRepository';
import RawQueryService from '@/domain/usecases/RawQueryService';
import { RawQueryInterface } from '@/domain/interfaces/rawQueryInterface';
import FileRepository from '@/infrastructure/repositories/FileRepository';
import { FileInterface } from '@/domain/interfaces/fileInterface';
import FileService from '@/domain/usecases/uploadService';

const authRepository: AuthRepository = new AuthRepository();
const auth_interface: AuthInterface = new AuthService(authRepository);

const configurationRepository: ConfigurationRepository =
  new ConfigurationRepository();
const configuration_interface: ConfigurationInterface =
  new ConfigurationService(configurationRepository);

const rawQueryRepository: RawQueryRepository = new RawQueryRepository();
const raw_query_interface: RawQueryInterface = new RawQueryService(
  rawQueryRepository
);

const fileRespository: FileRepository = new FileRepository();
const file_interface: FileInterface = new FileService(fileRespository);

export {
  auth_interface,
  configuration_interface,
  raw_query_interface,
  file_interface,
};
