import PdfChatRepository from "@/infrastructure/repositories/PdfChatRepository";

class PdfChatService {
  private pdfChatRepository: PdfChatRepository;
  constructor(pdfChatRepository: PdfChatRepository) {
    this.pdfChatRepository = pdfChatRepository;
  }

  async getChatResponse(access_token: string, filename: string, question: string) {
    return this.pdfChatRepository.getChatResponse(access_token, filename, question);
  }
}

export default PdfChatService;
