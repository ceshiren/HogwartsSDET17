import axios from "./http"
const testcase = {
    getTestcase() {
        return axios.get("/testcase/get")
    }
}

export default testcase;