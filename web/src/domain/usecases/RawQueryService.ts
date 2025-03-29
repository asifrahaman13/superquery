import RawQueryRepository from '@/infrastructure/repositories/RawQueryRepository';
import { RawQueryInterface } from '../interfaces/rawQueryInterface';

class RawQueryService implements RawQueryInterface {
  private rawQueryRepository: RawQueryRepository;

  constructor(rawQueryRepository: RawQueryRepository) {
    this.rawQueryRepository = rawQueryRepository;
  }

  async rawQuery(query: string, token: string, dbType: string) {
    return this.rawQueryRepository.rawQuery(query, token, dbType);
  }
}

export default RawQueryService;
