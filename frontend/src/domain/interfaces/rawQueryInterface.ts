import { SuccessEntity } from '../entities/Success';

export interface RawQueryInterface {
  rawQuery(
    query: string,
    token: string,
    dbType: string
  ): Promise<SuccessEntity | undefined>;
}
