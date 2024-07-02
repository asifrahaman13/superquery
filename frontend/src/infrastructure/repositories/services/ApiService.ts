import axios from 'axios';
class ApiService {
    async fetchData(url: string) {
      // Logic to fetch data from an external API
      const response = await axios.get(url);
      console.log(response)
      return response;
    }
  }
  
  export default ApiService;
  