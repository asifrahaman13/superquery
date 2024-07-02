import { SuccessEntity } from "../entities/Success";

interface PdfInterface {
  fetchAllPdfs(access_token: string): Promise<SuccessEntity | null>;
  fetchPdfPresignedUrl(access_token: string, pdfId: string): Promise<SuccessEntity | null>;
  uploadPdf(access_token: string, file: File, description: string, tag: string): Promise<SuccessEntity | null>;
  deletePdf(access_token: string, pdfId: string): Promise<SuccessEntity | null>;
}
export default PdfInterface;
