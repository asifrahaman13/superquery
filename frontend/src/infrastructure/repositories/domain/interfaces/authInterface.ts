import { SuccessEntity } from "../entities/Success";

export interface AuthInterface {
    signup(email: string, username: string, password: string): Promise<SuccessEntity | undefined>;
    login(username: string, password: string): Promise<SuccessEntity | undefined>;
}

