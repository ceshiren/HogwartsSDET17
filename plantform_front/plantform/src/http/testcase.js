import axios from "./http";
const testcase = {
  getTestcase() {
    return axios.get("/testcase/get");
  },
  deleteTestCase(nodeid) {
    return axios.get("/testcase/delete", { params: nodeid });
  },
  addTestCase(data) {
    return axios.post("/testcase/add", data);
  },
  updateTestCase(data) {
    return axios.post("/testcase/update", data);
  },
  runTestCase() {
      return axios.get("/testcase/run")
  }
};

export default testcase;
