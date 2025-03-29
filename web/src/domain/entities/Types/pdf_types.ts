export interface PdfInfo {
  _id: string;
  pdf_name: string;
  tag: string;
  username: string;
  description: string;
}

export interface ChatResponses {
  text: string;
  ai: boolean;
}
