import axios from "axios";
axios.defaults.baseURL = 'http://127.0.0.1:3000/';
export default class DataManager {
  static Test() {
    return axios.get('test',);
  }
  static Data_Lime100_port(start) {
    return axios.get('data_lim100_port',{params:{
        start:start
      }});
  }
  static Data_Lime100_protocol(start) {
    return axios.get('data_lim100_protocol',{params:{
        start:start
      }});
  }
  static Data_Lime100_length(start) {
    return axios.get('data_lim100_length',{params:{
        start:start
      }});
  }
  static Data_lim100(start) {
    return axios.get('data_lim100',{params:{
        start:start
      }});
  }
}
