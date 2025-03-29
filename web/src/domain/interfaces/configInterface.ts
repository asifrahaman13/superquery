import { SuccessEntity } from '../entities/Success';

export interface ConfigurationInterface {
  getConfiguration(
    dbType: string,
    token: string
  ): Promise<SuccessEntity | undefined>;

  updateConfiguration(
    token: string,
    configuration: any
  ): Promise<SuccessEntity | undefined>;
}
