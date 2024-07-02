import PdfInterface from "../interfaces/PdfInterface";

class FileService {
  private pdfRepository: PdfInterface;

  constructor(pdfRepository: PdfInterface) {
    this.pdfRepository = pdfRepository;
  }
  
  async uploadPdf(access_token: string, file: File, description: string, tag: string) {
    return this.pdfRepository.uploadPdf(access_token, file, description, tag);
  }

  async fetchAllPdfs(access_token: string) {
    return this.pdfRepository.fetchAllPdfs(access_token);
  }

  async fetchPdfPresignedUrl(access_token: string, pdfId: string) {
    return this.pdfRepository.fetchPdfPresignedUrl(access_token, pdfId);
  }

  async deletePdf(access_token: string, pdfId: string) {
    return this.pdfRepository.deletePdf(access_token, pdfId);
  }
}

export default FileService;
