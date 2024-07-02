import { SuccessEntity } from "../entities/Success";

export interface PdfChatInterface {
  getChatResponse(access_token: string, filename: string, question: string): Promise<SuccessEntity | null>;
}


