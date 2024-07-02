import User from "../entities/User";
interface UserRepositoryInterface {
  getById(id: string): Promise<User | null>;
}

export default UserRepositoryInterface;
