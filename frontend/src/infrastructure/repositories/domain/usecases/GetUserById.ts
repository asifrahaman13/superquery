import UserRepositoryInterface from '../interfaces/userInterfaces';

class GetUserById {
  private userRepository: UserRepositoryInterface;

  constructor(userRepository: UserRepositoryInterface) {
    this.userRepository = userRepository;
  }

  async execute(id: string) {
    return this.userRepository.getById(id);
  }
}

export default GetUserById;
